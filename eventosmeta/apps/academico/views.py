"""
Arquivo: apps/academico/views.py
Caminho: apps/academico/views.py
Descrição: Views do app Acadêmico — certificados e gestão de matrículas
Atualizações:
- 12/01/2026 - Criação
- 02/02/2026 - Reorganização
- 24/07/2026 - Adicionadas views de gestao_matricula, processar_matricula e alterar_status_inscricao
- 29/07/2026 - Adicionado prefetch de Matricula na gestao_matricula_view
- 29/07/2026 - Implementada lógica real de matrícula na processar_matricula_view
- 30/07/2026 - Corrigido caminho do template matricular_alunos.html para academico/
"""

from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.db import transaction
from django.db.models import Prefetch

import io
import zipfile

from apps.eventos.models import Evento, Turma
from apps.selecao.models import Classificacao, Inscricao, StatusInscricao

from .models import Avaliacao, Matricula, StatusMatricula
from .certificado import GeradorCertificado

# ==========================================================================
# GESTÃO DE MATRÍCULAS
# ==========================================================================

@staff_member_required
def gestao_matricula_view(request):
    """
    Exibe a tela de gestão de matrícula.
    GET sem evento_id: mostra TODOS os classificados.
    GET com evento_id: filtra pelo evento selecionado.
    """
    evento_id = request.GET.get('evento_id')

    eventos_disponiveis = Evento.objects.filter(
        inscricoes__classificacao__isnull=False
    ).distinct().order_by('nome')

    evento_selecionado = None
    classificacoes = None

    prefetch_matriculas = Prefetch(
        'inscricao__matriculas',
        queryset=Matricula.objects.select_related('status').order_by('-data_matricula')
    )

    if evento_id:
        try:
            evento_selecionado = Evento.objects.get(pk=evento_id)
            classificacoes = Classificacao.objects.filter(
                inscricao__evento=evento_selecionado
            ).select_related(
                'inscricao__interessado',
                'inscricao__status',
                'inscricao__evento',
            ).prefetch_related(
                prefetch_matriculas
            ).order_by('posicao')
        except Evento.DoesNotExist:
            messages.error(request, 'Evento não encontrado.')
    else:
        classificacoes = Classificacao.objects.select_related(
            'inscricao__interessado',
            'inscricao__status',
            'inscricao__evento',
        ).prefetch_related(
            prefetch_matriculas
        ).order_by('inscricao__evento__nome', 'posicao')

    # Buscar cores dos status para os botoes
    status_cores = {}
    for status in StatusInscricao.objects.all():
        status_cores[str(status.ordem)] = status.cor    

    contexto = {
        'eventos_disponiveis': eventos_disponiveis,
        'evento_selecionado': evento_selecionado,
        'classificacoes': classificacoes,
        'status_cores': status_cores,
    }

    return render(request, 'academico/gestao_matricula.html', contexto)

