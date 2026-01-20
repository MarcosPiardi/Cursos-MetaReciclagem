"""
Arquivo: backup_tabelas.py
Caminho: eventosmeta/backup_tabelas.py
Descrição: Exporta tabelas específicas para arquivos JSON editáveis
Data: 14/01/2026
Correção: Usa sys.executable para garantir uso do Python do ambiente virtual
"""

import os
import sys
import subprocess
from datetime import datetime

# ========================================
# CONFIGURAÇÕES
# ========================================

BACKUP_DIR = r"C:\PMS\PMS2025\Inscr-Meta\backup_apagar_bd"

# Lista de tabelas para backup (formato: app.Model)
TABELAS = [
    'accounts.Usuario',
    'auth.Group',
    'auth.Permission',
    'academico.StatusMatricula',
    'eventos.Criterio',
    'eventos.Status',
    'interessados.FotoTipo',
    'interessados.Sexo',
    'selecao.StatusInscricao'
]

# ========================================
# FUNÇÕES
# ========================================

def criar_diretorio_backup():
    """Cria o diretório de backup se não existir"""
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
        print(f"✅ Diretório criado: {BACKUP_DIR}")
    else:
        print(f"📁 Diretório já existe: {BACKUP_DIR}")


def exportar_tabela(tabela):
    """
    Exporta uma tabela para arquivo JSON
    
    Args:
        tabela: Nome da tabela no formato 'app.Model'
    
    Returns:
        bool: True se sucesso, False se erro
    """
    # Nome do arquivo de saída
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"{tabela.replace('.', '_')}_{timestamp}.json"
    caminho_completo = os.path.join(BACKUP_DIR, nome_arquivo)
    
    # Comando Django dumpdata (usando sys.executable para garantir o Python correto)
    comando = [
        sys.executable,  # 🔧 CORRIGIDO: Usa o Python do ambiente virtual
        'manage.py',
        'dumpdata',
        tabela,
        '--indent', '2',
        '--output', caminho_completo
    ]
    
    print(f"\n📤 Exportando: {tabela}...")
    
    try:
        # Executar comando
        resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True,
            check=True
        )
        
        # Verificar se o arquivo foi criado
        if os.path.exists(caminho_completo):
            tamanho = os.path.getsize(caminho_completo)
            print(f"   ✅ Sucesso! Arquivo: {nome_arquivo} ({tamanho} bytes)")
            return True
        else:
            print(f"   ❌ Erro: Arquivo não foi criado")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Erro ao exportar: {e.stderr}")
        return False
    except Exception as e:
        print(f"   ❌ Erro inesperado: {str(e)}")
        return False


def fazer_backup_completo():
    """Executa backup de todas as tabelas configuradas"""
    print("=" * 60)
    print("🔄 INICIANDO BACKUP DE TABELAS")
    print("=" * 60)
    print(f"🐍 Python: {sys.executable}")
    print(f"📁 Destino: {BACKUP_DIR}")
    
    # Criar diretório
    criar_diretorio_backup()
    
    # Estatísticas
    total = len(TABELAS)
    sucesso = 0
    erros = 0
    
    # Exportar cada tabela
    for tabela in TABELAS:
        if exportar_tabela(tabela):
            sucesso += 1
        else:
            erros += 1
    
    # Resumo
    print("\n" + "=" * 60)
    print("📊 RESUMO DO BACKUP")
    print("=" * 60)
    print(f"Total de tabelas: {total}")
    print(f"✅ Sucesso: {sucesso}")
    print(f"❌ Erros: {erros}")
    print(f"📁 Local: {BACKUP_DIR}")
    print("=" * 60)


# ========================================
# EXECUÇÃO
# ========================================

if __name__ == '__main__':
    fazer_backup_completo()

    