@staff_member_required
@require_http_methods(["POST"])
def processar_matricula_view(request):
    """
    Processa a matrícula dos inscritos selecionados.
    POST sem confirmar_matricula: mostra página intermediária de seleção de turma.
    POST com confirmar_matricula: cria as matrículas.

    Lógica espelha a action matricular_alunos_action do admin (apps/selecao/admin.py).
    """
    print("=" * 50)
    print(f"VIEW CHAMADA: method={request.method}, POST keys={list(request.POST.keys())}")
    print("=" * 50)

    evento_id = request.POST.get('evento_id')
    inscricoes_ids = request.POST.getlist('inscricoes_selecionadas')

    # 1. Validar seleção
    if not inscricoes_ids:
        messages.error(request, 'Nenhuma inscrição selecionada.')
        return redirect(f'{reverse("academico:gestao_matricula")}?evento_id={evento_id}')

    # 2. Buscar inscrições com joins
    inscricoes = Inscricao.objects.filter(
        id__in=inscricoes_ids
    ).select_related('evento', 'interessado', 'status').order_by('interessado__nome')

    if not inscricoes.exists():
        messages.error(request, 'Inscrições não encontradas.')
        return redirect(f'{reverse("academico:gestao_matricula")}?evento_id={evento_id}')

    # 3. Validar evento único
    eventos_ids = set(insc.evento_id for insc in inscricoes if insc.evento_id)

    if len(eventos_ids) == 0:
        messages.error(request, 'As inscrições selecionadas não possuem evento associado.')
        return redirect(f'{reverse("academico:gestao_matricula")}?evento_id={evento_id}')

    if len(eventos_ids) > 1:
        messages.error(request, 'Selecione apenas inscrições do mesmo evento.')
        return redirect(f'{reverse("academico:gestao_matricula")}?evento_id={evento_id}')

    evento = Evento.objects.get(id=list(eventos_ids)[0])

    # 4. Verificar se o evento tem turmas
    turmas = Turma.objects.filter(evento=evento).order_by('nome')
    if not turmas.exists():
        messages.error(
            request,
            f'O evento "{evento.nome}" não possui turmas cadastradas. '
            f'Crie uma turma em Eventos > Turmas.'
        )
        return redirect(f'{reverse("academico:gestao_matricula")}?evento_id={evento_id}')

    # 5. SEGUNDO POST: confirmar_matricula
    if 'confirmar_matricula' in request.POST:
        turma_id = request.POST.get('turma')

        print("=" * 50)
        print(f"VIEW CHAMADA: method={request.method}, POST keys={list(request.POST.keys())}")
        print("=" * 50)


        if not turma_id:
            messages.error(request, 'Selecione uma turma.')
            context = {
                'evento': evento,
                'turmas': turmas,
                'inscricoes': inscricoes,
                'inscricoes_ids': inscricoes_ids,
                'total_selecionado': inscricoes.count(),
            }
            return render(request, 'academico/matricular_alunos.html', context)

        turma = get_object_or_404(Turma, pk=turma_id)

        # 5a. Validar turma pertence ao evento
        if turma.evento != evento:
            messages.error(
                request,
                f'A turma "{turma.nome}" não pertence ao evento "{evento.nome}".'
            )
            return redirect(f'{reverse("academico:gestao_matricula")}?evento_id={evento_id}')

        # 5b. Validar capacidade
        matriculas_existentes = Matricula.objects.filter(
            turma=turma,
            status__nome__iexact='ATIVA'
        ).count()
        vagas_restantes = turma.capacidade - matriculas_existentes
        total_selecionado = inscricoes.count()

        if total_selecionado > vagas_restantes:
            messages.error(
                request,
                f'Falha na operação: Você selecionou {total_selecionado} classificados, '
                f'mas a turma "{turma.nome}" possui apenas {vagas_restantes} vaga(s) '
                f'disponível(eis). (Capacidade total: {turma.capacidade}, '
                f'Matrículas atuais: {matriculas_existentes})'
            )
            return redirect(f'{reverse("academico:gestao_matricula")}?evento_id={evento_id}')

        # 5c. Buscar status necessários
        try:
            status_matricula_ativa = StatusMatricula.objects.get(nome__iexact='ATIVA')
        except StatusMatricula.DoesNotExist:
            messages.error(
                request,
                'Status "ATIVA" não encontrado em Status de Matrículas. Crie-o primeiro.'
            )
            return redirect(f'{reverse("academico:gestao_matricula")}?evento_id={evento_id}')

        try:
            status_inscricao_confirmada = StatusInscricao.objects.get(nome__iexact='CONFIRMADA')
        except StatusInscricao.DoesNotExist:
            messages.error(
                request,
                'Status "CONFIRMADA" não encontrado em Status de Inscrições. Crie-o primeiro.'
            )
            return redirect(f'{reverse("academico:gestao_matricula")}?evento_id={evento_id}')

        # 5d. Criar matrículas com atomicidade
        matriculas_criadas = 0
        erros = []

        with transaction.atomic():
            for inscricao in inscricoes:
                try:
                    interessado = inscricao.interessado

                    # Proteção contra duplicidade
                    if Matricula.objects.filter(turma=turma, interessado=interessado).exists():
                        erros.append(
                            f'{interessado.nome} já está matriculado nesta turma. '
                            f'Matrícula ignorada.'
                        )
                        continue

                    Matricula.objects.create(
                        turma=turma,
                        interessado=interessado,
                        inscricao=inscricao,
                        status=status_matricula_ativa
                    )

                    # Atualizar status da inscrição para CONFIRMADA
                    inscricao.status = status_inscricao_confirmada
                    inscricao.save()

                    matriculas_criadas += 1
                except Exception as e:
                    erros.append(f'Erro ao matricular {inscricao.interessado.nome}: {str(e)}')

        # 5e. Mensagens de feedback
        if matriculas_criadas > 0:
            messages.success(
                request,
                f'{matriculas_criadas} matrícula(s) criada(s) na turma "{turma.nome}"!'
            )
        if erros:
            for erro in erros:
                messages.warning(request, erro)

        return redirect(f'{reverse("academico:gestao_matricula")}?evento_id={evento_id}')

    # 6. PRIMEIRO POST: mostrar página intermediária
    print("=" * 50)
    print(f"VIEW CHAMADA: method={request.method}, POST keys={list(request.POST.keys())}")
    print("=" * 50)
    context = {
        'evento': evento,
        'turmas': turmas,
        'inscricoes': inscricoes,
        'inscricoes_ids': inscricoes_ids,
        'total_selecionado': inscricoes.count(),
    }
    return render(request, 'academico/matricular_alunos.html', context)

@staff_member_required
@require_http_methods(["POST"])
def alterar_status_inscricao_view(request):
    """
    Altera o status das inscricoes selecionadas.
    Caso especial: novo_status='remover_matricula' exclui a matricula
    e restaura o status da inscricao conforme classificacao.
    """
    evento_id = request.POST.get('evento_id')
    inscricoes_ids = request.POST.getlist('inscricoes_selecionadas')
    novo_status = request.POST.get('novo_status')

    if not inscricoes_ids:
        messages.error(request, 'Nenhuma inscricao selecionada.')
        return redirect(f'{reverse("academico:gestao_matricula")}?evento_id={evento_id}')

    # ==========================================
    # CASO ESPECIAL: REMOVER MATRICULA
    # ==========================================
    if novo_status == 'remover_matricula':
        matriculas = Matricula.objects.filter(
            inscricao_id__in=inscricoes_ids
        )
        total = matriculas.count()

        if total == 0:
            messages.warning(
                request,
                'Nenhuma matricula encontrada para as inscricoes selecionadas.'
            )
            return redirect(f'{reverse("academico:gestao_matricula")}?evento_id={evento_id}')

        # Buscar classificacoes das inscricoes selecionadas
        classificacoes = Classificacao.objects.filter(
            inscricao_id__in=inscricoes_ids
        )

        # Buscar status por ordem (campo Ordem da tabela)
        status_classificado = StatusInscricao.objects.get(ordem=2)   # Classificado
        status_espera = StatusInscricao.objects.get(ordem=4)         # Lista de Espera

        with transaction.atomic():
            # 1. Excluir as matriculas
            matriculas.delete()

            # 2. Atualizar status de cada inscricao conforme classificacao
            for classificacao in classificacoes:
                inscricao = classificacao.inscricao
                if classificacao.classificado:
                    inscricao.status = status_classificado
                elif classificacao.lista_espera:
                    inscricao.status = status_espera
                inscricao.save()

        messages.success(
            request,
            f'{total} matricula(s) removida(s). Status das inscricoes '
            f'atualizado conforme classificacao.'
        )
        return redirect(f'{reverse("academico:gestao_matricula")}?evento_id={evento_id}')

    # ==========================================
    # DEMAIS STATUS - MAPEAMENTO POR ORDEM
    # ==========================================
    mapa_status = {
        'pendente': 1,
        'cancelada': 5,
        'expirada': 6,
        'desistente': 7,
        'nao_localizado': 8,
    }

    if novo_status not in mapa_status:
        messages.error(request, f'Status "{novo_status}" invalido.')
        return redirect(f'{reverse("academico:gestao_matricula")}?evento_id={evento_id}')

    ordem_status = mapa_status[novo_status]
    status_inscricao = StatusInscricao.objects.get(ordem=ordem_status)

    inscricoes = Inscricao.objects.filter(id__in=inscricoes_ids)
    with transaction.atomic():
        for inscricao in inscricoes:
            inscricao.status = status_inscricao
            inscricao.save()

    mensagens = {
        'pendente': 'Pendente',
        'cancelada': 'Cancelada',
        'expirada': 'Expirada',
        'desistente': 'Desistente',
        'nao_localizado': 'Nao localizado para confirmar matricula',
    }

    messages.success(
        request,
        f'{len(inscricoes_ids)} inscricao(oes) marcada(s) como "{mensagens[novo_status]}".'
    )
    return redirect(f'{reverse("academico:gestao_matricula")}?evento_id={evento_id}')

# ==========================================================================
# CERTIFICADOS
# ==========================================================================

@staff_member_required
@require_http_methods(["GET"])
def download_certificado_individual(request, avaliacao_id):
    """
    Download individual de certificado em PDF
    """
    avaliacao = get_object_or_404(Avaliacao, pk=avaliacao_id)

    if not avaliacao.aprovado:
        return HttpResponse("Certificado disponível apenas para alunos aprovados.", status=400)

    buffer = io.BytesIO()
    gerador = GeradorCertificado(avaliacao)
    gerador.gerar_pdf(buffer)
    buffer.seek(0)

    aluno_nome = avaliacao.matricula.interessado.nome.replace(' ', '_')
    curso_nome = avaliacao.matricula.turma.evento.nome.replace(' ', '_')
    filename = f"Certificado_{aluno_nome}_{curso_nome}.pdf"

    response = FileResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return response

@staff_member_required
@require_http_methods(["GET"])
def preview_certificado(request, avaliacao_id):
    """
    Preview do certificado (visualizar no navegador)
    """
    avaliacao = get_object_or_404(Avaliacao, pk=avaliacao_id)

    if not avaliacao.aprovado:
        return HttpResponse("Certificado disponível apenas para alunos aprovados.", status=400)

    buffer = io.BytesIO()
    gerador = GeradorCertificado(avaliacao)
    gerador.gerar_pdf(buffer)
    buffer.seek(0)

    response = FileResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'inline'

    return response

@staff_member_required
@require_http_methods(["GET"])
def download_certificados_lote(request):
    """
    Download em lote de certificados (ZIP)
    """
    ids_str = request.GET.get('ids', '')
    ids = [int(id) for id in ids_str.split(',') if id.strip().isdigit()]

    if not ids:
        return HttpResponse("Nenhuma avaliação selecionada.", status=400)

    avaliacoes = Avaliacao.objects.filter(pk__in=ids, aprovado=True)

    if avaliacoes.count() == 0:
        return HttpResponse("Nenhum aluno aprovado foi selecionado.", status=400)

    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for avaliacao in avaliacoes:
            pdf_buffer = io.BytesIO()
            gerador = GeradorCertificado(avaliacao)
            gerador.gerar_pdf(pdf_buffer)
            pdf_buffer.seek(0)

            aluno_nome = avaliacao.matricula.interessado.nome.replace(' ', '_')
            matricula_num = avaliacao.matricula.numero_matricula
            filename = f"Certificado_{matricula_num}_{aluno_nome}.pdf"

            zip_file.writestr(filename, pdf_buffer.read())

    zip_buffer.seek(0)

    response = HttpResponse(zip_buffer, content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="Certificados_{len(avaliacoes)}_alunos.zip"'

    return response

