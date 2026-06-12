## Saída do LOG de execução de testes


## apps.eventos.tests.test_admin.py

Creating test database for alias 'default' ('test_bdmetareciclagem')...

Found 29 test(s).
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
test_criterio_add_view (apps.eventos.tests.test_admin.CriterioAdminTest.test_criterio_add_view) ... ok
test_criterio_list_filter (apps.eventos.tests.test_admin.CriterioAdminTest.test_criterio_list_filter) ... ok
test_evento_add_view (apps.eventos.tests.test_admin.EventoAdminTest.test_evento_add_view) ... ok
test_evento_change_view (apps.eventos.tests.test_admin.EventoAdminTest.test_evento_change_view) ... ok
test_evento_criterios_inline (apps.eventos.tests.test_admin.EventoAdminTest.test_evento_criterios_inline) ... ok
test_evento_delete_view (apps.eventos.tests.test_admin.EventoAdminTest.test_evento_delete_view) ... ok
test_evento_individual_date_methods (apps.eventos.tests.test_admin.EventoAdminTest.test_evento_individual_date_methods) ... ok
test_evento_list_display (apps.eventos.tests.test_admin.EventoAdminTest.test_evento_list_display) ... ok
test_evento_list_view (apps.eventos.tests.test_admin.EventoAdminTest.test_evento_list_view) ... ok
test_evento_search (apps.eventos.tests.test_admin.EventoAdminTest.test_evento_search) ... ok
test_evento_turmas_inline (apps.eventos.tests.test_admin.EventoAdminTest.test_evento_turmas_inline) ... ok
test_horario_add_view (apps.eventos.tests.test_admin.HorarioAdminTest.test_horario_add_view) ... ok
test_horario_change_view (apps.eventos.tests.test_admin.HorarioAdminTest.test_horario_change_view) ... ok
test_horario_delete_view (apps.eventos.tests.test_admin.HorarioAdminTest.test_horario_delete_view) ... ok
test_horario_dia_semana_filter (apps.eventos.tests.test_admin.HorarioAdminTest.test_horario_dia_semana_filter) ... ok
test_horario_list_filter (apps.eventos.tests.test_admin.HorarioAdminTest.test_horario_list_filter) ... ok
test_horario_list_view (apps.eventos.tests.test_admin.HorarioAdminTest.test_horario_list_view) ... ok
test_horario_search (apps.eventos.tests.test_admin.HorarioAdminTest.test_horario_search) ... ok
test_status_add_view (apps.eventos.tests.test_admin.StatusAdminTest.test_status_add_view) ... ok
test_status_change_view (apps.eventos.tests.test_admin.StatusAdminTest.test_status_change_view) ... ok
test_status_delete_view (apps.eventos.tests.test_admin.StatusAdminTest.test_status_delete_view) ... ok
test_status_list_view (apps.eventos.tests.test_admin.StatusAdminTest.test_status_list_view) ... ok
test_status_search (apps.eventos.tests.test_admin.StatusAdminTest.test_status_search) ... ok
test_turma_add_view (apps.eventos.tests.test_admin.TurmaAdminTest.test_turma_add_view) ... ok
test_turma_change_view (apps.eventos.tests.test_admin.TurmaAdminTest.test_turma_change_view) ... ok
test_turma_delete_view (apps.eventos.tests.test_admin.TurmaAdminTest.test_turma_delete_view) ... ok
test_turma_list_display_evento (apps.eventos.tests.test_admin.TurmaAdminTest.test_turma_list_display_evento) ... ok
test_turma_list_view (apps.eventos.tests.test_admin.TurmaAdminTest.test_turma_list_view) ... ok
test_turma_search (apps.eventos.tests.test_admin.TurmaAdminTest.test_turma_search) ... ok

----------------------------------------------------------------------
Ran 29 tests in 3.675s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...

  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).





## apps.eventos.tests.test_models.py


(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.eventos.tests.test_models -v 2
Found 22 test(s).
Creating test database for alias 'default' ('test_bdmetareciclagem')...
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_create_criterio (apps.eventos.tests.test_models.CriterioModelTest.test_create_criterio) ... ok
test_criterio_categoria_choices (apps.eventos.tests.test_models.CriterioModelTest.test_criterio_categoria_choices) ... ok
test_criterio_codigo_unique (apps.eventos.tests.test_models.CriterioModelTest.test_criterio_codigo_unique) ... ok
test_criterio_pontos_non_negative (apps.eventos.tests.test_models.CriterioModelTest.test_criterio_pontos_non_negative) ... ok
test_criterio_str (apps.eventos.tests.test_models.CriterioModelTest.test_criterio_str) ... ok
test_create_evento (apps.eventos.tests.test_models.EventoModelTest.test_create_evento) ... ok
test_evento_data_inicio_evento_before_fim (apps.eventos.tests.test_models.EventoModelTest.test_evento_data_inicio_evento_before_fim) ... ok
test_evento_data_inicio_inscricao_before_fim (apps.eventos.tests.test_models.EventoModelTest.test_evento_data_inicio_inscricao_before_fim) ... ok
test_evento_datas_evento_validas (apps.eventos.tests.test_models.EventoModelTest.test_evento_datas_evento_validas) ... ok
test_evento_foreign_key_status (apps.eventos.tests.test_models.EventoModelTest.test_evento_foreign_key_status) ... ok
test_evento_str (apps.eventos.tests.test_models.EventoModelTest.test_evento_str) ... ok
test_evento_total_vagas_positive (apps.eventos.tests.test_models.EventoModelTest.test_evento_total_vagas_positive) ... ok
test_create_horario (apps.eventos.tests.test_models.HorarioModelTest.test_create_horario) ... ok
test_horario_foreign_key_turma (apps.eventos.tests.test_models.HorarioModelTest.test_horario_foreign_key_turma) ... ok
test_create_status (apps.eventos.tests.test_models.StatusModelTest.test_create_status) ... ok
test_status_cor_valid_hex (apps.eventos.tests.test_models.StatusModelTest.test_status_cor_valid_hex) ... ok
test_status_ordem_unique (apps.eventos.tests.test_models.StatusModelTest.test_status_ordem_unique) ... ok
test_status_str (apps.eventos.tests.test_models.StatusModelTest.test_status_str) ... ok
test_create_turma (apps.eventos.tests.test_models.TurmaModelTest.test_create_turma) ... ok
test_turma_capacidade_positive (apps.eventos.tests.test_models.TurmaModelTest.test_turma_capacidade_positive) ... ok
test_turma_foreign_key_evento (apps.eventos.tests.test_models.TurmaModelTest.test_turma_foreign_key_evento) ... ok
test_turma_str (apps.eventos.tests.test_models.TurmaModelTest.test_turma_str) ... ok

----------------------------------------------------------------------
Ran 22 tests in 0.323s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...


## apps.selecao.tests.test_services.py em 10/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> pytest apps/selecao/tests/test_services.py -v
=========================================================================== test session starts ===========================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 16 items                                                                                                                                                         

apps/selecao/tests/test_services.py::TestClassificadorServicePontuacao::test_calcular_pontuacao_inscricao_com_criterios PASSED                                       [  6%]
apps/selecao/tests/test_services.py::TestClassificadorServicePontuacao::test_calcular_pontuacao_inscricao_zero PASSED                                                [ 12%]
apps/selecao/tests/test_services.py::TestClassificadorServicePontuacao::test_calcular_pontuacao_multiplos_criterios PASSED                                           [ 18%]
apps/selecao/tests/test_services.py::TestClassificadorServicePontuacao::test_classificar_sem_eventocriterio_vinculado PASSED                                         [ 25%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_atribui_posicoes PASSED                                          [ 31%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_classifica_dentro_vagas PASSED                                   [ 37%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_lista_espera PASSED                                              [ 43%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_atualiza_status_inscricao PASSED                                 [ 50%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_com_criterios PASSED                                             [ 56%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_zero_inscricoes PASSED                                           [ 62%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_chamada_repetida PASSED                                          [ 68%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_exatamente_1_vaga PASSED                                         [ 75%]
apps/selecao/tests/test_services.py::TestClassificadorServiceDesempate::test_desempate_por_data_inscricao_igual_pontuacao PASSED                                     [ 81%]
apps/selecao/tests/test_services.py::TestClassificadorServiceDesempate::test_desempate_com_lista_espera PASSED                                                       [ 87%]
apps/selecao/tests/test_services.py::TestClassificadorServiceDesempate::test_desempate_misto_pontuacoes_diferentes_e_iguais PASSED                                   [ 93%]
apps/selecao/tests/test_services.py::TestClassificadorServiceProcessamento::test_processar_inscricao_cria_classificacao PASSED                                       [100%]

---------- coverage: platform win32, python 3.13.2-final-0 -----------
Name                                                                    Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------------------
apps\__init__.py                                                            0      0   100%
apps\academico\__init__.py                                                  0      0   100%
apps\academico\admin.py                                                   320    248    22%   64-70, 124, 129, 200, 205, 211-216, 225-266, 270-276, 284-440, 450-613, 623-653, 663-671, 678, 681
apps\academico\apps.py                                                      5      0   100%
apps\academico\certificado.py                                             136    136     0%   9-254
apps\academico\models.py                                                  110     51    54%   45, 122, 128-154, 167-176, 191-214, 282-283, 300-316, 330-342
apps\academico\services.py                                                136    136     0%   8-402
apps\academico\urls.py                                                      5      5     0%   8-19
apps\academico\views.py                                                    63     63     0%   8-124
apps\accounts\__init__.py                                                   0      0   100%
apps\accounts\admin.py                                                     52     19    63%   40-44, 48-63, 149-169
apps\accounts\apps.py                                                       5      0   100%
apps\accounts\forms.py                                                      5      5     0%   8-27
apps\accounts\middleware.py                                                20     20     0%   17-83
apps\accounts\models.py                                                    22      4    82%   103-106
apps\accounts\urls.py                                                       5      5     0%   9-17
apps\accounts\views.py                                                     47     47     0%   16-114
apps\accounts\views_exclusao.py                                            77     77     0%   9-125
apps\dashboard\__init__.py                                                  0      0   100%
apps\dashboard\admin.py                                                     0      0   100%
apps\dashboard\apps.py                                                      4      0   100%
apps\dashboard\models.py                                                    1      0   100%
apps\dashboard\utils_pdf.py                                               373    373     0%   9-751
apps\dashboard\views.py                                                   216    216     0%   13-690
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212    117    45%   61-67, 95, 110-114, 118-119, 122-124, 173-181, 187-206, 218-223, 229-234, 240-245, 251-256, 269-358, 371-415, 430-519, 537
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51     51     0%   8-114
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122     29    76%   28, 104-106, 127, 130-132, 135-137, 140-142, 145-147, 150-152, 155-160, 201, 206, 247, 280
apps\eventos\views.py                                                       1      1     0%   1
apps\interessados\__init__.py                                               0      0   100%
apps\interessados\admin.py                                                218    120    45%   178-183, 188, 193-194, 201-207, 216-222, 231-243, 248-260, 265-269, 280-282, 296-316, 329-330, 337-338, 347-431, 475, 480-481, 485-500, 509, 514, 523-527, 535-538, 546-552, 564, 567, 570
apps\interessados\apps.py                                                   5      0   100%
apps\interessados\authentication.py                                        25     25     0%   9-73
apps\interessados\forms.py                                                157    157     0%   20-453
apps\interessados\management\__init__.py                                    0      0   100%
apps\interessados\management\commands\__init__.py                           0      0   100%
apps\interessados\management\commands\criptografar_cpfs.py                 22     22     0%   11-47
apps\interessados\management\commands\limpar_tokens.py                     59     59     0%   13-155
apps\interessados\management\commands\popular_cpf_hash.py                  22     22     0%   9-40
apps\interessados\models.py                                               139     17    88%   29, 41, 135, 138, 141, 144, 147, 151, 155, 158, 162, 166, 172, 188, 191-192, 260
apps\interessados\urls.py                                                   5      5     0%   11-17
apps\interessados\utils.py                                                 14     14     0%   10-38
apps\interessados\views.py                                                202    202     0%   24-519
apps\interessados\views_exclusao.py                                        29     29     0%   8-76
apps\portal\__init__.py                                                     1      0   100%
apps\portal\admin.py                                                        1      0   100%
apps\portal\apps.py                                                         5      0   100%
apps\portal\forms.py                                                       34     34     0%   14-104
apps\portal\models.py                                                       1      0   100%
apps\portal\urls.py                                                         4      4     0%   8-13
apps\portal\views.py                                                       99     99     0%   13-247
apps\scripts_admin\__init__.py                                              0      0   100%
apps\scripts_admin\management\__init__.py                                   0      0   100%
apps\scripts_admin\management\commands\__init__.py                          0      0   100%
apps\scripts_admin\management\commands\classificar_evento.py              133    133     0%   8-291
apps\scripts_admin\management\commands\configurar_criterios_evento.py      57     57     0%   5-91
apps\scripts_admin\management\commands\popular_criterios.py                21     21     0%   4-117
apps\scripts_admin\management\commands\popular_dados_iniciais.py           66     66     0%   8-234
apps\selecao\__init__.py                                                    0      0   100%
apps\selecao\admin.py                                                     275    163    41%   66-72, 87, 110-115, 152, 223, 233, 240-241, 247, 254-255, 266-275, 293-456, 466-503, 507-544, 552, 558, 564, 570, 580, 586, 592, 598, 608, 612, 616, 661, 667, 673, 677
apps\selecao\apps.py                                                        5      0   100%
apps\selecao\management\__init__.py                                         0      0   100%
apps\selecao\management\commands\__init__.py                                0      0   100%
apps\selecao\models.py                                                     71      8    89%   38, 74, 129, 133-134, 137, 155, 188
apps\selecao\reports.py                                                   301    270    10%   27-31, 35-115, 126-132, 140-146, 151-163, 179-286, 302-420, 440-565, 580-711
apps\selecao\services.py                                                  125     26    79%   82-85, 89-92, 102, 106, 110, 114, 383-392, 414-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4195   3262    22%
Coverage HTML written to dir htmlcov


=========================================================================== 16 passed in 17.49s ===================================================================




## apps.selecao.tests.test_models.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> pytest apps/selecao/tests/test_models.py -v
========================================================== test session starts ===========================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 14 items                                                                                                                        

apps/selecao/tests/test_models.py::TestStatusInscricaoModel::test_create_status_inscricao PASSED                                    [  7%]
apps/selecao/tests/test_models.py::TestStatusInscricaoModel::test_status_inscricao_str PASSED                                       [ 14%]
apps/selecao/tests/test_models.py::TestStatusInscricaoModel::test_status_inscricao_unique_name PASSED                               [ 21%]
apps/selecao/tests/test_models.py::TestInscricaoModel::test_create_inscricao PASSED                                                 [ 28%]
apps/selecao/tests/test_models.py::TestInscricaoModel::test_inscricao_str PASSED                                                    [ 35%]
apps/selecao/tests/test_models.py::TestInscricaoModel::test_inscricao_unique_together PASSED                                        [ 42%]
apps/selecao/tests/test_models.py::TestInscricaoModel::test_inscricao_relacionamentos PASSED                                        [ 50%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_create_classificacao PASSED                                         [ 57%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_classificacao_str PASSED                                            [ 64%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_classificacao_posicao_null_default PASSED                           [ 71%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_classificacao_unique_inscricao PASSED                               [ 78%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_pontuacao_total_validacao_range PASSED                              [ 85%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_flags_classificacao_mutuamente_exclusivas PASSED                    [ 92%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_desempate_por_data_inscricao PASSED                                 [100%]

---------- coverage: platform win32, python 3.13.2-final-0 -----------
Name                                                                    Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------------------
apps\__init__.py                                                            0      0   100%
apps\academico\__init__.py                                                  0      0   100%
apps\academico\admin.py                                                   316    246    22%   64-70, 124, 129, 200, 205, 211-216, 225-266, 270-276, 284-440, 450-613, 623-653, 663-671
apps\academico\apps.py                                                      5      0   100%
apps\academico\certificado.py                                             136    136     0%   9-254
apps\academico\models.py                                                  110     51    54%   45, 122, 128-154, 167-176, 191-214, 282-283, 300-316, 330-342
apps\academico\services.py                                                134    134     0%   8-396
apps\academico\urls.py                                                      5      5     0%   8-19
apps\academico\views.py                                                    63     63     0%   8-124
apps\accounts\__init__.py                                                   0      0   100%
apps\accounts\admin.py                                                     52     19    63%   40-44, 48-63, 149-169
apps\accounts\apps.py                                                       5      0   100%
apps\accounts\forms.py                                                      5      5     0%   8-27
apps\accounts\middleware.py                                                20     20     0%   17-83
apps\accounts\models.py                                                    22      4    82%   103-106
apps\accounts\urls.py                                                       5      5     0%   9-17
apps\accounts\views.py                                                     47     47     0%   16-114
apps\accounts\views_exclusao.py                                            77     77     0%   9-125
apps\dashboard\__init__.py                                                  0      0   100%
apps\dashboard\admin.py                                                     0      0   100%
apps\dashboard\apps.py                                                      4      0   100%
apps\dashboard\models.py                                                    1      0   100%
apps\dashboard\utils_pdf.py                                               373    373     0%   9-751
apps\dashboard\views.py                                                   216    216     0%   13-690
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212    117    45%   61-67, 95, 110-114, 118-119, 122-124, 173-181, 187-206, 218-223, 229-234, 240-245, 251-256, 269-358, 371-415, 430-519, 537
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51     51     0%   8-114
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122     29    76%   28, 104-106, 127, 130-132, 135-137, 140-142, 145-147, 150-152, 155-160, 201, 206, 247, 280
apps\eventos\views.py                                                       1      1     0%   1
apps\interessados\__init__.py                                               0      0   100%
apps\interessados\admin.py                                                218    120    45%   178-183, 188, 193-194, 201-207, 216-222, 231-243, 248-260, 265-269, 280-282, 296-316, 329-330, 337-338, 347-431, 475, 480-481, 485-500, 509, 514, 523-527, 535-538, 546-552, 564, 567, 570
apps\interessados\apps.py                                                   5      0   100%
apps\interessados\authentication.py                                        25     25     0%   9-73
apps\interessados\forms.py                                                157    157     0%   20-453
apps\interessados\management\__init__.py                                    0      0   100%
apps\interessados\management\commands\__init__.py                           0      0   100%
apps\interessados\management\commands\criptografar_cpfs.py                 22     22     0%   11-47
apps\interessados\management\commands\limpar_tokens.py                     59     59     0%   13-155
apps\interessados\management\commands\popular_cpf_hash.py                  22     22     0%   9-40
apps\interessados\models.py                                               139     17    88%   29, 41, 135, 138, 141, 144, 147, 151, 155, 158, 162, 166, 172, 188, 191-192, 260
apps\interessados\urls.py                                                   5      5     0%   11-17
apps\interessados\utils.py                                                 14     14     0%   10-38
apps\interessados\views.py                                                202    202     0%   24-519
apps\interessados\views_exclusao.py                                        29     29     0%   8-76
apps\portal\__init__.py                                                     1      0   100%
apps\portal\admin.py                                                        1      0   100%
apps\portal\apps.py                                                         5      0   100%
apps\portal\forms.py                                                       34     34     0%   14-104
apps\portal\models.py                                                       1      0   100%
apps\portal\urls.py                                                         4      4     0%   8-13
apps\portal\views.py                                                       99     99     0%   13-247
apps\scripts_admin\__init__.py                                              0      0   100%
apps\scripts_admin\management\__init__.py                                   0      0   100%
apps\scripts_admin\management\commands\__init__.py                          0      0   100%
apps\scripts_admin\management\commands\classificar_evento.py              133    133     0%   8-291
apps\scripts_admin\management\commands\configurar_criterios_evento.py      57     57     0%   5-91
apps\scripts_admin\management\commands\popular_criterios.py                21     21     0%   4-117
apps\scripts_admin\management\commands\popular_dados_iniciais.py           66     66     0%   8-234
apps\selecao\__init__.py                                                    0      0   100%
apps\selecao\admin.py                                                     275    163    41%   66-72, 87, 110-115, 152, 223, 233, 240-241, 247, 254-255, 266-275, 293-456, 466-503, 507-544, 552, 558, 564, 570, 580, 586, 592, 598, 608, 612, 616, 661, 667, 673, 677
apps\selecao\apps.py                                                        5      0   100%
apps\selecao\management\__init__.py                                         0      0   100%
apps\selecao\management\commands\__init__.py                                0      0   100%
apps\selecao\models.py                                                     71      1    99%   188
apps\selecao\reports.py                                                   301    270    10%   27-31, 35-115, 126-132, 140-146, 151-163, 179-286, 302-420, 440-565, 580-711
apps\selecao\services.py                                                  125    125     0%   28-443
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4189   3350    20%
Coverage HTML written to dir htmlcov


=========================================================== 14 passed in 9.37s ===========================================================




## apps.selecao.tests.test_admin.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> pytest apps/selecao/tests/test_admin.py -v   
========================================================== test session starts ===========================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 12 items                                                                                                                        

apps/selecao/tests/test_admin.py::TestMatricularAlunosActionCapacity::test_matricular_alunos_capacidade_ultrapassada PASSED         [  8%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionCapacity::test_matricular_alunos_capacidade_exata PASSED                [ 16%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionValidation::test_validacao_evento_unico PASSED                          [ 25%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionValidation::test_validacao_turma_inexistente_para_evento PASSED         [ 33%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionValidation::test_protecao_duplicidade_matricula PASSED                  [ 41%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionValidation::test_validacao_turma_nao_pertence_ao_evento PASSED          [ 50%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionSuccess::test_sucesso_matricula_dentro_capacidade PASSED                [ 58%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionSuccess::test_nenhuma_classificacao_selecionada PASSED                  [ 66%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionErrorHandling::test_transacao_atomica_rollback_on_matricula_save_error PASSED [ 75%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionErrorHandling::test_status_ativa_nao_encontrado PASSED                  [ 83%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionErrorHandling::test_status_confirmada_nao_encontrado PASSED             [ 91%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionErrorHandling::test_classificacoes_sem_evento_associado PASSED          [100%]

---------- coverage: platform win32, python 3.13.2-final-0 -----------
Name                                                                    Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------------------
apps\__init__.py                                                            0      0   100%
apps\academico\__init__.py                                                  0      0   100%
apps\academico\admin.py                                                   316    246    22%   64-70, 124, 129, 200, 205, 211-216, 225-266, 270-276, 284-440, 450-613, 623-653, 663-671
apps\academico\apps.py                                                      5      0   100%
apps\academico\certificado.py                                             136    118    13%   24-37, 43-67, 72-79, 83-104, 108-116, 120-163, 167-208, 212-254
apps\academico\models.py                                                  110     25    77%   45, 122, 133, 142, 154, 168, 204-206, 282-283, 300-316, 339-342
apps\academico\services.py                                                134    134     0%   8-396
apps\academico\urls.py                                                      5      0   100%
apps\academico\views.py                                                    63     45    29%   31-52, 61-77, 87-124
apps\accounts\__init__.py                                                   0      0   100%
apps\accounts\admin.py                                                     52     16    69%   48-63, 149-169
apps\accounts\apps.py                                                       5      0   100%
apps\accounts\forms.py                                                      5      5     0%   8-27
apps\accounts\middleware.py                                                20     20     0%   17-83
apps\accounts\models.py                                                    22      4    82%   103-106
apps\accounts\urls.py                                                       5      0   100%
apps\accounts\views.py                                                     47     38    19%   26-52, 60-62, 83-114
apps\accounts\views_exclusao.py                                            77     66    14%   19, 25-33, 43-83, 94-125
apps\dashboard\__init__.py                                                  0      0   100%
apps\dashboard\admin.py                                                     0      0   100%
apps\dashboard\apps.py                                                      4      0   100%
apps\dashboard\models.py                                                    1      0   100%
apps\dashboard\utils_pdf.py                                               373    373     0%   9-751
apps\dashboard\views.py                                                   216    193    11%   23-66, 72-130, 136-319, 325-381, 386-407, 417-552, 558-613, 619-651, 657-690
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212    117    45%   61-67, 95, 110-114, 118-119, 122-124, 173-181, 187-206, 218-223, 229-234, 240-245, 251-256, 269-358, 371-415, 430-519, 537
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51     23    55%   25, 39, 67-81, 87-95, 101-112
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122     28    77%   28, 104-106, 127, 130-132, 135-137, 140-142, 145-147, 150-152, 155-160, 201, 206, 280
apps\eventos\views.py                                                       1      1     0%   1
apps\interessados\__init__.py                                               0      0   100%
apps\interessados\admin.py                                                218    120    45%   178-183, 188, 193-194, 201-207, 216-222, 231-243, 248-260, 265-269, 280-282, 296-316, 329-330, 337-338, 347-431, 475, 480-481, 485-500, 509, 514, 523-527, 535-538, 546-552, 564, 567, 570
apps\interessados\apps.py                                                   5      0   100%
apps\interessados\authentication.py                                        25     25     0%   9-73
apps\interessados\forms.py                                                157    106    32%   167-171, 179-213, 220-230, 234-235, 239-243, 247, 251, 255, 259, 263, 267, 271, 275-280, 287-302, 335-358, 392-396, 401-402, 406-410, 414, 418, 422, 426, 430, 434, 438, 445-453
apps\interessados\management\__init__.py                                    0      0   100%
apps\interessados\management\commands\__init__.py                           0      0   100%
apps\interessados\management\commands\criptografar_cpfs.py                 22     22     0%   11-47
apps\interessados\management\commands\limpar_tokens.py                     59     59     0%   13-155
apps\interessados\management\commands\popular_cpf_hash.py                  22     22     0%   9-40
apps\interessados\models.py                                               139     18    87%   22, 29, 41, 135, 138, 141, 144, 147, 151, 155, 158, 162, 166, 172, 188, 191-192, 260
apps\interessados\urls.py                                                   5      0   100%
apps\interessados\utils.py                                                 14     14     0%   10-38
apps\interessados\views.py                                                202    167    17%   49-67, 81-107, 113-115, 129-181, 194-216, 232-250, 266-323, 342-414, 422, 430-472, 477, 482, 496-519
apps\interessados\views_exclusao.py                                        29     20    31%   22-67, 76
apps\portal\__init__.py                                                     1      0   100%
apps\portal\admin.py                                                        1      0   100%
apps\portal\apps.py                                                         5      0   100%
apps\portal\forms.py                                                       34     24    29%   45-51, 55-76, 98-104
apps\portal\models.py                                                       1      0   100%
apps\portal\urls.py                                                         4      0   100%
apps\portal\views.py                                                       99     79    20%   30-39, 45-74, 79-82, 87-116, 122-163, 168-189, 196-220, 225-242, 247
apps\scripts_admin\__init__.py                                              0      0   100%
apps\scripts_admin\management\__init__.py                                   0      0   100%
apps\scripts_admin\management\commands\__init__.py                          0      0   100%
apps\scripts_admin\management\commands\classificar_evento.py              133    133     0%   8-291
apps\scripts_admin\management\commands\configurar_criterios_evento.py      57     57     0%   5-91
apps\scripts_admin\management\commands\popular_criterios.py                21     21     0%   4-117
apps\scripts_admin\management\commands\popular_dados_iniciais.py           66     66     0%   8-234
apps\selecao\__init__.py                                                    0      0   100%
apps\selecao\admin.py                                                     275     93    66%   71-72, 87, 110-115, 152, 223, 233, 240-241, 247, 254-255, 266-275, 306-307, 338-343, 445, 466-503, 507-544, 552, 558, 564, 570, 580, 586, 592, 598, 608, 612, 616, 661, 667, 673, 677
apps\selecao\apps.py                                                        5      0   100%
apps\selecao\management\__init__.py                                         0      0   100%
apps\selecao\management\commands\__init__.py                                0      0   100%
apps\selecao\models.py                                                     71      8    89%   38, 74, 129, 133-134, 137, 155, 188
apps\selecao\reports.py                                                   301    270    10%   27-31, 35-115, 126-132, 140-146, 151-163, 179-286, 302-420, 440-565, 580-711
apps\selecao\services.py                                                  125    125     0%   28-443
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4189   3007    28%
Coverage HTML written to dir htmlcov


========================================================== 12 passed in 17.28s ===========================================================



## apps.selecao.tests.test_validators.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> pytest apps/selecao/tests/test_validators.py -v
========================================================== test session starts ===========================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 13 items                                                                                                                        

apps/selecao/tests/test_validators.py::TestValidarEvento::test_evento_sem_vagas_falha PASSED                                        [  7%]
apps/selecao/tests/test_validators.py::TestValidarEvento::test_evento_sem_inscricoes_falha PASSED                                   [ 15%]
apps/selecao/tests/test_validators.py::TestValidarEvento::test_evento_datas_invalidas_falha PASSED                                  [ 23%]
apps/selecao/tests/test_validators.py::TestValidarEvento::test_evento_sem_criterios_falha PASSED                                    [ 30%]
apps/selecao/tests/test_validators.py::TestValidarEvento::test_evento_com_criterios_passa PASSED                                    [ 38%]
apps/selecao/tests/test_validators.py::TestValidarInteressado::test_interessado_valido_passa PASSED                                 [ 46%]
apps/selecao/tests/test_validators.py::TestValidarInteressado::test_interessado_sem_nome_falha PASSED                               [ 53%]
apps/selecao/tests/test_validators.py::TestValidarInteressado::test_interessado_data_nascimento_futura_falha PASSED                 [ 61%]
apps/selecao/tests/test_validators.py::TestValidarInteressado::test_interessado_sem_sexo_gera_aviso PASSED                          [ 69%]
apps/selecao/tests/test_validators.py::TestValidarInscricao::test_inscricao_valida_passa PASSED                                     [ 76%]
apps/selecao/tests/test_validators.py::TestValidarInscricao::test_inscricao_sem_evento_falha PASSED                                 [ 84%]
apps/selecao/tests/test_validators.py::TestValidarInscricao::test_inscricao_sem_interessado_falha PASSED                            [ 92%]
apps/selecao/tests/test_validators.py::TestValidarInscricao::test_inscricao_com_data_futura_falha PASSED                            [100%]

---------- coverage: platform win32, python 3.13.2-final-0 -----------
Name                                                                    Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------------------
apps\__init__.py                                                            0      0   100%
apps\academico\__init__.py                                                  0      0   100%
apps\academico\admin.py                                                   316    246    22%   64-70, 124, 129, 200, 205, 211-216, 225-266, 270-276, 284-440, 450-613, 623-653, 663-671
apps\academico\apps.py                                                      5      0   100%
apps\academico\certificado.py                                             136    136     0%   9-254
apps\academico\models.py                                                  110     51    54%   45, 122, 128-154, 167-176, 191-214, 282-283, 300-316, 330-342
apps\academico\services.py                                                134    134     0%   8-396
apps\academico\urls.py                                                      5      5     0%   8-19
apps\academico\views.py                                                    63     63     0%   8-124
apps\accounts\__init__.py                                                   0      0   100%
apps\accounts\admin.py                                                     52     19    63%   40-44, 48-63, 149-169
apps\accounts\apps.py                                                       5      0   100%
apps\accounts\forms.py                                                      5      5     0%   8-27
apps\accounts\middleware.py                                                20     20     0%   17-83
apps\accounts\models.py                                                    22      4    82%   103-106
apps\accounts\urls.py                                                       5      5     0%   9-17
apps\accounts\views.py                                                     47     47     0%   16-114
apps\accounts\views_exclusao.py                                            77     77     0%   9-125
apps\dashboard\__init__.py                                                  0      0   100%
apps\dashboard\admin.py                                                     0      0   100%
apps\dashboard\apps.py                                                      4      0   100%
apps\dashboard\models.py                                                    1      0   100%
apps\dashboard\utils_pdf.py                                               373    373     0%   9-751
apps\dashboard\views.py                                                   216    216     0%   13-690
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212    117    45%   61-67, 95, 110-114, 118-119, 122-124, 173-181, 187-206, 218-223, 229-234, 240-245, 251-256, 269-358, 371-415, 430-519, 537
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51     51     0%   8-114
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122     29    76%   28, 104-106, 127, 130-132, 135-137, 140-142, 145-147, 150-152, 155-160, 201, 206, 247, 280
apps\eventos\views.py                                                       1      1     0%   1
apps\interessados\__init__.py                                               0      0   100%
apps\interessados\admin.py                                                218    120    45%   178-183, 188, 193-194, 201-207, 216-222, 231-243, 248-260, 265-269, 280-282, 296-316, 329-330, 337-338, 347-431, 475, 480-481, 485-500, 509, 514, 523-527, 535-538, 546-552, 564, 567, 570
apps\interessados\apps.py                                                   5      0   100%
apps\interessados\authentication.py                                        25     25     0%   9-73
apps\interessados\forms.py                                                157    157     0%   20-453
apps\interessados\management\__init__.py                                    0      0   100%
apps\interessados\management\commands\__init__.py                           0      0   100%
apps\interessados\management\commands\criptografar_cpfs.py                 22     22     0%   11-47
apps\interessados\management\commands\limpar_tokens.py                     59     59     0%   13-155
apps\interessados\management\commands\popular_cpf_hash.py                  22     22     0%   9-40
apps\interessados\models.py                                               139     17    88%   29, 41, 135, 138, 141, 144, 147, 151, 155, 158, 162, 166, 172, 188, 191-192, 260
apps\interessados\urls.py                                                   5      5     0%   11-17
apps\interessados\utils.py                                                 14     14     0%   10-38
apps\interessados\views.py                                                202    202     0%   24-519
apps\interessados\views_exclusao.py                                        29     29     0%   8-76
apps\portal\__init__.py                                                     1      0   100%
apps\portal\admin.py                                                        1      0   100%
apps\portal\apps.py                                                         5      0   100%
apps\portal\forms.py                                                       34     34     0%   14-104
apps\portal\models.py                                                       1      0   100%
apps\portal\urls.py                                                         4      4     0%   8-13
apps\portal\views.py                                                       99     99     0%   13-247
apps\scripts_admin\__init__.py                                              0      0   100%
apps\scripts_admin\management\__init__.py                                   0      0   100%
apps\scripts_admin\management\commands\__init__.py                          0      0   100%
apps\scripts_admin\management\commands\classificar_evento.py              133    133     0%   8-291
apps\scripts_admin\management\commands\configurar_criterios_evento.py      57     57     0%   5-91
apps\scripts_admin\management\commands\popular_criterios.py                21     21     0%   4-117
apps\scripts_admin\management\commands\popular_dados_iniciais.py           66     66     0%   8-234
apps\selecao\__init__.py                                                    0      0   100%
apps\selecao\admin.py                                                     275    163    41%   66-72, 87, 110-115, 152, 223, 233, 240-241, 247, 254-255, 266-275, 293-456, 466-503, 507-544, 552, 558, 564, 570, 580, 586, 592, 598, 608, 612, 616, 661, 667, 673, 677
apps\selecao\apps.py                                                        5      0   100%
apps\selecao\management\__init__.py                                         0      0   100%
apps\selecao\management\commands\__init__.py                                0      0   100%
apps\selecao\models.py                                                     71     15    79%   38, 74, 124-137, 145-146, 155, 188
apps\selecao\reports.py                                                   301    270    10%   27-31, 35-115, 126-132, 140-146, 151-163, 179-286, 302-420, 440-565, 580-711
apps\selecao\services.py                                                  125    125     0%   28-443
apps\selecao\validators.py                                                105     35    67%   38-39, 47, 74, 101, 105, 116, 123, 126, 130, 149-175, 193-194, 199, 204, 213-215, 222-223
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4189   3294    21%
Coverage HTML written to dir htmlcov


=========================================================== 13 passed in 7.49s ===========================================================





## apps.accounts.test.test_models.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.accounts.tests.test_models -v 2
Found 10 test(s).
Creating test database for alias 'default' ('test_bdmetareciclagem')...
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_cpf_unico (apps.accounts.tests.test_models.TestUsuarioModel.test_cpf_unico)
Verifica se CPF duplicado falha. ... ok
test_criar_superuser_is_staff (apps.accounts.tests.test_models.TestUsuarioModel.test_criar_superuser_is_staff) ... ok
test_criar_superuser_is_superuser (apps.accounts.tests.test_models.TestUsuarioModel.test_criar_superuser_is_superuser) ... ok
test_criar_usuario_com_cpf_invalido (apps.accounts.tests.test_models.TestUsuarioModel.test_criar_usuario_com_cpf_invalido)
Verifica se a criação falha com CPF que não tem 11 dígitos. ... ok
test_criar_usuario_com_cpf_valido (apps.accounts.tests.test_models.TestUsuarioModel.test_criar_usuario_com_cpf_valido)
Verifica se um usuário pode ser criado com um CPF válido de 11 dígitos. ... ok
test_criar_usuario_sem_password_falha (apps.accounts.tests.test_models.TestUsuarioModel.test_criar_usuario_sem_password_falha) ... ok
test_criar_usuario_sem_username_falha (apps.accounts.tests.test_models.TestUsuarioModel.test_criar_usuario_sem_username_falha) ... ok
test_usuario_nao_staff_nao_pode_login_staff (apps.accounts.tests.test_models.TestUsuarioModel.test_usuario_nao_staff_nao_pode_login_staff)
Verifica se um usuário não staff é criado com is_staff=False. ... ok
test_usuario_staff_pode_login (apps.accounts.tests.test_models.TestUsuarioModel.test_usuario_staff_pode_login)
Verifica se um usuário staff é criado com is_staff=True. ... ok
test_usuario_str_retorna_username (apps.accounts.tests.test_models.TestUsuarioModel.test_usuario_str_retorna_username) ... ok

----------------------------------------------------------------------
Ran 10 tests in 4.498s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...


## apps.accounts.test.test_views.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.accounts.tests.test_views -v 2
Found 10 test(s).
Creating test database for alias 'default' ('test_bdmetareciclagem')...
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_login_staff_form_tem_csrf (apps.accounts.tests.test_views.AccountsViewsTest.test_login_staff_form_tem_csrf) ... ok
test_login_staff_get (apps.accounts.tests.test_views.AccountsViewsTest.test_login_staff_get)
Verifica se a página de login é acessível via GET. ... ok
test_login_staff_inativo_falha (apps.accounts.tests.test_views.AccountsViewsTest.test_login_staff_inativo_falha) ... AXES: New login failure by {username: "********************", ip_address: "********************", user_agent: "<unknown>", path_info: "/staff/login/"}. Created new record in the database.
ok
test_login_staff_invalido (apps.accounts.tests.test_views.AccountsViewsTest.test_login_staff_invalido)
Verifica se credenciais inválidas falham. ... AXES: New login failure by {username: "********************", ip_address: "********************", user_agent: "<unknown>", path_info: "/staff/login/"}. Created new record in the database.
ok
test_login_staff_nao_staff (apps.accounts.tests.test_views.AccountsViewsTest.test_login_staff_nao_staff)
Verifica se usuário não-staff não consegue fazer login. ... ok
test_login_staff_valido (apps.accounts.tests.test_views.AccountsViewsTest.test_login_staff_valido)
Verifica se credenciais válidas realizam login e redirecionam. ... ok
test_logout_staff (apps.accounts.tests.test_views.AccountsViewsTest.test_logout_staff)
Verifica se logout funciona corretamente. ... ok
test_logout_staff_get_desloga (apps.accounts.tests.test_views.AccountsViewsTest.test_logout_staff_get_desloga) ... ok
test_nao_staff_redirecionado_ao_acessar_pagina_staff (apps.accounts.tests.test_views.AccountsViewsTest.test_nao_staff_redirecionado_ao_acessar_pagina_staff) ... ok
test_staff_acessa_pagina_restrita_apos_login (apps.accounts.tests.test_views.AccountsViewsTest.test_staff_acessa_pagina_restrita_apos_login) ... ok

----------------------------------------------------------------------
Ran 10 tests in 12.662s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...


## apps.accounts.test.test_views_exclusao.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.accounts.tests.test_views_exclusao -v 2
Found 15 test(s).
Creating test database for alias 'default' ('test_bdmetareciclagem')...
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_anonimizar_interessado_limpa_campos (apps.accounts.tests.test_views_exclusao.TestAnonimizarInteressado.test_anonimizar_interessado_limpa_campos) ... ok
test_anonimizar_interessado_mantem_registro (apps.accounts.tests.test_views_exclusao.TestAnonimizarInteressado.test_anonimizar_interessado_mantem_registro) ... ok
test_detalhe_solicitacao_404 (apps.accounts.tests.test_views_exclusao.TestDetalheSolicitacaoView.test_detalhe_solicitacao_404) ... ok
test_detalhe_solicitacao_acao_invalida (apps.accounts.tests.test_views_exclusao.TestDetalheSolicitacaoView.test_detalhe_solicitacao_acao_invalida) ... ok
test_detalhe_solicitacao_aprovar (apps.accounts.tests.test_views_exclusao.TestDetalheSolicitacaoView.test_detalhe_solicitacao_aprovar) ... ok
test_detalhe_solicitacao_recusar (apps.accounts.tests.test_views_exclusao.TestDetalheSolicitacaoView.test_detalhe_solicitacao_recusar) ... ok
test_detalhe_solicitacao_sem_login_redirect (apps.accounts.tests.test_views_exclusao.TestDetalheSolicitacaoView.test_detalhe_solicitacao_sem_login_redirect) ... ok
test_detalhe_solicitacao_sem_parecer (apps.accounts.tests.test_views_exclusao.TestDetalheSolicitacaoView.test_detalhe_solicitacao_sem_parecer) ... ok
test_detalhe_solicitacao_status_200 (apps.accounts.tests.test_views_exclusao.TestDetalheSolicitacaoView.test_detalhe_solicitacao_status_200) ... ok
test_listar_solicitacoes_contexto_tem_aprovadas (apps.accounts.tests.test_views_exclusao.TestListarSolicitacoesView.test_listar_solicitacoes_contexto_tem_aprovadas) ... ok
test_listar_solicitacoes_contexto_tem_pendentes (apps.accounts.tests.test_views_exclusao.TestListarSolicitacoesView.test_listar_solicitacoes_contexto_tem_pendentes) ... ok
test_listar_solicitacoes_contexto_tem_recusadas (apps.accounts.tests.test_views_exclusao.TestListarSolicitacoesView.test_listar_solicitacoes_contexto_tem_recusadas) ... ok
test_listar_solicitacoes_nao_staff_redirect (apps.accounts.tests.test_views_exclusao.TestListarSolicitacoesView.test_listar_solicitacoes_nao_staff_redirect) ... ok
test_listar_solicitacoes_sem_login_redirect (apps.accounts.tests.test_views_exclusao.TestListarSolicitacoesView.test_listar_solicitacoes_sem_login_redirect) ... ok
test_listar_solicitacoes_status_200 (apps.accounts.tests.test_views_exclusao.TestListarSolicitacoesView.test_listar_solicitacoes_status_200) ... ok

----------------------------------------------------------------------
Ran 15 tests in 23.915s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...



## apps.accounts.test.test_admin.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.accounts.tests.test_admin -v 2
Found 11 test(s).
Creating test database for alias 'default' ('test_bdmetareciclagem')...
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_admin_index_sem_login_redirect (apps.accounts.tests.test_admin.TestCustomAdminSite.test_admin_index_sem_login_redirect) ... ok
test_admin_index_status_200 (apps.accounts.tests.test_admin.TestCustomAdminSite.test_admin_index_status_200) ... ok
test_dashboard_sem_login_redirect (apps.accounts.tests.test_admin.TestCustomAdminSite.test_dashboard_sem_login_redirect) ... ok
test_dashboard_status_200 (apps.accounts.tests.test_admin.TestCustomAdminSite.test_dashboard_status_200) ... C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_fim_inscricao received a naive datetime (2026-05-28 00:00:00) while time zone support is active.
  warnings.warn(
ok
test_gerar_senha_provisoria_seleciona_1 (apps.accounts.tests.test_admin.TestUsuarioAdminActionGerarSenhaProvisoria.test_gerar_senha_provisoria_seleciona_1) ... ok
test_gerar_senha_provisoria_seleciona_2_falha (apps.accounts.tests.test_admin.TestUsuarioAdminActionGerarSenhaProvisoria.test_gerar_senha_provisoria_seleciona_2_falha) ... ok
test_usuario_admin_add_status_200 (apps.accounts.tests.test_admin.TestUsuarioAdminAdd.test_usuario_admin_add_status_200) ... ok
test_usuario_admin_add_usuario (apps.accounts.tests.test_admin.TestUsuarioAdminAdd.test_usuario_admin_add_usuario) ... ok
test_usuario_admin_list_pesquisa_por_username (apps.accounts.tests.test_admin.TestUsuarioAdminList.test_usuario_admin_list_pesquisa_por_username) ... ok
test_usuario_admin_list_sem_login_redirect (apps.accounts.tests.test_admin.TestUsuarioAdminList.test_usuario_admin_list_sem_login_redirect) ... ok
test_usuario_admin_list_status_200 (apps.accounts.tests.test_admin.TestUsuarioAdminList.test_usuario_admin_list_status_200) ... ok

----------------------------------------------------------------------
Ran 11 tests in 10.662s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...



## apps.selecao.tests.test_reports.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> pytest apps/selecao/tests/test_reports.py -v
========================================================== test session starts ===========================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 13 items                                                                                                                        

apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_valido PASSED                                  [  7%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_none PASSED                                    [ 15%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_vazio PASSED                                   [ 23%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_ja_formatado PASSED                            [ 30%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_menos_de_11 PASSED                             [ 38%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_mascarado_valido PASSED                        [ 46%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_mascarado_none PASSED                          [ 53%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_mascarado_vazio PASSED                         [ 61%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_telefone_celular PASSED                            [ 69%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_telefone_fixo PASSED                               [ 76%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_telefone_none PASSED                               [ 84%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_telefone_vazio PASSED                              [ 92%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_telefone_ja_formatado PASSED                       [100%]

---------- coverage: platform win32, python 3.13.2-final-0 -----------
Name                                                                    Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------------------
apps\__init__.py                                                            0      0   100%
apps\academico\__init__.py                                                  0      0   100%
apps\academico\admin.py                                                   316    246    22%   64-70, 124, 129, 200, 205, 211-216, 225-266, 270-276, 284-440, 450-613, 623-653, 663-671
apps\academico\apps.py                                                      5      0   100%
apps\academico\certificado.py                                             136    136     0%   9-254
apps\academico\models.py                                                  110     51    54%   45, 122, 128-154, 167-176, 191-214, 282-283, 300-316, 330-342
apps\academico\services.py                                                134    134     0%   8-396
apps\academico\urls.py                                                      5      5     0%   8-19
apps\academico\views.py                                                    63     63     0%   8-124
apps\accounts\__init__.py                                                   0      0   100%
apps\accounts\admin.py                                                     52     19    63%   40-44, 48-63, 149-169
apps\accounts\apps.py                                                       5      0   100%
apps\accounts\forms.py                                                      5      5     0%   8-27
apps\accounts\middleware.py                                                20     20     0%   17-83
apps\accounts\models.py                                                    22      4    82%   103-106
apps\accounts\urls.py                                                       5      5     0%   9-17
apps\accounts\views.py                                                     47     47     0%   16-114
apps\accounts\views_exclusao.py                                            77     77     0%   9-125
apps\dashboard\__init__.py                                                  0      0   100%
apps\dashboard\admin.py                                                     0      0   100%
apps\dashboard\apps.py                                                      4      0   100%
apps\dashboard\models.py                                                    1      0   100%
apps\dashboard\utils_pdf.py                                               373    373     0%   9-751
apps\dashboard\views.py                                                   216    216     0%   13-690
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212    117    45%   61-67, 95, 110-114, 118-119, 122-124, 173-181, 187-206, 218-223, 229-234, 240-245, 251-256, 269-358, 371-415, 430-519, 537
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51     51     0%   8-114
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122     29    76%   28, 104-106, 127, 130-132, 135-137, 140-142, 145-147, 150-152, 155-160, 201, 206, 247, 280
apps\eventos\views.py                                                       1      1     0%   1
apps\interessados\__init__.py                                               0      0   100%
apps\interessados\admin.py                                                218    120    45%   178-183, 188, 193-194, 201-207, 216-222, 231-243, 248-260, 265-269, 280-282, 296-316, 329-330, 337-338, 347-431, 475, 480-481, 485-500, 509, 514, 523-527, 535-538, 546-552, 564, 567, 570
apps\interessados\apps.py                                                   5      0   100%
apps\interessados\authentication.py                                        25     25     0%   9-73
apps\interessados\forms.py                                                157    157     0%   20-453
apps\interessados\management\__init__.py                                    0      0   100%
apps\interessados\management\commands\__init__.py                           0      0   100%
apps\interessados\management\commands\criptografar_cpfs.py                 22     22     0%   11-47
apps\interessados\management\commands\limpar_tokens.py                     59     59     0%   13-155
apps\interessados\management\commands\popular_cpf_hash.py                  22     22     0%   9-40
apps\interessados\models.py                                               139     19    86%   22, 29, 41, 132, 135, 138, 141, 144, 147, 151, 155, 158, 162, 166, 172, 188, 191-192, 260
apps\interessados\urls.py                                                   5      5     0%   11-17
apps\interessados\utils.py                                                 14     14     0%   10-38
apps\interessados\views.py                                                202    202     0%   24-519
apps\interessados\views_exclusao.py                                        29     29     0%   8-76
apps\portal\__init__.py                                                     1      0   100%
apps\portal\admin.py                                                        1      0   100%
apps\portal\apps.py                                                         5      0   100%
apps\portal\forms.py                                                       34     34     0%   14-104
apps\portal\models.py                                                       1      0   100%
apps\portal\urls.py                                                         4      4     0%   8-13
apps\portal\views.py                                                       99     99     0%   13-247
apps\scripts_admin\__init__.py                                              0      0   100%
apps\scripts_admin\management\__init__.py                                   0      0   100%
apps\scripts_admin\management\commands\__init__.py                          0      0   100%
apps\scripts_admin\management\commands\classificar_evento.py              133    133     0%   8-291
apps\scripts_admin\management\commands\configurar_criterios_evento.py      57     57     0%   5-91
apps\scripts_admin\management\commands\popular_criterios.py                21     21     0%   4-117
apps\scripts_admin\management\commands\popular_dados_iniciais.py           66     66     0%   8-234
apps\selecao\__init__.py                                                    0      0   100%
apps\selecao\admin.py                                                     275    163    41%   66-72, 87, 110-115, 152, 223, 233, 240-241, 247, 254-255, 266-275, 293-456, 466-503, 507-544, 552, 558, 564, 570, 580, 586, 592, 598, 608, 612, 616, 661, 667, 673, 677
apps\selecao\apps.py                                                        5      0   100%
apps\selecao\management\__init__.py                                         0      0   100%
apps\selecao\management\commands\__init__.py                                0      0   100%
apps\selecao\models.py                                                     71     15    79%   38, 74, 124-137, 145-146, 155, 188
apps\selecao\reports.py                                                   301    252    16%   27-31, 35-115, 146, 163, 179-286, 302-420, 440-565, 580-711
apps\selecao\services.py                                                  125    125     0%   28-443
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4189   3348    20%
Coverage HTML written to dir htmlcov


=========================================================== 13 passed in 3.09s ===========================================================




## apps.accounts.tests.test_middleware.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.accounts.tests.test_middleware -v 2
Found 9 test(s).
Creating test database for alias 'default' ('test_bdmetareciclagem')...
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_interessado_com_must_change_password_url_restrita (apps.accounts.tests.test_middleware.TestTrocarSenhaObrigatorioMiddleware.test_interessado_com_must_change_password_url_restrita) ... ok
test_media_url_liberada_mesmo_com_must_change_password (apps.accounts.tests.test_middleware.TestTrocarSenhaObrigatorioMiddleware.test_media_url_liberada_mesmo_com_must_change_password) ... ok
test_static_url_liberada_mesmo_com_must_change_password (apps.accounts.tests.test_middleware.TestTrocarSenhaObrigatorioMiddleware.test_static_url_liberada_mesmo_com_must_change_password) ... ok
test_url_admin_login_liberada (apps.accounts.tests.test_middleware.TestTrocarSenhaObrigatorioMiddleware.test_url_admin_login_liberada) ... ok
test_url_admin_logout_liberada (apps.accounts.tests.test_middleware.TestTrocarSenhaObrigatorioMiddleware.test_url_admin_logout_liberada) ... ok
test_usuario_com_must_change_password_url_liberada_staff (apps.accounts.tests.test_middleware.TestTrocarSenhaObrigatorioMiddleware.test_usuario_com_must_change_password_url_liberada_staff) ... ok
test_usuario_com_must_change_password_url_restrita_staff (apps.accounts.tests.test_middleware.TestTrocarSenhaObrigatorioMiddleware.test_usuario_com_must_change_password_url_restrita_staff) ... ok
test_usuario_nao_autenticado_passa (apps.accounts.tests.test_middleware.TestTrocarSenhaObrigatorioMiddleware.test_usuario_nao_autenticado_passa) ... ok
test_usuario_sem_must_change_password_passa (apps.accounts.tests.test_middleware.TestTrocarSenhaObrigatorioMiddleware.test_usuario_sem_must_change_password_passa) ... ok

----------------------------------------------------------------------
Ran 9 tests in 12.263s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...



## apps.academico.tests.test_admin.py em 09/06/2026


(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> pytest apps/academico/tests/test_admin.py -vpytest apps/academico/tests/test_admin.py -v
========================================================== test session starts ===========================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 22 items                                                                                                                        

apps/academico/tests/test_admin.py::TestStatusMatriculaAdmin::test_cor_display_com_cor PASSED                                       [  4%]
apps/academico/tests/test_admin.py::TestStatusMatriculaAdmin::test_cor_display_sem_cor PASSED                                       [  9%]
apps/academico/tests/test_admin.py::TestMatriculaAdmin::test_get_interessado PASSED                                                 [ 13%]
apps/academico/tests/test_admin.py::TestMatriculaAdmin::test_get_evento PASSED                                                      [ 18%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_acoes_certificado_aprovado PASSED                                      [ 22%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_acoes_certificado_nao_aprovado PASSED                                  [ 27%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_changelist_view_contexto PASSED                                        [ 31%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_gerar_certificados_marca_emitidos PASSED                               [ 36%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_gerar_certificados_sem_aprovados PASSED                                [ 40%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_gerar_certificados_ja_emitido PASSED                                   [ 45%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_download_certificados_lote_action_redirect PASSED                      [ 50%]
apps/academico/tests/test_admin.py::TestStatusMatriculaAdmin::test_cor_display_com_cor PASSED                                       [ 50%]
apps/academico/tests/test_admin.py::TestStatusMatriculaAdmin::test_cor_display_sem_cor PASSED                                       [ 50%]
apps/academico/tests/test_admin.py::TestMatriculaAdmin::test_get_interessado PASSED                                                 [ 50%]
apps/academico/tests/test_admin.py::TestMatriculaAdmin::test_get_evento PASSED                                                      [ 50%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_acoes_certificado_aprovado PASSED                                      [ 50%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_acoes_certificado_nao_aprovado PASSED                                  [ 50%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_changelist_view_contexto PASSED                                        [ 50%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_gerar_certificados_marca_emitidos PASSED                               [ 50%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_gerar_certificados_sem_aprovados PASSED                                [ 50%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_gerar_certificados_ja_emitido PASSED                                   [ 50%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_download_certificados_lote_action_redirect PASSED                      [ 50%]

---------- coverage: platform win32, python 3.13.2-final-0 -----------
Name                                                                    Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------------------
apps\__init__.py                                                            0      0   100%
apps\academico\__init__.py                                                  0      0   100%
apps\academico\admin.py                                                   320    199    38%   245-264, 270-276, 284-440, 450-613, 641-642, 666-667, 678, 681
apps\academico\apps.py                                                      5      0   100%
apps\academico\certificado.py                                             136    118    13%   24-37, 43-67, 72-79, 83-104, 108-116, 120-163, 167-208, 212-254
apps\academico\models.py                                                  110     34    69%   45, 122, 133, 142, 154, 168, 174, 191-214, 300-316, 339-342
apps\academico\services.py                                                134    134     0%   8-396
apps\academico\urls.py                                                      5      0   100%
apps\academico\views.py                                                    63     45    29%   31-52, 61-77, 87-124
apps\accounts\__init__.py                                                   0      0   100%
apps\accounts\admin.py                                                     52     16    69%   48-63, 149-169
apps\accounts\apps.py                                                       5      0   100%
apps\accounts\forms.py                                                      5      5     0%   8-27
apps\accounts\middleware.py                                                20      9    55%   66-81
apps\accounts\models.py                                                    22      4    82%   103-106
apps\accounts\urls.py                                                       5      0   100%
apps\accounts\views.py                                                     47     38    19%   26-52, 60-62, 83-114
apps\accounts\views_exclusao.py                                            77     66    14%   19, 25-33, 43-83, 94-125
apps\dashboard\__init__.py                                                  0      0   100%
apps\dashboard\admin.py                                                     0      0   100%
apps\dashboard\apps.py                                                      4      0   100%
apps\dashboard\models.py                                                    1      0   100%
apps\dashboard\utils_pdf.py                                               373    373     0%   9-751
apps\dashboard\views.py                                                   216    193    11%   23-66, 72-130, 136-319, 325-381, 386-407, 417-552, 558-613, 619-651, 657-690
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212    116    45%   61-67, 110-114, 118-119, 122-124, 173-181, 187-206, 218-223, 229-234, 240-245, 251-256, 269-358, 371-415, 430-519, 537
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51     23    55%   25, 39, 67-81, 87-95, 101-112
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122     27    78%   28, 104-106, 130-132, 135-137, 140-142, 145-147, 150-152, 155-160, 201, 206, 280
apps\eventos\views.py                                                       1      1     0%   1
apps\interessados\__init__.py                                               0      0   100%
apps\interessados\admin.py                                                218    117    46%   178-183, 188, 193-194, 201-207, 216-222, 231-243, 248-260, 265-269, 280-282, 296-316, 329-330, 337-338, 347-431, 475, 480-481, 485-500, 509, 514, 523-527, 535-538, 546-552
apps\interessados\apps.py                                                   5      0   100%
apps\interessados\authentication.py                                        25     25     0%   9-73
apps\interessados\forms.py                                                157    106    32%   167-171, 179-213, 220-230, 234-235, 239-243, 247, 251, 255, 259, 263, 267, 271, 275-280, 287-302, 335-358, 392-396, 401-402, 406-410, 414, 418, 422, 426, 430, 434, 438, 445-453
apps\interessados\management\__init__.py                                    0      0   100%
apps\interessados\management\commands\__init__.py                           0      0   100%
apps\interessados\management\commands\criptografar_cpfs.py                 22     22     0%   11-47
apps\interessados\management\commands\limpar_tokens.py                     59     59     0%   13-155
apps\interessados\management\commands\popular_cpf_hash.py                  22     22     0%   9-40
apps\interessados\models.py                                               139     17    88%   29, 41, 135, 138, 141, 144, 147, 151, 155, 158, 162, 166, 172, 188, 191-192, 260
apps\interessados\urls.py                                                   5      0   100%
apps\interessados\utils.py                                                 14     14     0%   10-38
apps\interessados\views.py                                                202    167    17%   49-67, 81-107, 113-115, 129-181, 194-216, 232-250, 266-323, 342-414, 422, 430-472, 477, 482, 496-519
apps\interessados\views_exclusao.py                                        29     20    31%   22-67, 76
apps\portal\__init__.py                                                     1      0   100%
apps\portal\admin.py                                                        1      0   100%
apps\portal\apps.py                                                         5      0   100%
apps\portal\forms.py                                                       34     24    29%   45-51, 55-76, 98-104
apps\portal\models.py                                                       1      0   100%
apps\portal\urls.py                                                         4      0   100%
apps\portal\views.py                                                       99     79    20%   30-39, 45-74, 79-82, 87-116, 122-163, 168-189, 196-220, 225-242, 247
apps\scripts_admin\__init__.py                                              0      0   100%
apps\scripts_admin\management\__init__.py                                   0      0   100%
apps\scripts_admin\management\commands\__init__.py                          0      0   100%
apps\scripts_admin\management\commands\classificar_evento.py              133    133     0%   8-291
apps\scripts_admin\management\commands\configurar_criterios_evento.py      57     57     0%   5-91
apps\scripts_admin\management\commands\popular_criterios.py                21     21     0%   4-117
apps\scripts_admin\management\commands\popular_dados_iniciais.py           66     66     0%   8-234
apps\selecao\__init__.py                                                    0      0   100%
apps\selecao\admin.py                                                     275    158    43%   66-72, 87, 110-115, 152, 223, 233, 240-241, 247, 254-255, 266-275, 293-456, 466-503, 507-544, 552, 558, 564, 570, 580, 586, 592, 598, 661, 667
apps\selecao\apps.py                                                        5      0   100%
apps\selecao\management\__init__.py                                         0      0   100%
apps\selecao\management\commands\__init__.py                                0      0   100%
apps\selecao\models.py                                                     71      8    89%   38, 74, 129, 133-134, 137, 155, 188
apps\selecao\reports.py                                                   301    270    10%   27-31, 35-115, 126-132, 140-146, 151-163, 179-286, 302-420, 440-565, 580-711
apps\selecao\services.py                                                  125    125     0%   28-443
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4193   3017    28%
Coverage HTML written to dir htmlcov


========================================================== 22 passed in 20.73s ===========================================================



## apps.academico.tests.test_certificad.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.academico.tests.test_certificado -v 2
Found 10 test(s).
Creating test database for alias 'default' ('test_bdmetareciclagem')...
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_carga_horaria_fallback_40h (apps.academico.tests.test_certificado.TestGeradorCertificado.test_carga_horaria_fallback_40h)
Verifica se quando carga_horaria nao existe no evento, ... C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_inicio_inscricao received a naive datetime (2026-05-29 00:00:00) while time zone support is active.
  warnings.warn(
C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_fim_inscricao received a naive datetime (2026-05-29 00:00:00) while time zone support is active.
  warnings.warn(
ok
test_cpf_formatado (apps.academico.tests.test_certificado.TestGeradorCertificado.test_cpf_formatado)
Verifica a formatacao do CPF: XXX.XXX.XXX-XX ... ok
test_data_emissao_fallback_para_agora (apps.academico.tests.test_certificado.TestGeradorCertificado.test_data_emissao_fallback_para_agora)
Verifica se quando data_emissao_certificado e None, ... ok
test_gerar_pdf_multiplas_chamadas (apps.academico.tests.test_certificado.TestGeradorCertificado.test_gerar_pdf_multiplas_chamadas)
Verifica se pode gerar multiplos PDFs sem erro ... ok
test_gerar_pdf_retorna_buffer_valido (apps.academico.tests.test_certificado.TestGeradorCertificado.test_gerar_pdf_retorna_buffer_valido)
Verifica se gerar_pdf retorna um buffer com PDF valido (%PDF) ... ok
test_inicializacao_atributos (apps.academico.tests.test_certificado.TestGeradorCertificado.test_inicializacao_atributos)
Verifica se o construtor extrai corretamente a cadeia de FK ... ok
test_pagesize_a4_paisagem (apps.academico.tests.test_certificado.TestGeradorCertificado.test_pagesize_a4_paisagem)
Verifica se o tamanho da pagina e A4 em modo paisagem ... ok
test_static_path_construido (apps.academico.tests.test_certificado.TestGeradorCertificado.test_static_path_construido)
Verifica se static_path foi construido com BASE_DIR ... ok
test_traducao_mes_agosto (apps.academico.tests.test_certificado.TestGeradorCertificado.test_traducao_mes_agosto)
Verifica se 'August' e traduzido para 'agosto' ... ok
test_traducao_mes_janeiro (apps.academico.tests.test_certificado.TestGeradorCertificado.test_traducao_mes_janeiro)
Verifica se 'January' e traduzido para 'janeiro' ... ok

----------------------------------------------------------------------
Ran 10 tests in 6.572s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...



## apps.academico.tests.test_models.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.academico.tests.test_models -v 2     
Found 4 test(s).
Creating test database for alias 'default' ('test_bdmetareciclagem')...
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_matricula_criada_corretamente (apps.academico.tests.test_models.TestMatriculaModel.test_matricula_criada_corretamente) ... ok
test_matricula_unique_together_turma_interessado (apps.academico.tests.test_models.TestMatriculaModel.test_matricula_unique_together_turma_interessado)
unique_together = ['turma', 'interessado'] ... ok
test_status_criado_corretamente (apps.academico.tests.test_models.TestStatusMatriculaModel.test_status_criado_corretamente) ... ok
test_status_nome_unique_no_banco (apps.academico.tests.test_models.TestStatusMatriculaModel.test_status_nome_unique_no_banco)
Testa a constraint real, nao o comportamento da factory ... ok

----------------------------------------------------------------------
Ran 4 tests in 1.085s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...




## apps.academico.tests.test_services.py em 09/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> pytest apps/academico/tests/test_services.py -v
========================================================== test session starts ===========================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 19 items                                                                                                                        

apps/academico/tests/test_services.py::TestVerificacaoDisponibilidade::test_verificar_disponibilidade_turma_com_vagas PASSED        [  5%]
apps/academico/tests/test_services.py::TestVerificacaoDisponibilidade::test_verificar_disponibilidade_turma_lotada PASSED           [ 10%]
apps/academico/tests/test_services.py::TestVerificacaoDisponibilidade::test_verificar_disponibilidade_turma_parcial PASSED          [ 15%]
apps/academico/tests/test_services.py::TestVerificacaoDisponibilidade::test_verificar_disponibilidade_turma_exatamente_cheia PASSED [ 21%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_aprovado PASSED                                       [ 26%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_reprovado_por_nota PASSED                             [ 31%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_reprovado_por_frequencia PASSED                       [ 36%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_nota_invalida PASSED                                  [ 42%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_frequencia_invalida PASSED                            [ 47%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_nota_limite_minimo_aprovado PASSED                    [ 52%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_nota_limite_maximo PASSED                             [ 57%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_frequencia_limite_minimo PASSED                       [ 63%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_frequencia_limite_maximo PASSED                       [ 68%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_atualiza_status_matricula PASSED                      [ 73%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_cria_ou_atualiza PASSED                               [ 78%]
apps/academico/tests/test_services.py::TestRelatorioTurma::test_gerar_relatorio_turma PASSED                                        [ 84%]
apps/academico/tests/test_services.py::TestRelatorioTurma::test_gerar_relatorio_turma_vazia PASSED                                  [ 89%]
apps/academico/tests/test_services.py::TestRelatorioTurma::test_gerar_relatorio_turma_parcialmente_avaliada PASSED                  [ 94%]
apps/academico/tests/test_services.py::TestRelatorioTurma::test_gerar_relatorio_turma_valida_valores PASSED                         [100%]

---------- coverage: platform win32, python 3.13.2-final-0 -----------
Name                                                                    Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------------------
apps\__init__.py                                                            0      0   100%
apps\academico\__init__.py                                                  0      0   100%
apps\academico\admin.py                                                   320    248    22%   64-70, 124, 129, 200, 205, 211-216, 225-266, 270-276, 284-440, 450-613, 623-653, 663-671, 678, 681
apps\academico\apps.py                                                      5      0   100%
apps\academico\certificado.py                                             136    136     0%   9-254
apps\academico\models.py                                                  110     25    77%   45, 122, 133, 142, 154, 168, 204-206, 282-283, 300-316, 339-342
apps\academico\services.py                                                136     72    47%   65-106, 121-144, 165-232, 255-283
apps\academico\urls.py                                                      5      5     0%   8-19
apps\academico\views.py                                                    63     63     0%   8-124
apps\accounts\__init__.py                                                   0      0   100%
apps\accounts\admin.py                                                     52     19    63%   40-44, 48-63, 149-169
apps\accounts\apps.py                                                       5      0   100%
apps\accounts\forms.py                                                      5      5     0%   8-27
apps\accounts\middleware.py                                                20     20     0%   17-83
apps\accounts\models.py                                                    22      4    82%   103-106
apps\accounts\urls.py                                                       5      5     0%   9-17
apps\accounts\views.py                                                     47     47     0%   16-114
apps\accounts\views_exclusao.py                                            77     77     0%   9-125
apps\dashboard\__init__.py                                                  0      0   100%
apps\dashboard\admin.py                                                     0      0   100%
apps\dashboard\apps.py                                                      4      0   100%
apps\dashboard\models.py                                                    1      0   100%
apps\dashboard\utils_pdf.py                                               373    373     0%   9-751
apps\dashboard\views.py                                                   216    216     0%   13-690
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212    117    45%   61-67, 95, 110-114, 118-119, 122-124, 173-181, 187-206, 218-223, 229-234, 240-245, 251-256, 269-358, 371-415, 430-519, 537
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51     51     0%   8-114
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122     29    76%   28, 104-106, 127, 130-132, 135-137, 140-142, 145-147, 150-152, 155-160, 201, 206, 247, 280
apps\eventos\views.py                                                       1      1     0%   1
apps\interessados\__init__.py                                               0      0   100%
apps\interessados\admin.py                                                218    120    45%   178-183, 188, 193-194, 201-207, 216-222, 231-243, 248-260, 265-269, 280-282, 296-316, 329-330, 337-338, 347-431, 475, 480-481, 485-500, 509, 514, 523-527, 535-538, 546-552, 564, 567, 570
apps\interessados\apps.py                                                   5      0   100%
apps\interessados\authentication.py                                        25     25     0%   9-73
apps\interessados\forms.py                                                157    157     0%   20-453
apps\interessados\management\__init__.py                                    0      0   100%
apps\interessados\management\commands\__init__.py                           0      0   100%
apps\interessados\management\commands\criptografar_cpfs.py                 22     22     0%   11-47
apps\interessados\management\commands\limpar_tokens.py                     59     59     0%   13-155
apps\interessados\management\commands\popular_cpf_hash.py                  22     22     0%   9-40
apps\interessados\models.py                                               139     18    87%   22, 29, 41, 135, 138, 141, 144, 147, 151, 155, 158, 162, 166, 172, 188, 191-192, 260
apps\interessados\urls.py                                                   5      5     0%   11-17
apps\interessados\utils.py                                                 14     14     0%   10-38
apps\interessados\views.py                                                202    202     0%   24-519
apps\interessados\views_exclusao.py                                        29     29     0%   8-76
apps\portal\__init__.py                                                     1      0   100%
apps\portal\admin.py                                                        1      0   100%
apps\portal\apps.py                                                         5      0   100%
apps\portal\forms.py                                                       34     34     0%   14-104
apps\portal\models.py                                                       1      0   100%
apps\portal\urls.py                                                         4      4     0%   8-13
apps\portal\views.py                                                       99     99     0%   13-247
apps\scripts_admin\__init__.py                                              0      0   100%
apps\scripts_admin\management\__init__.py                                   0      0   100%
apps\scripts_admin\management\commands\__init__.py                          0      0   100%
apps\scripts_admin\management\commands\classificar_evento.py              133    133     0%   8-291
apps\scripts_admin\management\commands\configurar_criterios_evento.py      57     57     0%   5-91
apps\scripts_admin\management\commands\popular_criterios.py                21     21     0%   4-117
apps\scripts_admin\management\commands\popular_dados_iniciais.py           66     66     0%   8-234
apps\selecao\__init__.py                                                    0      0   100%
apps\selecao\admin.py                                                     275    163    41%   66-72, 87, 110-115, 152, 223, 233, 240-241, 247, 254-255, 266-275, 293-456, 466-503, 507-544, 552, 558, 564, 570, 580, 586, 592, 598, 608, 612, 616, 661, 667, 673, 677
apps\selecao\apps.py                                                        5      0   100%
apps\selecao\management\__init__.py                                         0      0   100%
apps\selecao\management\commands\__init__.py                                0      0   100%
apps\selecao\models.py                                                     71     15    79%   38, 74, 124-137, 145-146, 155, 188
apps\selecao\reports.py                                                   301    270    10%   27-31, 35-115, 126-132, 140-146, 151-163, 179-286, 302-420, 440-565, 580-711
apps\selecao\services.py                                                  125    125     0%   28-443
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4195   3279    22%
Coverage HTML written to dir htmlcov


========================================================== 19 passed in 14.12s ===========================================================




## apps.academico.tests.test_views.py


(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.academico.tests.test_views -v 2
Found 11 test(s).
Creating test database for alias 'default' ('test_bdmetareciclagem')...
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_aluno_aprovado_gera_pdf (apps.academico.tests.test_views.TestDownloadCertificadoIndividual.test_aluno_aprovado_gera_pdf) ... ok
test_aluno_reprovado_retorna_400 (apps.academico.tests.test_views.TestDownloadCertificadoIndividual.test_aluno_reprovado_retorna_400) ... ok
test_avaliacao_inexistente_retorna_404 (apps.academico.tests.test_views.TestDownloadCertificadoIndividual.test_avaliacao_inexistente_retorna_404) ... ok
test_sem_autenticacao_redireciona (apps.academico.tests.test_views.TestDownloadCertificadoIndividual.test_sem_autenticacao_redireciona) ... ok
test_apenas_aprovados_no_zip (apps.academico.tests.test_views.TestDownloadCertificadosLote.test_apenas_aprovados_no_zip) ... ok
test_ids_invalidos_retorna_400 (apps.academico.tests.test_views.TestDownloadCertificadosLote.test_ids_invalidos_retorna_400) ... ok
test_sem_ids_retorna_400 (apps.academico.tests.test_views.TestDownloadCertificadosLote.test_sem_ids_retorna_400) ... ok
test_zip_com_multiplos_certificados (apps.academico.tests.test_views.TestDownloadCertificadosLote.test_zip_com_multiplos_certificados) ... ok
test_aluno_aprovado_inline (apps.academico.tests.test_views.TestPreviewCertificado.test_aluno_aprovado_inline) ... ok
test_aluno_reprovado_retorna_400 (apps.academico.tests.test_views.TestPreviewCertificado.test_aluno_reprovado_retorna_400) ... ok
test_sem_autenticacao_redireciona (apps.academico.tests.test_views.TestPreviewCertificado.test_sem_autenticacao_redireciona) ... ok

----------------------------------------------------------------------
Ran 11 tests in 9.858s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...



## apps.dashboard.tests.test_utils_pdf.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.dashboard.tests.test_utils_pdf -v 2
Found 9 test(s).
Skipping setup of unused database(s): default.
System check identified no issues (0 silenced).
test_dados_validos_retorna_buffer (apps.dashboard.tests.test_utils_pdf.TestCriarGraficoBarras.test_dados_validos_retorna_buffer) ... ok
test_dados_validos_retorna_buffer (apps.dashboard.tests.test_utils_pdf.TestCriarGraficoPizza.test_dados_validos_retorna_buffer) ... ok
test_lista_vazia_retorna_none (apps.dashboard.tests.test_utils_pdf.TestCriarGraficoPizza.test_lista_vazia_retorna_none) ... ok
test_todos_valores_zero_retorna_none (apps.dashboard.tests.test_utils_pdf.TestCriarGraficoPizza.test_todos_valores_zero_retorna_none) ... ok
test_um_item_valido_retorna_buffer (apps.dashboard.tests.test_utils_pdf.TestCriarGraficoPizza.test_um_item_valido_retorna_buffer) ... ok
test_context_minimo_retorna_buffer (apps.dashboard.tests.test_utils_pdf.TestGerarPdfAcademico.test_context_minimo_retorna_buffer) ... ok
test_context_minimo_retorna_buffer (apps.dashboard.tests.test_utils_pdf.TestGerarPdfEventos.test_context_minimo_retorna_buffer) ... ok
test_context_minimo_retorna_buffer (apps.dashboard.tests.test_utils_pdf.TestGerarPdfInteressados.test_context_minimo_retorna_buffer) ... ok
test_context_minimo_retorna_buffer (apps.dashboard.tests.test_utils_pdf.TestGerarPdfProcessoSeletivo.test_context_minimo_retorna_buffer) ... ok

----------------------------------------------------------------------
Ran 9 tests in 1.008s

OK


## apps.dashboard.tests.test_views.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.dashboard.tests.test_views -v 2
Found 22 test(s).
Creating test database for alias 'default' ('test_bdmetareciclagem')...
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_pdf_academico_sem_auth_redireciona (apps.dashboard.tests.test_views.TestDashboardPdfViews.test_pdf_academico_sem_auth_redireciona) ... ok
test_pdf_academico_staff_200 (apps.dashboard.tests.test_views.TestDashboardPdfViews.test_pdf_academico_staff_200) ... ok
test_pdf_eventos_sem_auth_redireciona (apps.dashboard.tests.test_views.TestDashboardPdfViews.test_pdf_eventos_sem_auth_redireciona) ... ok
test_pdf_eventos_staff_200 (apps.dashboard.tests.test_views.TestDashboardPdfViews.test_pdf_eventos_staff_200) ... ok
test_pdf_interessados_sem_auth_redireciona (apps.dashboard.tests.test_views.TestDashboardPdfViews.test_pdf_interessados_sem_auth_redireciona) ... ok
test_pdf_interessados_sem_dados_nao_quebra (apps.dashboard.tests.test_views.TestDashboardPdfViews.test_pdf_interessados_sem_dados_nao_quebra) ... ok
test_pdf_interessados_staff_200 (apps.dashboard.tests.test_views.TestDashboardPdfViews.test_pdf_interessados_staff_200) ... ok
test_pdf_processo_seletivo_sem_auth_redireciona (apps.dashboard.tests.test_views.TestDashboardPdfViews.test_pdf_processo_seletivo_sem_auth_redireciona) ... ok
test_pdf_processo_seletivo_staff_200 (apps.dashboard.tests.test_views.TestDashboardPdfViews.test_pdf_processo_seletivo_staff_200) ... C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Inscricao.data_inscricao received a naive datetime (2026-04-29 00:00:00) while time zone support is active.
  warnings.warn(
ok
test_dashboard_academico_non_staff_redireciona (apps.dashboard.tests.test_views.TestDashboardViews.test_dashboard_academico_non_staff_redireciona) ... ok
test_dashboard_academico_sem_auth_redireciona (apps.dashboard.tests.test_views.TestDashboardViews.test_dashboard_academico_sem_auth_redireciona) ... ok
test_dashboard_academico_sem_dados_nao_quebra (apps.dashboard.tests.test_views.TestDashboardViews.test_dashboard_academico_sem_dados_nao_quebra)
Banco vazio nao causa erro 500 ... ok
test_dashboard_academico_staff_200 (apps.dashboard.tests.test_views.TestDashboardViews.test_dashboard_academico_staff_200) ... ok
test_dashboard_eventos_sem_auth_redireciona (apps.dashboard.tests.test_views.TestDashboardViews.test_dashboard_eventos_sem_auth_redireciona) ... ok
test_dashboard_eventos_staff_200 (apps.dashboard.tests.test_views.TestDashboardViews.test_dashboard_eventos_staff_200) ... ok
test_dashboard_interessados_sem_auth_redireciona (apps.dashboard.tests.test_views.TestDashboardViews.test_dashboard_interessados_sem_auth_redireciona) ... ok
test_dashboard_interessados_staff_200 (apps.dashboard.tests.test_views.TestDashboardViews.test_dashboard_interessados_staff_200) ... ok
test_dashboard_interessados_total_zero_nao_quebra (apps.dashboard.tests.test_views.TestDashboardViews.test_dashboard_interessados_total_zero_nao_quebra)
Divisao por zero nos percentuais com banco vazio ... ok
test_dashboard_lgpd_sem_auth_redireciona (apps.dashboard.tests.test_views.TestDashboardViews.test_dashboard_lgpd_sem_auth_redireciona) ... ok
test_dashboard_lgpd_staff_200 (apps.dashboard.tests.test_views.TestDashboardViews.test_dashboard_lgpd_staff_200) ... ok
test_dashboard_processo_seletivo_sem_auth_redireciona (apps.dashboard.tests.test_views.TestDashboardViews.test_dashboard_processo_seletivo_sem_auth_redireciona) ... ok
test_dashboard_processo_seletivo_staff_200 (apps.dashboard.tests.test_views.TestDashboardViews.test_dashboard_processo_seletivo_staff_200) ... ok

----------------------------------------------------------------------
Ran 22 tests in 3.275s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...




##  apps/dashboard/tests/test_services.py em 12/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> pytest apps/dashboard/tests/test_services.py -v
========================================================= test session starts ==========================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 22 items                                                                                                                      

apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_distribuicao_deficiencias PASSED           [  4%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_distribuicao_escolaridade PASSED           [  9%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_distribuicao_fototipo PASSED               [ 13%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_distribuicao_programas_sociais PASSED      [ 18%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_distribuicao_sexo PASSED                   [ 22%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_faixas_etarias PASSED                      [ 27%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_metricas_gerais PASSED                     [ 31%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_tipos_deficiencia PASSED                   [ 36%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_obter_contexto_completo PASSED                      [ 40%]
apps/dashboard/tests/test_services.py::TestDashboardEventosService::test_calcular_eventos_por_status PASSED                       [ 45%]
apps/dashboard/tests/test_services.py::TestDashboardEventosService::test_calcular_metricas_gerais PASSED                          [ 50%]
apps/dashboard/tests/test_services.py::TestDashboardEventosService::test_calcular_top_eventos_inscricoes PASSED                   [ 54%]
apps/dashboard/tests/test_services.py::TestDashboardEventosService::test_calcular_turmas_por_status PASSED                        [ 59%]
apps/dashboard/tests/test_services.py::TestDashboardEventosService::test_obter_contexto_completo PASSED                           [ 63%]
apps/dashboard/tests/test_services.py::TestDashboardAcademicoService::test_calcular_metricas_avaliacoes PASSED                    [ 68%]
apps/dashboard/tests/test_services.py::TestDashboardAcademicoService::test_calcular_taxa_aprovacao PASSED                         [ 72%]
apps/dashboard/tests/test_services.py::TestDashboardAcademicoService::test_calcular_top_cursos_aprovados PASSED                   [ 77%]
apps/dashboard/tests/test_services.py::TestDashboardAcademicoService::test_obter_contexto_completo PASSED                         [ 81%]
apps/dashboard/tests/test_services.py::TestDashboardProcessoSeletivoService::test_calcular_metricas_classificacoes PASSED         [ 86%]
apps/dashboard/tests/test_services.py::TestDashboardProcessoSeletivoService::test_calcular_metricas_inscricoes PASSED             [ 90%]
apps/dashboard/tests/test_services.py::TestDashboardProcessoSeletivoService::test_calcular_top_eventos_inscricoes PASSED          [ 95%]
apps/dashboard/tests/test_services.py::TestDashboardProcessoSeletivoService::test_obter_contexto_completo PASSED                  [100%]

---------- coverage: platform win32, python 3.13.2-final-0 -----------
Name                                                                    Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------------------
apps\__init__.py                                                            0      0   100%
apps\academico\__init__.py                                                  0      0   100%
apps\academico\admin.py                                                   320    248    22%   64-70, 124, 129, 200, 205, 211-216, 225-266, 270-276, 284-440, 450-613, 623-653, 663-671, 678, 681
apps\academico\apps.py                                                      5      0   100%
apps\academico\certificado.py                                             136    136     0%   9-254
apps\academico\models.py                                                  110     28    75%   45, 122, 133, 142, 154, 168, 201-206, 282-283, 300-316, 339-342
apps\academico\services.py                                                136    136     0%   8-402
apps\academico\urls.py                                                      5      5     0%   8-19
apps\academico\views.py                                                    63     63     0%   8-124
apps\accounts\__init__.py                                                   0      0   100%
apps\accounts\admin.py                                                     52     19    63%   40-44, 48-63, 149-169
apps\accounts\apps.py                                                       5      0   100%
apps\accounts\forms.py                                                      5      5     0%   8-27
apps\accounts\middleware.py                                                20     20     0%   17-83
apps\accounts\models.py                                                    22      4    82%   103-106
apps\accounts\urls.py                                                       5      5     0%   9-17
apps\accounts\views.py                                                     47     47     0%   16-114
apps\accounts\views_exclusao.py                                            77     77     0%   9-125
apps\dashboard\__init__.py                                                  0      0   100%
apps\dashboard\admin.py                                                     0      0   100%
apps\dashboard\apps.py                                                      4      0   100%
apps\dashboard\models.py                                                    1      0   100%
apps\dashboard\services.py                                                157      6    96%   88, 111, 161, 282, 308, 371
apps\dashboard\utils_pdf.py                                               373    373     0%   9-751
apps\dashboard\views.py                                                    71     71     0%   13-161
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212    117    45%   61-67, 95, 110-114, 118-119, 122-124, 173-181, 187-206, 218-223, 229-234, 240-245, 251-256, 269-358, 371-415, 430-519, 537
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51     51     0%   8-114
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122     29    76%   28, 104-106, 127, 130-132, 135-137, 140-142, 145-147, 150-152, 155-160, 201, 206, 247, 280
apps\eventos\views.py                                                       1      1     0%   1
apps\interessados\__init__.py                                               0      0   100%
apps\interessados\admin.py                                                218    120    45%   178-183, 188, 193-194, 201-207, 216-222, 231-243, 248-260, 265-269, 280-282, 296-316, 329-330, 337-338, 347-431, 475, 480-481, 485-500, 509, 514, 523-527, 535-538, 546-552, 564, 567, 570
apps\interessados\apps.py                                                   5      0   100%
apps\interessados\authentication.py                                        25     25     0%   9-73
apps\interessados\forms.py                                                157    157     0%   20-453
apps\interessados\management\__init__.py                                    0      0   100%
apps\interessados\management\commands\__init__.py                           0      0   100%
apps\interessados\management\commands\criptografar_cpfs.py                 22     22     0%   11-47
apps\interessados\management\commands\limpar_tokens.py                     59     59     0%   13-155
apps\interessados\management\commands\popular_cpf_hash.py                  22     22     0%   9-40
apps\interessados\models.py                                               139     17    88%   29, 41, 135, 138, 141, 144, 147, 151, 155, 158, 162, 166, 172, 188, 191-192, 260
apps\interessados\urls.py                                                   5      5     0%   11-17
apps\interessados\utils.py                                                 14     14     0%   10-38
apps\interessados\views.py                                                202    202     0%   24-519
apps\interessados\views_exclusao.py                                        29     29     0%   8-76
apps\portal\__init__.py                                                     1      0   100%
apps\portal\admin.py                                                        1      0   100%
apps\portal\apps.py                                                         5      0   100%
apps\portal\forms.py                                                       34     34     0%   14-104
apps\portal\models.py                                                       1      0   100%
apps\portal\urls.py                                                         4      4     0%   8-13
apps\portal\views.py                                                       99     99     0%   13-247
apps\scripts_admin\__init__.py                                              0      0   100%
apps\scripts_admin\management\__init__.py                                   0      0   100%
apps\scripts_admin\management\commands\__init__.py                          0      0   100%
apps\scripts_admin\management\commands\classificar_evento.py              133    133     0%   8-291
apps\scripts_admin\management\commands\configurar_criterios_evento.py      57     57     0%   5-91
apps\scripts_admin\management\commands\popular_criterios.py                21     21     0%   4-117
apps\scripts_admin\management\commands\popular_dados_iniciais.py           66     66     0%   8-234
apps\selecao\__init__.py                                                    0      0   100%
apps\selecao\admin.py                                                     275    163    41%   66-72, 87, 110-115, 152, 223, 233, 240-241, 247, 254-255, 266-275, 293-456, 466-503, 507-544, 552, 558, 564, 570, 580, 586, 592, 598, 608, 612, 616, 661, 667, 673, 677
apps\selecao\apps.py                                                        5      0   100%
apps\selecao\management\__init__.py                                         0      0   100%
apps\selecao\management\commands\__init__.py                                0      0   100%
apps\selecao\models.py                                                     71      8    89%   38, 74, 129, 133-134, 137, 155, 188
apps\selecao\reports.py                                                   301    270    10%   27-31, 35-115, 126-132, 140-146, 151-163, 179-286, 302-420, 440-565, 580-711
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4207   3199    24%
Coverage HTML written to dir htmlcov


========================================================= 22 passed in 14.56s ==========================================================


## apps.eventos.tests.test_context_processors.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.eventos.tests.test_context_processors -v 2
Found 13 test(s).
Creating test database for alias 'default' ('test_bdmetareciclagem')...
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_multiplos_eventos_com_alerta (apps.eventos.tests.test_context_processors.TestNotificacoesEventos.test_multiplos_eventos_com_alerta) ... C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_inicio_inscricao received a naive datetime (2026-05-28 00:00:00) while time zone support is active.
  warnings.warn(
C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_fim_inscricao received a naive datetime (2026-05-30 00:00:00) while time zone support is active.
  warnings.warn(
C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_inicio_inscricao received a naive datetime (2026-04-29 00:00:00) while time zone support is active.
  warnings.warn(
C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_fim_inscricao received a naive datetime (2026-05-09 00:00:00) while time zone support is active.
  warnings.warn(
ok
test_sem_eventos_retorna_lista_vazia (apps.eventos.tests.test_context_processors.TestNotificacoesEventos.test_sem_eventos_retorna_lista_vazia) ... ok
test_usuario_anonimo_retorna_lista_vazia (apps.eventos.tests.test_context_processors.TestNotificacoesEventos.test_usuario_anonimo_retorna_lista_vazia) ... ok
test_usuario_nao_staff_retorna_lista_vazia (apps.eventos.tests.test_context_processors.TestNotificacoesEventos.test_usuario_nao_staff_retorna_lista_vazia) ... ok
test_verificacao1_status_correto_sem_alerta (apps.eventos.tests.test_context_processors.TestNotificacoesEventos.test_verificacao1_status_correto_sem_alerta) ... ok
test_verificacao1_status_errado_gera_alerta (apps.eventos.tests.test_context_processors.TestNotificacoesEventos.test_verificacao1_status_errado_gera_alerta) ... ok
test_verificacao2_status_invalido_gera_alerta (apps.eventos.tests.test_context_processors.TestNotificacoesEventos.test_verificacao2_status_invalido_gera_alerta) ... C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_inicio_inscricao received a naive datetime (2026-05-19 00:00:00) while time zone support is active.
  warnings.warn(
C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_fim_inscricao received a naive datetime (2026-05-28 00:00:00) while time zone support is active.
  warnings.warn(
ok
test_verificacao2_status_valido_sem_alerta (apps.eventos.tests.test_context_processors.TestNotificacoesEventos.test_verificacao2_status_valido_sem_alerta) ... ok
test_verificacao3_status_correto_sem_alerta (apps.eventos.tests.test_context_processors.TestNotificacoesEventos.test_verificacao3_status_correto_sem_alerta) ... C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_inicio_inscricao received a naive datetime (2026-05-09 00:00:00) while time zone support is active.
  warnings.warn(
C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_fim_inscricao received a naive datetime (2026-05-19 00:00:00) while time zone support is active.
  warnings.warn(
ok
test_verificacao3_status_errado_gera_alerta (apps.eventos.tests.test_context_processors.TestNotificacoesEventos.test_verificacao3_status_errado_gera_alerta) ... ok
test_verificacao4_cancelado_sem_alerta (apps.eventos.tests.test_context_processors.TestNotificacoesEventos.test_verificacao4_cancelado_sem_alerta) ... ok
test_verificacao4_status_invalido_gera_alerta (apps.eventos.tests.test_context_processors.TestNotificacoesEventos.test_verificacao4_status_invalido_gera_alerta) ... ok
test_verificacao4_status_valido_sem_alerta (apps.eventos.tests.test_context_processors.TestNotificacoesEventos.test_verificacao4_status_valido_sem_alerta) ... ok

----------------------------------------------------------------------
Ran 13 tests in 1.033s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...



## apps.interessados.tests.test_forms.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.interessados.tests.test_forms -v 2
Found 19 test(s).
Creating test database for alias 'default' ('test_bdmetareciclagem')...
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_cadastro_cpf_duplicado (apps.interessados.tests.test_forms.TestCadastroInteressadoForm.test_cadastro_cpf_duplicado)
Rejeita se CPF ja existe no banco. ... ok
test_cadastro_cpf_invalido_todos_iguais (apps.interessados.tests.test_forms.TestCadastroInteressadoForm.test_cadastro_cpf_invalido_todos_iguais)
Rejeita CPF com todos digitos iguais. ... ok
test_cadastro_email_duplicado (apps.interessados.tests.test_forms.TestCadastroInteressadoForm.test_cadastro_email_duplicado)
Rejeita se email ja existe no banco. ... ok
test_cadastro_sem_consentimento_lgpd (apps.interessados.tests.test_forms.TestCadastroInteressadoForm.test_cadastro_sem_consentimento_lgpd)
Rejeita sem aceitar consentimento LGPD. ... ok
test_cadastro_senhas_nao_conferem (apps.interessados.tests.test_forms.TestCadastroInteressadoForm.test_cadastro_senhas_nao_conferem)
Rejeita se senhas sao diferentes. ... ok
test_cadastro_valido_dados_minimos (apps.interessados.tests.test_forms.TestCadastroInteressadoForm.test_cadastro_valido_dados_minimos)
Formulario valido com dados minimos obrigatorios. ... ok
test_cpf_invalido_digito_verificador (apps.interessados.tests.test_forms.TestCadastroInteressadoForm.test_cpf_invalido_digito_verificador)
Rejeita CPF com digito verificador invalido. ... ok
test_cpf_muito_curto (apps.interessados.tests.test_forms.TestCadastroInteressadoForm.test_cpf_muito_curto)
Rejeita CPF com menos de 11 digitos. ... ok
test_cpf_valido_com_pontuacao (apps.interessados.tests.test_forms.TestCadastroInteressadoForm.test_cpf_valido_com_pontuacao)
Aceita CPF formatado (123.456.789-00). ... ok
test_cpf_nao_aparece_na_edicao (apps.interessados.tests.test_forms.TestEdicaoInteressadoForm.test_cpf_nao_aparece_na_edicao)
CPF nao esta nos fields do formulario de edicao. ... ok
test_edicao_email_invalido_rejeita (apps.interessados.tests.test_forms.TestEdicaoInteressadoForm.test_edicao_email_invalido_rejeita)
Rejeita edicao com email mal formatado. ... ok
test_edicao_sem_nome_rejeita (apps.interessados.tests.test_forms.TestEdicaoInteressadoForm.test_edicao_sem_nome_rejeita)
Rejeita edicao sem nome. ... ok
test_edicao_valida_dados_minimos (apps.interessados.tests.test_forms.TestEdicaoInteressadoForm.test_edicao_valida_dados_minimos)
Formulario valido com dados minimos obrigatorios. ... ok
test_tentativa_alterar_cpf_ignorada (apps.interessados.tests.test_forms.TestEdicaoInteressadoForm.test_tentativa_alterar_cpf_ignorada)
Passar CPF no POST nao altera o cpf_hash do interessado. ... ok
test_login_cpf_formatado_com_pontuacao (apps.interessados.tests.test_forms.TestLoginInteressadoForm.test_login_cpf_formatado_com_pontuacao)
Login funciona com CPF contendo pontos e tracos. ... ok
test_login_cpf_nao_cadastrado (apps.interessados.tests.test_forms.TestLoginInteressadoForm.test_login_cpf_nao_cadastrado)
Login com CPF nao existente. ... ok
test_login_interessado_inativo (apps.interessados.tests.test_forms.TestLoginInteressadoForm.test_login_interessado_inativo)
Login falha se conta esta inativa. ... ok
test_login_senha_incorreta (apps.interessados.tests.test_forms.TestLoginInteressadoForm.test_login_senha_incorreta)
Login com senha errada. ... ok
test_login_valido (apps.interessados.tests.test_forms.TestLoginInteressadoForm.test_login_valido)
Login com CPF e senha corretos. ... ok

----------------------------------------------------------------------
Ran 19 tests in 6.195s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...



## apps.interessados.tests.test_forms.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.interessados.tests.test_models -v 2
Found 38 test(s).
Creating test database for alias 'default' ('test_bdmetareciclagem')...
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_descricao_pode_ser_vazia (apps.interessados.tests.test_models.TestFototipoModel.test_descricao_pode_ser_vazia) ... ok
test_factory_cria_valido (apps.interessados.tests.test_models.TestFototipoModel.test_factory_cria_valido) ... ok
test_cpfs_diferentes_hashes_diferentes (apps.interessados.tests.test_models.TestHashCPF.test_cpfs_diferentes_hashes_diferentes) ... ok
test_hash_tem_64_caracteres (apps.interessados.tests.test_models.TestHashCPF.test_hash_tem_64_caracteres) ... ok
test_mesmo_cpf_mesmo_hash (apps.interessados.tests.test_models.TestHashCPF.test_mesmo_cpf_mesmo_hash) ... ok
test_cep_muito_curto_rejeita (apps.interessados.tests.test_models.TestInteressadoModel.test_cep_muito_curto_rejeita) ... ok
test_cep_valido (apps.interessados.tests.test_models.TestInteressadoModel.test_cep_valido) ... ok
test_check_password_errado (apps.interessados.tests.test_models.TestInteressadoModel.test_check_password_errado) ... ok
test_check_password_ok (apps.interessados.tests.test_models.TestInteressadoModel.test_check_password_ok) ... ok
test_cpf_11_digitos_valido (apps.interessados.tests.test_models.TestInteressadoModel.test_cpf_11_digitos_valido) ... ok
test_cpf_criptografado_no_banco (apps.interessados.tests.test_models.TestInteressadoModel.test_cpf_criptografado_no_banco) ... ok
test_cpf_formatado_aceito_pelo_model (apps.interessados.tests.test_models.TestInteressadoModel.test_cpf_formatado_aceito_pelo_model)
Model aceita CPF formatado (14 chars). A limpeza e da form. ... ok
test_cpf_hash_busca_eficiente (apps.interessados.tests.test_models.TestInteressadoModel.test_cpf_hash_busca_eficiente) ... ok
test_cpf_hash_unico (apps.interessados.tests.test_models.TestInteressadoModel.test_cpf_hash_unico) ... ok
test_factory_cria_interessado_valido (apps.interessados.tests.test_models.TestInteressadoModel.test_factory_cria_interessado_valido) ... ok
test_is_anonymous (apps.interessados.tests.test_models.TestInteressadoModel.test_is_anonymous) ... ok
test_is_authenticated (apps.interessados.tests.test_models.TestInteressadoModel.test_is_authenticated) ... ok
test_multiplas_deficiencias (apps.interessados.tests.test_models.TestInteressadoModel.test_multiplas_deficiencias) ... ok
test_nis_criptografado_no_banco (apps.interessados.tests.test_models.TestInteressadoModel.test_nis_criptografado_no_banco) ... ok
test_nis_muito_curto_rejeita (apps.interessados.tests.test_models.TestInteressadoModel.test_nis_muito_curto_rejeita) ... ok
test_nis_valido (apps.interessados.tests.test_models.TestInteressadoModel.test_nis_valido) ... ok
test_relacionamento_fototipo (apps.interessados.tests.test_models.TestInteressadoModel.test_relacionamento_fototipo) ... ok
test_relacionamento_sexo (apps.interessados.tests.test_models.TestInteressadoModel.test_relacionamento_sexo) ... ok
test_relacionamentos_simultaneos (apps.interessados.tests.test_models.TestInteressadoModel.test_relacionamentos_simultaneos) ... ok
test_senha_nao_e_texto_puro (apps.interessados.tests.test_models.TestInteressadoModel.test_senha_nao_e_texto_puro) ... ok
test_str_contem_nome (apps.interessados.tests.test_models.TestInteressadoModel.test_str_contem_nome) ... ok
test_tem_deficiencia_property (apps.interessados.tests.test_models.TestInteressadoModel.test_tem_deficiencia_property) ... ok
test_expiracao_futura (apps.interessados.tests.test_models.TestPasswordResetTokenModel.test_expiracao_futura) ... ok
test_factory_cria_token_valido (apps.interessados.tests.test_models.TestPasswordResetTokenModel.test_factory_cria_token_valido) ... ok
test_marca_como_usado (apps.interessados.tests.test_models.TestPasswordResetTokenModel.test_marca_como_usado) ... ok
test_factory_cria_valido (apps.interessados.tests.test_models.TestSexoModel.test_factory_cria_valido) ... ok
test_str_retorna_nome (apps.interessados.tests.test_models.TestSexoModel.test_str_retorna_nome) ... ok
test_unique_constraint_violado (apps.interessados.tests.test_models.TestSexoModel.test_unique_constraint_violado) ... ok
test_criada_com_status_pendente (apps.interessados.tests.test_models.TestSolicitacaoExclusao.test_criada_com_status_pendente) ... ok
test_email_solicitante_opcional (apps.interessados.tests.test_models.TestSolicitacaoExclusao.test_email_solicitante_opcional) ... ok
test_nome_solicitante_obrigatorio (apps.interessados.tests.test_models.TestSolicitacaoExclusao.test_nome_solicitante_obrigatorio) ... ok
test_str_contem_status_e_nome (apps.interessados.tests.test_models.TestSolicitacaoExclusao.test_str_contem_status_e_nome) ... ok
test_todos_os_status_sao_validos (apps.interessados.tests.test_models.TestSolicitacaoExclusao.test_todos_os_status_sao_validos) ... ok

----------------------------------------------------------------------
Ran 38 tests in 14.695s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...



## apps.interessados.tests.test_models.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.interessados.tests.test_models -v 2
Found 38 test(s).
Creating test database for alias 'default' ('test_bdmetareciclagem')...
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_descricao_pode_ser_vazia (apps.interessados.tests.test_models.TestFototipoModel.test_descricao_pode_ser_vazia) ... ok
test_factory_cria_valido (apps.interessados.tests.test_models.TestFototipoModel.test_factory_cria_valido) ... ok
test_cpfs_diferentes_hashes_diferentes (apps.interessados.tests.test_models.TestHashCPF.test_cpfs_diferentes_hashes_diferentes) ... ok
test_hash_tem_64_caracteres (apps.interessados.tests.test_models.TestHashCPF.test_hash_tem_64_caracteres) ... ok
test_mesmo_cpf_mesmo_hash (apps.interessados.tests.test_models.TestHashCPF.test_mesmo_cpf_mesmo_hash) ... ok
test_cep_muito_curto_rejeita (apps.interessados.tests.test_models.TestInteressadoModel.test_cep_muito_curto_rejeita) ... ok
test_cep_valido (apps.interessados.tests.test_models.TestInteressadoModel.test_cep_valido) ... ok
test_check_password_errado (apps.interessados.tests.test_models.TestInteressadoModel.test_check_password_errado) ... ok
test_check_password_ok (apps.interessados.tests.test_models.TestInteressadoModel.test_check_password_ok) ... ok
test_cpf_11_digitos_valido (apps.interessados.tests.test_models.TestInteressadoModel.test_cpf_11_digitos_valido) ... ok
test_cpf_criptografado_no_banco (apps.interessados.tests.test_models.TestInteressadoModel.test_cpf_criptografado_no_banco) ... ok
test_cpf_formatado_aceito_pelo_model (apps.interessados.tests.test_models.TestInteressadoModel.test_cpf_formatado_aceito_pelo_model)
Model aceita CPF formatado (14 chars). A limpeza e da form. ... ok
test_cpf_hash_busca_eficiente (apps.interessados.tests.test_models.TestInteressadoModel.test_cpf_hash_busca_eficiente) ... ok
test_cpf_hash_unico (apps.interessados.tests.test_models.TestInteressadoModel.test_cpf_hash_unico) ... ok
test_factory_cria_interessado_valido (apps.interessados.tests.test_models.TestInteressadoModel.test_factory_cria_interessado_valido) ... ok
test_is_anonymous (apps.interessados.tests.test_models.TestInteressadoModel.test_is_anonymous) ... ok
test_is_authenticated (apps.interessados.tests.test_models.TestInteressadoModel.test_is_authenticated) ... ok
test_multiplas_deficiencias (apps.interessados.tests.test_models.TestInteressadoModel.test_multiplas_deficiencias) ... ok
test_nis_criptografado_no_banco (apps.interessados.tests.test_models.TestInteressadoModel.test_nis_criptografado_no_banco) ... ok
test_nis_muito_curto_rejeita (apps.interessados.tests.test_models.TestInteressadoModel.test_nis_muito_curto_rejeita) ... ok
test_nis_valido (apps.interessados.tests.test_models.TestInteressadoModel.test_nis_valido) ... ok
test_relacionamento_fototipo (apps.interessados.tests.test_models.TestInteressadoModel.test_relacionamento_fototipo) ... ok
test_relacionamento_sexo (apps.interessados.tests.test_models.TestInteressadoModel.test_relacionamento_sexo) ... ok
test_relacionamentos_simultaneos (apps.interessados.tests.test_models.TestInteressadoModel.test_relacionamentos_simultaneos) ... ok
test_senha_nao_e_texto_puro (apps.interessados.tests.test_models.TestInteressadoModel.test_senha_nao_e_texto_puro) ... ok
test_str_contem_nome (apps.interessados.tests.test_models.TestInteressadoModel.test_str_contem_nome) ... ok
test_tem_deficiencia_property (apps.interessados.tests.test_models.TestInteressadoModel.test_tem_deficiencia_property) ... ok
test_expiracao_futura (apps.interessados.tests.test_models.TestPasswordResetTokenModel.test_expiracao_futura) ... ok
test_factory_cria_token_valido (apps.interessados.tests.test_models.TestPasswordResetTokenModel.test_factory_cria_token_valido) ... ok
test_marca_como_usado (apps.interessados.tests.test_models.TestPasswordResetTokenModel.test_marca_como_usado) ... ok
test_factory_cria_valido (apps.interessados.tests.test_models.TestSexoModel.test_factory_cria_valido) ... ok
test_str_retorna_nome (apps.interessados.tests.test_models.TestSexoModel.test_str_retorna_nome) ... ok
test_unique_constraint_violado (apps.interessados.tests.test_models.TestSexoModel.test_unique_constraint_violado) ... ok
test_criada_com_status_pendente (apps.interessados.tests.test_models.TestSolicitacaoExclusao.test_criada_com_status_pendente) ... ok
test_email_solicitante_opcional (apps.interessados.tests.test_models.TestSolicitacaoExclusao.test_email_solicitante_opcional) ... ok
test_nome_solicitante_obrigatorio (apps.interessados.tests.test_models.TestSolicitacaoExclusao.test_nome_solicitante_obrigatorio) ... ok
test_str_contem_status_e_nome (apps.interessados.tests.test_models.TestSolicitacaoExclusao.test_str_contem_status_e_nome) ... ok
test_todos_os_status_sao_validos (apps.interessados.tests.test_models.TestSolicitacaoExclusao.test_todos_os_status_sao_validos) ... ok

----------------------------------------------------------------------
Ran 38 tests in 14.695s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...



## apps.interessados.tests.test_views.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.interessados.tests.test_views -v 2         
Found 16 test(s).
Creating test database for alias 'default' ('test_bdmetareciclagem')...
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_nao_autenticado_redireciona_login (apps.interessados.tests.test_views.TestDashboardAutenticacao.test_nao_autenticado_redireciona_login) ... ok
test_usuario_inativo_redireciona_login (apps.interessados.tests.test_views.TestDashboardAutenticacao.test_usuario_inativo_redireciona_login)
Login via POST com usuario inativo nao autentica e redireciona. ... ok
test_cadastro_post_com_dados_completos (apps.interessados.tests.test_views.TestInteressadosViews.test_cadastro_post_com_dados_completos)
CPF valido: 111.222.333-96. ... ok
test_cadastro_rejeita_senha_fraca (apps.interessados.tests.test_views.TestInteressadosViews.test_cadastro_rejeita_senha_fraca) ... ok
test_cadastro_view_get (apps.interessados.tests.test_views.TestInteressadosViews.test_cadastro_view_get) ... ok
test_cadastro_view_post_valido (apps.interessados.tests.test_views.TestInteressadosViews.test_cadastro_view_post_valido) ... ok
test_dashboard_com_login (apps.interessados.tests.test_views.TestInteressadosViews.test_dashboard_com_login) ... ok
test_dashboard_requer_login (apps.interessados.tests.test_views.TestInteressadosViews.test_dashboard_requer_login) ... ok
test_login_nao_expoe_mensagem_diferenciada (apps.interessados.tests.test_views.TestInteressadosViews.test_login_nao_expoe_mensagem_diferenciada) ... ok
test_login_sql_injection (apps.interessados.tests.test_views.TestInteressadosViews.test_login_sql_injection) ... ok
test_login_view_valido (apps.interessados.tests.test_views.TestInteressadosViews.test_login_view_valido) ... ok
test_meus_dados_edicao_sem_nome_rejeita (apps.interessados.tests.test_views.TestInteressadosViews.test_meus_dados_edicao_sem_nome_rejeita) ... ok
test_meus_dados_edicao_valida (apps.interessados.tests.test_views.TestInteressadosViews.test_meus_dados_edicao_valida)
POST com dados minimos que o EdicaoInteressadoForm aceita. ... ok
test_meus_dados_view_get (apps.interessados.tests.test_views.TestInteressadosViews.test_meus_dados_view_get) ... ok
test_senha_recuperar_view (apps.interessados.tests.test_views.TestInteressadosViews.test_senha_recuperar_view) ... ok
test_portal_index (apps.interessados.tests.test_views.TestPortalViews.test_portal_index) ... ok

----------------------------------------------------------------------
Ran 16 tests in 13.566s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...



## apps.interessados.tests.test_admin.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.interessados.tests.test_admin -v 2
Found 39 test(s).
Creating test database for alias 'default' ('test_bdmetareciclagem')...
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_list_display (apps.interessados.tests.test_admin.TestFototipoAdmin.test_list_display) ... ok
test_search_fields (apps.interessados.tests.test_admin.TestFototipoAdmin.test_search_fields) ... ok
test_ativar_interessados (apps.interessados.tests.test_admin.TestInteressadoAdminActions.test_ativar_interessados) ... ok
test_desativar_interessados (apps.interessados.tests.test_admin.TestInteressadoAdminActions.test_desativar_interessados) ... ok
test_exportar_interessados_conteudo_tem_cabecalho (apps.interessados.tests.test_admin.TestInteressadoAdminActions.test_exportar_interessados_conteudo_tem_cabecalho) ... ok
test_exportar_interessados_retorna_csv (apps.interessados.tests.test_admin.TestInteressadoAdminActions.test_exportar_interessados_retorna_csv) ... ok
test_gerar_senha_provisoria_rejeita_multiplos (apps.interessados.tests.test_admin.TestInteressadoAdminActions.test_gerar_senha_provisoria_rejeita_multiplos) ... ok
test_gerar_senha_provisoria_um_interessado (apps.interessados.tests.test_admin.TestInteressadoAdminActions.test_gerar_senha_provisoria_um_interessado) ... ok
test_celular_formatado_11_digitos (apps.interessados.tests.test_admin.TestInteressadoAdminMetodos.test_celular_formatado_11_digitos) ... ok
test_celular_formatado_vazio (apps.interessados.tests.test_admin.TestInteressadoAdminMetodos.test_celular_formatado_vazio) ... ok
test_data_nascimento_formatada_com_data (apps.interessados.tests.test_admin.TestInteressadoAdminMetodos.test_data_nascimento_formatada_com_data) ... ok
test_data_nascimento_formatada_sem_data (apps.interessados.tests.test_admin.TestInteressadoAdminMetodos.test_data_nascimento_formatada_sem_data) ... ok
test_fototipo_display_com_fototipo (apps.interessados.tests.test_admin.TestInteressadoAdminMetodos.test_fototipo_display_com_fototipo) ... ok
test_fototipo_display_sem_fototipo (apps.interessados.tests.test_admin.TestInteressadoAdminMetodos.test_fototipo_display_sem_fototipo) ... ok
test_is_active_display_ativo (apps.interessados.tests.test_admin.TestInteressadoAdminMetodos.test_is_active_display_ativo) ... ok
test_is_active_display_inativo (apps.interessados.tests.test_admin.TestInteressadoAdminMetodos.test_is_active_display_inativo) ... ok
test_necessidades_especiais_display_false (apps.interessados.tests.test_admin.TestInteressadoAdminMetodos.test_necessidades_especiais_display_false) ... ok
test_necessidades_especiais_display_true (apps.interessados.tests.test_admin.TestInteressadoAdminMetodos.test_necessidades_especiais_display_true) ... ok
test_programa_social_display_false (apps.interessados.tests.test_admin.TestInteressadoAdminMetodos.test_programa_social_display_false) ... ok
test_programa_social_display_true (apps.interessados.tests.test_admin.TestInteressadoAdminMetodos.test_programa_social_display_true) ... ok
test_sexo_display_com_sexo (apps.interessados.tests.test_admin.TestInteressadoAdminMetodos.test_sexo_display_com_sexo) ... ok
test_sexo_display_sem_sexo (apps.interessados.tests.test_admin.TestInteressadoAdminMetodos.test_sexo_display_sem_sexo) ... ok
test_short_descriptions (apps.interessados.tests.test_admin.TestInteressadoAdminMetodos.test_short_descriptions) ... ok
test_telefone_formatado_10_digitos (apps.interessados.tests.test_admin.TestInteressadoAdminMetodos.test_telefone_formatado_10_digitos) ... ok
test_telefone_formatado_vazio (apps.interessados.tests.test_admin.TestInteressadoAdminMetodos.test_telefone_formatado_vazio) ... ok
test_save_model_com_senha_nova_aplica_set_password (apps.interessados.tests.test_admin.TestInteressadoAdminSaveModel.test_save_model_com_senha_nova_aplica_set_password) ... ok
test_get_interessado_retorna_nome (apps.interessados.tests.test_admin.TestPasswordResetTokenAdmin.test_get_interessado_retorna_nome) ... ok
test_get_status_expirado (apps.interessados.tests.test_admin.TestPasswordResetTokenAdmin.test_get_status_expirado) ... ok
test_get_status_usado (apps.interessados.tests.test_admin.TestPasswordResetTokenAdmin.test_get_status_usado) ... ok
test_get_status_valido (apps.interessados.tests.test_admin.TestPasswordResetTokenAdmin.test_get_status_valido) ... ok
test_has_add_permission_false (apps.interessados.tests.test_admin.TestPasswordResetTokenAdmin.test_has_add_permission_false) ... ok
test_has_change_permission_false (apps.interessados.tests.test_admin.TestPasswordResetTokenAdmin.test_has_change_permission_false) ... ok
test_has_delete_permission_normal_user_false (apps.interessados.tests.test_admin.TestPasswordResetTokenAdmin.test_has_delete_permission_normal_user_false) ... ok
test_has_delete_permission_superuser_true (apps.interessados.tests.test_admin.TestPasswordResetTokenAdmin.test_has_delete_permission_superuser_true) ... ok
test_limpar_todos_invalidos (apps.interessados.tests.test_admin.TestPasswordResetTokenAdmin.test_limpar_todos_invalidos) ... ok
test_limpar_tokens_expirados (apps.interessados.tests.test_admin.TestPasswordResetTokenAdmin.test_limpar_tokens_expirados) ... ok
test_limpar_tokens_usados (apps.interessados.tests.test_admin.TestPasswordResetTokenAdmin.test_limpar_tokens_usados) ... ok
test_list_display (apps.interessados.tests.test_admin.TestSexoAdmin.test_list_display) ... ok
test_search_fields (apps.interessados.tests.test_admin.TestSexoAdmin.test_search_fields) ... ok

----------------------------------------------------------------------
Ran 39 tests in 8.803s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...



## apps.interessados.tests.test_authentication.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.interessados.tests.test_authentication -v 2
Found 10 test(s).
Creating test database for alias 'default' ('test_bdmetareciclagem')...
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_autentica_com_cpf_e_senha_validos (apps.interessados.tests.test_authentication.TestInteressadoBackendAuthenticate.test_autentica_com_cpf_e_senha_validos) ... ok
test_autentica_com_cpf_inexistente_retorna_none (apps.interessados.tests.test_authentication.TestInteressadoBackendAuthenticate.test_autentica_com_cpf_inexistente_retorna_none) ... ok
test_autentica_com_cpf_none_retorna_none (apps.interessados.tests.test_authentication.TestInteressadoBackendAuthenticate.test_autentica_com_cpf_none_retorna_none) ... ok
test_autentica_com_senha_errada_retorna_none (apps.interessados.tests.test_authentication.TestInteressadoBackendAuthenticate.test_autentica_com_senha_errada_retorna_none) ... ok
test_autentica_com_senha_none_retorna_none (apps.interessados.tests.test_authentication.TestInteressadoBackendAuthenticate.test_autentica_com_senha_none_retorna_none) ... ok
test_autentica_interessado_inativo_retorna_none (apps.interessados.tests.test_authentication.TestInteressadoBackendAuthenticate.test_autentica_interessado_inativo_retorna_none) ... ok
test_autentica_sem_request_mas_com_cpf_valido (apps.interessados.tests.test_authentication.TestInteressadoBackendAuthenticate.test_autentica_sem_request_mas_com_cpf_valido) ... ok
test_get_user_com_id_inexistente_retorna_none (apps.interessados.tests.test_authentication.TestInteressadoBackendGetUser.test_get_user_com_id_inexistente_retorna_none) ... ok
test_get_user_com_id_valido_retorna_interessado (apps.interessados.tests.test_authentication.TestInteressadoBackendGetUser.test_get_user_com_id_valido_retorna_interessado) ... ok
test_get_user_interessado_inativo_retorna_none (apps.interessados.tests.test_authentication.TestInteressadoBackendGetUser.test_get_user_interessado_inativo_retorna_none) ... ok

----------------------------------------------------------------------
Ran 10 tests in 3.652s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...



## apps.interessados.tests.test_urls.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.interessados.tests.test_urls -v 2
Found 28 test(s).
Skipping setup of unused database(s): default.
System check identified no issues (0 silenced).
test_cadastro_path (apps.interessados.tests.test_urls.TestUrlsPath.test_cadastro_path) ... ok
test_dashboard_path (apps.interessados.tests.test_urls.TestUrlsPath.test_dashboard_path) ... ok
test_detalhes_path (apps.interessados.tests.test_urls.TestUrlsPath.test_detalhes_path) ... ok
test_exclusao_solicitada_path (apps.interessados.tests.test_urls.TestUrlsPath.test_exclusao_solicitada_path) ... ok
test_inscrever_evento_path (apps.interessados.tests.test_urls.TestUrlsPath.test_inscrever_evento_path) ... ok
test_login_path (apps.interessados.tests.test_urls.TestUrlsPath.test_login_path) ... ok
test_logout_path (apps.interessados.tests.test_urls.TestUrlsPath.test_logout_path) ... ok
test_meus_dados_path (apps.interessados.tests.test_urls.TestUrlsPath.test_meus_dados_path) ... ok
test_senha_recuperar_enviado_path (apps.interessados.tests.test_urls.TestUrlsPath.test_senha_recuperar_enviado_path) ... ok
test_senha_recuperar_path (apps.interessados.tests.test_urls.TestUrlsPath.test_senha_recuperar_path) ... ok
test_senha_redefinir_concluido_path (apps.interessados.tests.test_urls.TestUrlsPath.test_senha_redefinir_concluido_path) ... ok
test_senha_redefinir_path (apps.interessados.tests.test_urls.TestUrlsPath.test_senha_redefinir_path) ... ok
test_senha_sem_email_path (apps.interessados.tests.test_urls.TestUrlsPath.test_senha_sem_email_path) ... ok
test_solicitar_exclusao_path (apps.interessados.tests.test_urls.TestUrlsPath.test_solicitar_exclusao_path) ... ok
test_cadastro_url (apps.interessados.tests.test_urls.TestUrlsResolvem.test_cadastro_url) ... ok
test_dashboard_url (apps.interessados.tests.test_urls.TestUrlsResolvem.test_dashboard_url) ... ok
test_detalhes_url (apps.interessados.tests.test_urls.TestUrlsResolvem.test_detalhes_url) ... ok
test_exclusao_solicitada_url (apps.interessados.tests.test_urls.TestUrlsResolvem.test_exclusao_solicitada_url) ... ok
test_inscrever_evento_url (apps.interessados.tests.test_urls.TestUrlsResolvem.test_inscrever_evento_url) ... ok
test_login_url (apps.interessados.tests.test_urls.TestUrlsResolvem.test_login_url) ... ok
test_logout_url (apps.interessados.tests.test_urls.TestUrlsResolvem.test_logout_url) ... ok
test_meus_dados_url (apps.interessados.tests.test_urls.TestUrlsResolvem.test_meus_dados_url) ... ok
test_senha_recuperar_enviado_url (apps.interessados.tests.test_urls.TestUrlsResolvem.test_senha_recuperar_enviado_url) ... ok
test_senha_recuperar_url (apps.interessados.tests.test_urls.TestUrlsResolvem.test_senha_recuperar_url) ... ok
test_senha_redefinir_concluido_url (apps.interessados.tests.test_urls.TestUrlsResolvem.test_senha_redefinir_concluido_url) ... ok
test_senha_redefinir_url (apps.interessados.tests.test_urls.TestUrlsResolvem.test_senha_redefinir_url) ... ok
test_senha_sem_email_url (apps.interessados.tests.test_urls.TestUrlsResolvem.test_senha_sem_email_url) ... ok
test_solicitar_exclusao_url (apps.interessados.tests.test_urls.TestUrlsResolvem.test_solicitar_exclusao_url) ... ok

----------------------------------------------------------------------
Ran 28 tests in 0.016s

OK




##  apps.interessados.tests.test_utils.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.interessados.tests.test_utils -v 2
Found 7 test(s).
Skipping setup of unused database(s): default.
System check identified no issues (0 silenced).
test_timeout_padrao_nao_definido (apps.interessados.tests.test_utils.TestCustomEmailBackend.test_timeout_padrao_nao_definido) ... ok
test_timeout_personalizado (apps.interessados.tests.test_utils.TestCustomEmailBackend.test_timeout_personalizado) ... ok
test_herda_de_emailbackend (apps.interessados.tests.test_utils.TestCustomEmailBackendHeranca.test_herda_de_emailbackend) ... ok
test_com_ssl_certfile_mantem_verificacao (apps.interessados.tests.test_utils.TestCustomEmailBackendSSLContext.test_com_ssl_certfile_mantem_verificacao) ... ok
test_context_e_cached_property (apps.interessados.tests.test_utils.TestCustomEmailBackendSSLContext.test_context_e_cached_property) ... ok
test_sem_certificate_desabilita_verificacao (apps.interessados.tests.test_utils.TestCustomEmailBackendSSLContext.test_sem_certificate_desabilita_verificacao) ... ok
test_ssl_context_sem_cert_e_sem_keyfile (apps.interessados.tests.test_utils.TestCustomEmailBackendSSLContext.test_ssl_context_sem_cert_e_sem_keyfile) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.073s

OK



##  apps.interessados.tests.test_views_exclusao.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.interessados.tests.test_views_exclusao -v 2
Found 12 test(s).
Creating test database for alias 'default' ('test_bdmetareciclagem')...
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_get_com_login_retorna_200 (apps.interessados.tests.test_views_exclusao.TestExclusaoSolicitadaView.test_get_com_login_retorna_200) ... ok
test_sem_login_redirect_para_login (apps.interessados.tests.test_views_exclusao.TestExclusaoSolicitadaView.test_sem_login_redirect_para_login) ... ok
test_get_com_pendente_redirect_dashboard (apps.interessados.tests.test_views_exclusao.TestSolicitarExclusaoView.test_get_com_pendente_redirect_dashboard) ... ok
test_get_sem_pendente_retorna_200 (apps.interessados.tests.test_views_exclusao.TestSolicitarExclusaoView.test_get_sem_pendente_retorna_200) ... ok
test_interessado_inativo_logout_e_redirect (apps.interessados.tests.test_views_exclusao.TestSolicitarExclusaoView.test_interessado_inativo_logout_e_redirect) ... ok
test_post_com_pendente_nao_cria_nova (apps.interessados.tests.test_views_exclusao.TestSolicitarExclusaoView.test_post_com_pendente_nao_cria_nova) ... ok
test_post_confirmacao_invalida_mostra_erro (apps.interessados.tests.test_views_exclusao.TestSolicitarExclusaoView.test_post_confirmacao_invalida_mostra_erro) ... ok
test_post_confirmacao_valida_cria_solicitacao (apps.interessados.tests.test_views_exclusao.TestSolicitarExclusaoView.test_post_confirmacao_valida_cria_solicitacao) ... ok
test_post_confirmacao_valida_sem_motivo (apps.interessados.tests.test_views_exclusao.TestSolicitarExclusaoView.test_post_confirmacao_valida_sem_motivo) ... ok
test_post_confirmacao_vazia_mostra_erro (apps.interessados.tests.test_views_exclusao.TestSolicitarExclusaoView.test_post_confirmacao_vazia_mostra_erro) ... ok
test_post_sem_login_redirect_para_login (apps.interessados.tests.test_views_exclusao.TestSolicitarExclusaoView.test_post_sem_login_redirect_para_login) ... ok
test_sem_login_redirect_para_login (apps.interessados.tests.test_views_exclusao.TestSolicitarExclusaoView.test_sem_login_redirect_para_login) ... ok

----------------------------------------------------------------------
Ran 12 tests in 1.320s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...



##  apps.portal.tests.test_forms.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.portal.tests.test_forms -v 2
Found 11 test(s).
Creating test database for alias 'default' ('test_bdmetareciclagem')...
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_cpf_invalido_com_menos_de_11_digitos (apps.portal.tests.test_forms.TestConsultaPublicaForm.test_cpf_invalido_com_menos_de_11_digitos) ... ok
test_cpf_invalido_vazio (apps.portal.tests.test_forms.TestConsultaPublicaForm.test_cpf_invalido_vazio) ... ok
test_cpf_valido_com_formatacao (apps.portal.tests.test_forms.TestConsultaPublicaForm.test_cpf_valido_com_formatacao) ... ok
test_cpf_valido_sem_formatacao (apps.portal.tests.test_forms.TestConsultaPublicaForm.test_cpf_valido_sem_formatacao) ... ok
test_form_invalido_com_campos_vazios (apps.portal.tests.test_forms.TestLoginInteressadoForm.test_form_invalido_com_campos_vazios) ... ok
test_form_invalido_com_cpf_incorreto (apps.portal.tests.test_forms.TestLoginInteressadoForm.test_form_invalido_com_cpf_incorreto) ... ok
test_form_invalido_com_senha_incorreta (apps.portal.tests.test_forms.TestLoginInteressadoForm.test_form_invalido_com_senha_incorreta) ... ok
test_form_invalido_cpf_com_menos_de_11_digitos (apps.portal.tests.test_forms.TestLoginInteressadoForm.test_form_invalido_cpf_com_menos_de_11_digitos) ... ok
test_form_invalido_interessado_inativo (apps.portal.tests.test_forms.TestLoginInteressadoForm.test_form_invalido_interessado_inativo) ... ok
test_form_valido_com_cpf_e_senha_corretos (apps.portal.tests.test_forms.TestLoginInteressadoForm.test_form_valido_com_cpf_e_senha_corretos) ... ok
test_form_valido_com_cpf_formatado (apps.portal.tests.test_forms.TestLoginInteressadoForm.test_form_valido_com_cpf_formatado) ... ok

----------------------------------------------------------------------
Ran 11 tests in 2.661s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...



##  apps.portal.tests.test_urls.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.portal.tests.test_urls -v 2
Found 18 test(s).
Skipping setup of unused database(s): default.
System check identified no issues (0 silenced).
test_consulta_publica_path (apps.portal.tests.test_urls.TestUrlsPath.test_consulta_publica_path) ... ok
test_contato_path (apps.portal.tests.test_urls.TestUrlsPath.test_contato_path) ... ok
test_dashboard_path (apps.portal.tests.test_urls.TestUrlsPath.test_dashboard_path) ... ok
test_detalhes_evento_path (apps.portal.tests.test_urls.TestUrlsPath.test_detalhes_evento_path) ... ok
test_index_path (apps.portal.tests.test_urls.TestUrlsPath.test_index_path) ... ok
test_login_path (apps.portal.tests.test_urls.TestUrlsPath.test_login_path) ... ok
test_logout_path (apps.portal.tests.test_urls.TestUrlsPath.test_logout_path) ... ok
test_privacidade_path (apps.portal.tests.test_urls.TestUrlsPath.test_privacidade_path) ... ok
test_resultado_evento_path (apps.portal.tests.test_urls.TestUrlsPath.test_resultado_evento_path) ... ok
test_consulta_publica_url (apps.portal.tests.test_urls.TestUrlsResolvem.test_consulta_publica_url) ... ok
test_contato_url (apps.portal.tests.test_urls.TestUrlsResolvem.test_contato_url) ... ok
test_dashboard_url (apps.portal.tests.test_urls.TestUrlsResolvem.test_dashboard_url) ... ok
test_detalhes_evento_url (apps.portal.tests.test_urls.TestUrlsResolvem.test_detalhes_evento_url) ... ok
test_index_url (apps.portal.tests.test_urls.TestUrlsResolvem.test_index_url) ... ok
test_login_url (apps.portal.tests.test_urls.TestUrlsResolvem.test_login_url) ... ok
test_logout_url (apps.portal.tests.test_urls.TestUrlsResolvem.test_logout_url) ... ok
test_privacidade_url (apps.portal.tests.test_urls.TestUrlsResolvem.test_privacidade_url) ... ok
test_resultado_evento_url (apps.portal.tests.test_urls.TestUrlsResolvem.test_resultado_evento_url) ... ok

----------------------------------------------------------------------
Ran 18 tests in 0.014s

OK




##  apps.portal.tests.test_views.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.portal.tests.test_views -v 2
Found 26 test(s).
Creating test database for alias 'default' ('test_bdmetareciclagem')...
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_consulta_get_200 (apps.portal.tests.test_views.TestConsultaPublicaView.test_consulta_get_200) ... ok
test_consulta_post_cpf_invalido_mensagem (apps.portal.tests.test_views.TestConsultaPublicaView.test_consulta_post_cpf_invalido_mensagem) ... ok
test_consulta_post_cpf_valido_context (apps.portal.tests.test_views.TestConsultaPublicaView.test_consulta_post_cpf_valido_context) ... ok
test_consulta_post_vazio_form (apps.portal.tests.test_views.TestConsultaPublicaView.test_consulta_post_vazio_form) ... ok
test_contato_context (apps.portal.tests.test_views.TestContatoView.test_contato_context) ... ok
test_contato_get_200 (apps.portal.tests.test_views.TestContatoView.test_contato_get_200) ... ok
test_dashboard_sem_sessao_redirect_302 (apps.portal.tests.test_views.TestDashboardView.test_dashboard_sem_sessao_redirect_302) ... ok
test_dashboard_sessao_invalida_redirect_302 (apps.portal.tests.test_views.TestDashboardView.test_dashboard_sessao_invalida_redirect_302) ... ok
test_dashboard_sessao_valida_nao_302 (apps.portal.tests.test_views.TestDashboardView.test_dashboard_sessao_valida_nao_302) ... ok
test_dashboard_sessao_valida_status_ok (apps.portal.tests.test_views.TestDashboardView.test_dashboard_sessao_valida_status_ok) ... ok
test_detalhes_com_sessao_status_valido (apps.portal.tests.test_views.TestDetalhesEventoView.test_detalhes_com_sessao_status_valido) ... ok
test_detalhes_sem_sessao_redirect (apps.portal.tests.test_views.TestDetalhesEventoView.test_detalhes_sem_sessao_redirect) ... ok
test_index_context_eventos (apps.portal.tests.test_views.TestIndexView.test_index_context_eventos) ... ok
test_index_get_200 (apps.portal.tests.test_views.TestIndexView.test_index_get_200) ... ok
test_index_total_eventos_int (apps.portal.tests.test_views.TestIndexView.test_index_total_eventos_int) ... ok
test_login_com_sessao_redirect_302 (apps.portal.tests.test_views.TestLoginInteressadoView.test_login_com_sessao_redirect_302) ... ok
test_login_post_valido_cria_sessao_id (apps.portal.tests.test_views.TestLoginInteressadoView.test_login_post_valido_cria_sessao_id) ... ok
test_login_post_valido_redirect_302 (apps.portal.tests.test_views.TestLoginInteressadoView.test_login_post_valido_redirect_302) ... ok
test_login_post_valido_sessao_cpf_mascarado (apps.portal.tests.test_views.TestLoginInteressadoView.test_login_post_valido_sessao_cpf_mascarado) ... ok
test_login_post_valido_sessao_nome (apps.portal.tests.test_views.TestLoginInteressadoView.test_login_post_valido_sessao_nome) ... ok
test_logout_limpa_sessao (apps.portal.tests.test_views.TestLogoutInteressadoView.test_logout_limpa_sessao) ... ok
test_logout_redirect_302 (apps.portal.tests.test_views.TestLogoutInteressadoView.test_logout_redirect_302) ... ok
test_politica_content_existe (apps.portal.tests.test_views.TestPoliticaPrivacidadeView.test_politica_content_existe) ... ok
test_politica_get_200 (apps.portal.tests.test_views.TestPoliticaPrivacidadeView.test_politica_get_200) ... ok
test_resultado_get_nao_erro_500 (apps.portal.tests.test_views.TestResultadoEventoView.test_resultado_get_nao_erro_500) ... ok
test_resultado_get_status_valido (apps.portal.tests.test_views.TestResultadoEventoView.test_resultado_get_status_valido) ... ok

----------------------------------------------------------------------
Ran 26 tests in 5.094s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...




##  apps.scripts_admin.management.commands.tests.test_classificar_evento.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.scripts_admin.management.commands.tests.test_classificar_evento -v 2
Found 32 test(s).
Creating test database for alias 'default' ('test_bdmetareciclagem')...
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_criterio_ordenacao_nao_soma_pontos (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoCriterioOrdenacaoTest.test_criterio_ordenacao_nao_soma_pontos) ... ok
test_desempate_idoso_prioriza_mais_velho (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoDesempatePorIdadeTest.test_desempate_idoso_prioriza_mais_velho) ... ok
test_desempate_jovem_prioriza_mais_novo (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoDesempatePorIdadeTest.test_desempate_jovem_prioriza_mais_novo) ... ok
test_evento_inexistente_exibe_erro (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoEventoNaoEncontradoTest.test_evento_inexistente_exibe_erro) ... ok
test_segunda_execucao_nao_duplica_classificacao (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoIdempotenciaTest.test_segunda_execucao_nao_duplica_classificacao) ... C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Classificacao.processado_em received a naive datetime (2026-06-02 00:00:00) while time zone support is active.
  warnings.warn(
ok
test_segunda_execucao_nao_duplica_criterios_atendidos (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoIdempotenciaTest.test_segunda_execucao_nao_duplica_criterios_atendidos) ... ok
test_criterio_cota_racial_indigena (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoPontuacaoTest.test_criterio_cota_racial_indigena) ... ok
test_criterio_cota_racial_nao_atribuido_para_branca (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoPontuacaoTest.test_criterio_cota_racial_nao_atribuido_para_branca) ... ok
test_criterio_cota_racial_parda (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoPontuacaoTest.test_criterio_cota_racial_parda) ... ok
test_criterio_cota_racial_preta (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoPontuacaoTest.test_criterio_cota_racial_preta) ... ok
test_criterio_cota_racial_sem_fototipo (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoPontuacaoTest.test_criterio_cota_racial_sem_fototipo) ... ok
test_criterio_escolaridade_fundamental_incompleto (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoPontuacaoTest.test_criterio_escolaridade_fundamental_incompleto) ... ok
test_criterio_escolaridade_medio_completo (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoPontuacaoTest.test_criterio_escolaridade_medio_completo) ... ok
test_criterio_idoso_atribuido_50_anos (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoPontuacaoTest.test_criterio_idoso_atribuido_50_anos) ... ok
test_criterio_idoso_nao_atribuido_para_49_anos (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoPontuacaoTest.test_criterio_idoso_nao_atribuido_para_49_anos) ... ok
test_criterio_jovem_atribuido_16_anos (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoPontuacaoTest.test_criterio_jovem_atribuido_16_anos) ... ok
test_criterio_jovem_atribuido_24_anos (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoPontuacaoTest.test_criterio_jovem_atribuido_24_anos) ... ok
test_criterio_jovem_nao_atribuido_para_adulto (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoPontuacaoTest.test_criterio_jovem_nao_atribuido_para_adulto) ... ok
test_criterio_nis_atribuido (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoPontuacaoTest.test_criterio_nis_atribuido) ... ok
test_criterio_nis_nao_atribuido_sem_nis (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoPontuacaoTest.test_criterio_nis_nao_atribuido_sem_nis) ... ok
test_criterio_pcd_atribuido (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoPontuacaoTest.test_criterio_pcd_atribuido) ... ok
test_criterio_pcd_nao_atribuido_quando_sem_deficiencia (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoPontuacaoTest.test_criterio_pcd_nao_atribuido_quando_sem_deficiencia) ... ok
test_multiplos_criterios_somam_pontos (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoPontuacaoTest.test_multiplos_criterios_somam_pontos) ... ok
test_fora_das_vagas_esta_em_lista_espera (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoPosicaoTest.test_fora_das_vagas_esta_em_lista_espera) ... ok
test_posicoes_sao_unicas (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoPosicaoTest.test_posicoes_sao_unicas) ... ok
test_primeiro_colocado_esta_classificado (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoPosicaoTest.test_primeiro_colocado_esta_classificado) ... ok
test_total_de_classificacoes_igual_ao_total_de_inscricoes (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoPosicaoTest.test_total_de_classificacoes_igual_ao_total_de_inscricoes) ... ok
test_sem_criterios_exibe_aviso (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoSemCriteriosTest.test_sem_criterios_exibe_aviso) ... ok
test_sem_inscricoes_confirmadas_exibe_aviso (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoSemInscricoesTest.test_sem_inscricoes_confirmadas_exibe_aviso) ... ok
test_sem_inscricoes_nao_cria_classificacao (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoSemInscricoesTest.test_sem_inscricoes_nao_cria_classificacao) ... ok
test_inscricao_confirmada_e_processada (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoStatusInscricaoTest.test_inscricao_confirmada_e_processada) ... ok
test_inscricao_pendente_e_ignorada (apps.scripts_admin.management.commands.tests.test_classificar_evento.ClassificarEventoStatusInscricaoTest.test_inscricao_pendente_e_ignorada) ... ok

----------------------------------------------------------------------
Ran 32 tests in 1.127s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...


##  apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais -v 2
Found 53 test(s).
Creating test database for alias 'default' ('test_bdmetareciclagem')...
Operations to perform:
  Synchronize unmigrated apps: csp, django_extensions, messages, scripts_admin, staticfiles
  Apply all migrations: academico, accounts, admin, auth, axes, contenttypes, eventos, interessados, selecao, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying interessados.0001_initial... OK
  Applying eventos.0001_initial... OK
  Applying selecao.0001_initial... OK
  Applying interessados.0002_interessado_cep_interessado_raca_cor... OK
  Applying interessados.0003_remove_interessado_raca_cor... OK
  Applying interessados.0004_passwordresettoken... OK
  Applying interessados.0005_interessado_must_change_password... OK
  Applying academico.0001_initial... OK
  Applying academico.0002_matricula_academico_m_inscric_af84a1_idx... OK
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_usuario_must_change_password... OK
  Applying accounts.0003_alter_usuario_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying axes.0001_initial... OK
  Applying axes.0002_auto_20151217_2044... OK
  Applying axes.0003_auto_20160322_0929... OK
  Applying axes.0004_auto_20181024_1538... OK
  Applying axes.0005_remove_accessattempt_trusted... OK
  Applying axes.0006_remove_accesslog_trusted... OK
  Applying axes.0007_alter_accessattempt_unique_together... OK
  Applying axes.0008_accessfailurelog... OK
  Applying axes.0009_add_session_hash... OK
  Applying axes.0010_accessattemptexpiration... OK
  Applying interessados.0006_alter_interessado_email... OK
  Applying interessados.0007_alter_interessado_cpf_alter_interessado_num_nis... OK
  Applying interessados.0008_interessado_cpf_hash... OK
  Applying interessados.0009_interessado_cpf_hash_unique... OK
  Applying interessados.0010_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0011_alter_interessado_consentimento_lgpd_and_more... OK
  Applying interessados.0012_alter_interessado_cpf_alter_sexo_nome... OK
  Applying selecao.0002_alter_classificacao_pontuacao_total_and_more... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_comando_executa_sem_erro (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisComandoTest.test_comando_executa_sem_erro) ... ok
test_comando_nao_vazio (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisComandoTest.test_comando_nao_vazio) ... ok
test_comando_retorna_string (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisComandoTest.test_comando_retorna_string) ... ok
test_criterio_cota_racial (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisCriteriosTest.test_criterio_cota_racial) ... ok
test_criterio_ensino_fundamental (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisCriteriosTest.test_criterio_ensino_fundamental) ... ok
test_criterio_idoso (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisCriteriosTest.test_criterio_idoso) ... ok
test_criterio_jovem (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisCriteriosTest.test_criterio_jovem) ... ok
test_criterio_pcd (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisCriteriosTest.test_criterio_pcd) ... ok
test_criterio_programa_social (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisCriteriosTest.test_criterio_programa_social) ... ok
test_criterio_renda_baixa (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisCriteriosTest.test_criterio_renda_baixa) ... ok
test_fototipo_amarela (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisFototipesTest.test_fototipo_amarela) ... ok
test_fototipo_branca (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisFototipesTest.test_fototipo_branca) ... ok
test_fototipo_indigena (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisFototipesTest.test_fototipo_indigena) ... ok
test_fototipo_parda (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisFototipesTest.test_fototipo_parda) ... ok
test_fototipo_preta (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisFototipesTest.test_fototipo_preta) ... ok
test_total_fototipos (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisFototipesTest.test_total_fototipos) ... ok
test_execucao_dupla_nao_duplica_dados (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisIdempotenciaTest.test_execucao_dupla_nao_duplica_dados) ... ok
test_execucao_tripla_nao_duplica_dados (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisIdempotenciaTest.test_execucao_tripla_nao_duplica_dados) ... ok
test_contagem_total_registros (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisIntegracaoTest.test_contagem_total_registros) ... ok
test_integridade_dados (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisIntegracaoTest.test_integridade_dados) ... ok
test_todos_modelos_populados (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisIntegracaoTest.test_todos_modelos_populados) ... ok
test_saida_contem_nome_comando (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisSaidaTest.test_saida_contem_nome_comando) ... ok
test_saida_contem_sucesso (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisSaidaTest.test_saida_contem_sucesso) ... ok
test_saida_nao_contem_ansi (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisSaidaTest.test_saida_nao_contem_ansi) ... ok
test_sexo_feminino (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisSexoTest.test_sexo_feminino) ... ok
test_sexo_masculino (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisSexoTest.test_sexo_masculino) ... ok
test_sexo_nao_informar (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisSexoTest.test_sexo_nao_informar) ... ok
test_sexo_outro (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisSexoTest.test_sexo_outro) ... ok
test_total_sexo (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisSexoTest.test_total_sexo) ... ok
test_status_cancelado (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusEventosTest.test_status_cancelado) ... ok
test_status_em_andamento (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusEventosTest.test_status_em_andamento) ... ok
test_status_em_classificacao (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusEventosTest.test_status_em_classificacao) ... ok
test_status_finalizado (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusEventosTest.test_status_finalizado) ... ok
test_status_inscricoes_abertas (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusEventosTest.test_status_inscricoes_abertas) ... ok
test_status_inscricoes_encerradas (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusEventosTest.test_status_inscricoes_encerradas) ... ok
test_status_planejamento (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusEventosTest.test_status_planejamento) ... ok
test_status_resultado_divulgado (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusEventosTest.test_status_resultado_divulgado) ... ok
test_total_status_eventos (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusEventosTest.test_total_status_eventos) ... ok
test_status_cancelada (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusInscricoesTest.test_status_cancelada) ... ok
test_status_classificado (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusInscricoesTest.test_status_classificado) ... ok
test_status_confirmada (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusInscricoesTest.test_status_confirmada) ... ok
test_status_desistente (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusInscricoesTest.test_status_desistente) ... ok
test_status_expirada (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusInscricoesTest.test_status_expirada) ... ok
test_status_lista_espera (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusInscricoesTest.test_status_lista_espera) ... ok
test_status_nao_localizado (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusInscricoesTest.test_status_nao_localizado) ... ok
test_status_pendente (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusInscricoesTest.test_status_pendente) ... ok
test_total_status_inscricoes (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusInscricoesTest.test_total_status_inscricoes) ... ok
test_status_ativa (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusMatriculasTest.test_status_ativa) ... ok
test_status_cancelada (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusMatriculasTest.test_status_cancelada) ... ok
test_status_concluida (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusMatriculasTest.test_status_concluida) ... ok
test_status_pendente (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusMatriculasTest.test_status_pendente) ... ok
test_status_trancada (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusMatriculasTest.test_status_trancada) ... ok
test_total_status_matriculas (apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.PopularDadosIniciaisStatusMatriculasTest.test_total_status_matriculas) ... ok

----------------------------------------------------------------------
Ran 53 tests in 2.274s

OK
Destroying test database for alias 'default' ('test_bdmetareciclagem')...



##   python manage.py test

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python manage.py test
Found 589 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_inicio_inscricao received a naive datetime (2026-06-02 00:00:00) while time zone support is active.
  warnings.warn(
C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_fim_inscricao received a naive datetime (2026-07-02 00:00:00) while time zone support is active.
  warnings.warn(
...........C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_fim_inscricao received a naive datetime (2026-06-02 00:00:00) while time zone support is active.
  warnings.warn(
.................................................................AXES: New login failure by {username: "********************", ip_address: "********************", user_agent: "<unknown>", path_info: "/staff/login/"}. Created new record in the database.
.AXES: New login failure by {username: "********************", ip_address: "********************", user_agent: "<unknown>", path_info: "/staff/login/"}. Created new record in the database.
..............................C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Inscricao.data_inscricao received a naive datetime (2026-05-03 00:00:00) while time zone support is active.
  warnings.warn(
...........................................C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_inicio_inscricao received a naive datetime (2026-06-01 00:00:00) while time zone support is active.
  warnings.warn(
C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_fim_inscricao received a naive datetime (2026-06-03 00:00:00) while time zone support is active.
  warnings.warn(
C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_inicio_inscricao received a naive datetime (2026-05-03 00:00:00) while time zone support is active.
  warnings.warn(
C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_fim_inscricao received a naive datetime (2026-05-13 00:00:00) while time zone support is active.
  warnings.warn(
......C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_inicio_inscricao received a naive datetime (2026-05-23 00:00:00) while time zone support is active.
  warnings.warn(
C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_fim_inscricao received a naive datetime (2026-06-01 00:00:00) while time zone support is active.
  warnings.warn(
..C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_inicio_inscricao received a naive datetime (2026-05-13 00:00:00) while time zone support is active.
  warnings.warn(
C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_fim_inscricao received a naive datetime (2026-05-23 00:00:00) while time zone support is active.
  warnings.warn(
......................................................................................................................................................................................................................................C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Classificacao.processado_em received a naive datetime (2026-06-02 00:00:00) while time zone support is active.
  warnings.warn(
.........................................................................................................................................................................................................
----------------------------------------------------------------------
Ran 589 tests in 190.592s

OK
Destroying test database for alias 'default'...




##  coverage 

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta>    pip install coverage                                                                   
>>    coverage run --source='.' manage.py test
>>    coverage report
Requirement already satisfied: coverage in C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages (7.11.0)
Found 589 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_inicio_inscricao received a naive datetime (2026-06-02 00:00:00) while time zone support is active.
  warnings.warn(
c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_fim_inscricao received a naive datetime (2026-07-02 00:00:00) while time zone support is active.
  warnings.warn(
...........c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_fim_inscricao received a naive datetime (2026-06-02 00:00:00) while time zone support is active.
  warnings.warn(
.................................................................AXES: New login failure by {username: "********************", ip_address: "********************", user_agent: "<unknown>", path_info: "/staff/login/"}. Created new record in the database.
.AXES: New login failure by {username: "********************", ip_address: "********************", user_agent: "<unknown>", path_info: "/staff/login/"}. Created new record in the database.
..............................c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Inscricao.data_inscricao received a naive datetime (2026-05-03 00:00:00) while time zone support is active.
  warnings.warn(
...........................................c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_inicio_inscricao received a naive datetime (2026-06-01 00:00:00) while time zone support is active.
  warnings.warn(
c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_fim_inscricao received a naive datetime (2026-06-03 00:00:00) while time zone support is active.
  warnings.warn(
c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_inicio_inscricao received a naive datetime (2026-05-03 00:00:00) while time zone support is active.
  warnings.warn(
c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_fim_inscricao received a naive datetime (2026-05-13 00:00:00) while time zone support is active.
  warnings.warn(
......c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_inicio_inscricao received a naive datetime (2026-05-23 00:00:00) while time zone support is active.
  warnings.warn(
c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_fim_inscricao received a naive datetime (2026-06-01 00:00:00) while time zone support is active.
  warnings.warn(
..c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_inicio_inscricao received a naive datetime (2026-05-13 00:00:00) while time zone support is active.
  warnings.warn(
c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Evento.data_fim_inscricao received a naive datetime (2026-05-23 00:00:00) while time zone support is active.
  warnings.warn(
......................................................................................................................................................................................................................................c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1612: RuntimeWarning: DateTimeField Classificacao.processado_em received a naive datetime (2026-06-02 00:00:00) while time zone support is active.
  warnings.warn(
.........................................................................................................................................................................................................
----------------------------------------------------------------------
Ran 589 tests in 193.565s

OK
Destroying test database for alias 'default'...
Name                                                                    Stmts   Miss  Cover
-------------------------------------------------------------------------------------------
apps\__init__.py                                                            0      0   100%
apps\academico\__init__.py                                                  0      0   100%
apps\academico\admin.py                                                   316    197    38%
apps\academico\apps.py                                                      5      0   100%
apps\academico\certificado.py                                             136      3    98%
apps\academico\models.py                                                  110     34    69%
apps\academico\services.py                                                134     75    44%
apps\academico\urls.py                                                      5      0   100%
apps\academico\views.py                                                    63      0   100%
apps\accounts\__init__.py                                                   0      0   100%
apps\accounts\admin.py                                                     52      0   100%
apps\accounts\apps.py                                                       5      0   100%
apps\accounts\forms.py                                                      5      5     0%
apps\accounts\middleware.py                                                20      0   100%
apps\accounts\models.py                                                    22      1    95%
apps\accounts\urls.py                                                       5      0   100%
apps\accounts\views.py                                                     47     20    57%
apps\accounts\views_exclusao.py                                            77      2    97%
apps\dashboard\__init__.py                                                  0      0   100%
apps\dashboard\admin.py                                                     0      0   100%
apps\dashboard\apps.py                                                      4      0   100%
apps\dashboard\models.py                                                    1      0   100%
apps\dashboard\utils_pdf.py                                               373     82    78%
apps\dashboard\views.py                                                   216      8    96%
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212     89    58%
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51      3    94%
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122     18    85%
apps\eventos\views.py                                                       1      1     0%
apps\interessados\__init__.py                                               0      0   100%
apps\interessados\admin.py                                                218     20    91%
apps\interessados\apps.py                                                   5      0   100%
apps\interessados\authentication.py                                        25      0   100%
apps\interessados\forms.py                                                157      7    96%
apps\interessados\management\__init__.py                                    0      0   100%
apps\interessados\management\commands\__init__.py                           0      0   100%
apps\interessados\management\commands\criptografar_cpfs.py                 22     22     0%
apps\interessados\management\commands\limpar_tokens.py                     59     59     0%
apps\interessados\management\commands\popular_cpf_hash.py                  22     22     0%
apps\interessados\models.py                                               139      9    94%
apps\interessados\urls.py                                                   5      0   100%
apps\interessados\utils.py                                                 14      0   100%
apps\interessados\views.py                                                202    103    49%
apps\interessados\views_exclusao.py                                        29      3    90%
apps\portal\__init__.py                                                     1      0   100%
apps\portal\admin.py                                                        1      0   100%
apps\portal\apps.py                                                         5      0   100%
apps\portal\forms.py                                                       34      0   100%
apps\portal\models.py                                                       1      0   100%
apps\portal\urls.py                                                         4      0   100%
apps\portal\views.py                                                       99     11    89%
apps\scripts_admin\__init__.py                                              0      0   100%
apps\scripts_admin\management\__init__.py                                   0      0   100%
apps\scripts_admin\management\commands\__init__.py                          0      0   100%
apps\scripts_admin\management\commands\classificar_evento.py              133      9    93%
apps\scripts_admin\management\commands\configurar_criterios_evento.py      57     57     0%
apps\scripts_admin\management\commands\popular_criterios.py                21     21     0%
apps\scripts_admin\management\commands\popular_dados_iniciais.py           66      0   100%
apps\selecao\__init__.py                                                    0      0   100%
apps\selecao\admin.py                                                     275    158    43%
apps\selecao\apps.py                                                        5      0   100%
apps\selecao\management\__init__.py                                         0      0   100%
apps\selecao\management\commands\__init__.py                                0      0   100%
apps\selecao\models.py                                                     71      1    99%
apps\selecao\reports.py                                                   301    252    16%
apps\selecao\services.py                                                  125     28    78%
apps\selecao\validators.py                                                105     34    68%
apps\selecao\views.py                                                       1      1     0%
config\__init__.py                                                          0      0   100%
config\asgi.py                                                              4      4     0%
config\settings.py                                                         54      9    83%
config\urls.py                                                             14      2    86%
config\wsgi.py                                                              4      4     0%
-------------------------------------------------------------------------------------------
TOTAL                                                                    4265   1374    68%




##  apps/eventos/tests/test_admin.py em 09/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> pytest apps/eventos/tests/test_admin.py -v
========================================================== test session starts ===========================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 30 items                                                                                                                        

apps/eventos/tests/test_admin.py::TestEventoAdminConfig::test_list_display PASSED                                                   [  3%]
apps/eventos/tests/test_admin.py::TestEventoAdminConfig::test_list_filter PASSED                                                    [  6%]
apps/eventos/tests/test_admin.py::TestEventoAdminConfig::test_search_fields PASSED                                                  [ 10%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_changelist_carrega PASSED                                         [ 13%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_busca_por_nome PASSED                                             [ 16%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_filtrar_por_status PASSED                                         [ 20%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_paginacao PASSED                                                  [ 23%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_busca_vazia PASSED                                                [ 26%]
apps/eventos/tests/test_admin.py::TestStatusAdminChangeList::test_changelist_carrega PASSED                                         [ 30%]
apps/eventos/tests/test_admin.py::TestStatusAdminChangeList::test_busca_por_nome PASSED                                             [ 33%]
apps/eventos/tests/test_admin.py::TestTurmaAdminChangeList::test_changelist_carrega PASSED                                          [ 36%]
apps/eventos/tests/test_admin.py::TestTurmaAdminChangeList::test_busca_por_nome PASSED                                              [ 40%]
apps/eventos/tests/test_admin.py::TestEventoAdminViews::test_add_view PASSED                                                        [ 43%]
apps/eventos/tests/test_admin.py::TestEventoAdminViews::test_change_view PASSED                                                     [ 46%]
apps/eventos/tests/test_admin.py::TestEventoAdminViews::test_delete_view PASSED                                                     [ 50%]
apps/eventos/tests/test_admin.py::TestStatusAdminViews::test_add_view PASSED                                                        [ 53%]
apps/eventos/tests/test_admin.py::TestStatusAdminViews::test_change_view PASSED                                                     [ 56%]
apps/eventos/tests/test_admin.py::TestStatusAdminViews::test_delete_view PASSED                                                     [ 60%]
apps/eventos/tests/test_admin.py::TestTurmaAdminViews::test_add_view PASSED                                                         [ 63%]
apps/eventos/tests/test_admin.py::TestTurmaAdminViews::test_change_view PASSED                                                      [ 66%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_status_colorido PASSED                                               [ 70%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_vagas_inscritos_sem_inscricoes PASSED                                [ 73%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_vagas_inscritos_com_inscricoes PASSED                                [ 76%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_data_inicio_inscricao_formatada PASSED                               [ 80%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_data_fim_inscricao_formatada PASSED                                  [ 83%]
apps/eventos/tests/test_admin.py::TestEventoAdminInlines::test_exibe_inline_criterios PASSED                                        [ 86%]
apps/eventos/tests/test_admin.py::TestEventoAdminInlines::test_exibe_inline_turmas PASSED                                           [ 90%]
apps/eventos/tests/test_admin.py::TestEventoAdminInlines::test_change_view_carrega_com_inlines PASSED                               [ 93%]
apps/eventos/tests/test_admin.py::TestHorarioAdminChangeList::test_changelist_carrega PASSED                                        [ 96%]
apps/eventos/tests/test_admin.py::TestHorarioAdminChangeList::test_filtro_dia_semana PASSED                                         [100%]

---------- coverage: platform win32, python 3.13.2-final-0 -----------
Name                                                                    Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------------------
apps\__init__.py                                                            0      0   100%
apps\academico\__init__.py                                                  0      0   100%
apps\academico\admin.py                                                   320    248    22%   64-70, 124, 129, 200, 205, 211-216, 225-266, 270-276, 284-440, 450-613, 623-653, 663-671, 678, 681
apps\academico\apps.py                                                      5      0   100%
apps\academico\certificado.py                                             136    118    13%   24-37, 43-67, 72-79, 83-104, 108-116, 120-163, 167-208, 212-254
apps\academico\models.py                                                  110     51    54%   45, 122, 128-154, 167-176, 191-214, 282-283, 300-316, 330-342
apps\academico\services.py                                                136    136     0%   8-402
apps\academico\urls.py                                                      5      0   100%
apps\academico\views.py                                                    63     45    29%   31-52, 61-77, 87-124
apps\accounts\__init__.py                                                   0      0   100%
apps\accounts\admin.py                                                     52     16    69%   48-63, 149-169
apps\accounts\apps.py                                                       5      0   100%
apps\accounts\forms.py                                                      5      5     0%   8-27
apps\accounts\middleware.py                                                20      9    55%   66-81
apps\accounts\models.py                                                    22      4    82%   103-106
apps\accounts\urls.py                                                       5      0   100%
apps\accounts\views.py                                                     47     38    19%   26-52, 60-62, 83-114
apps\accounts\views_exclusao.py                                            77     66    14%   19, 25-33, 43-83, 94-125
apps\dashboard\__init__.py                                                  0      0   100%
apps\dashboard\admin.py                                                     0      0   100%
apps\dashboard\apps.py                                                      4      0   100%
apps\dashboard\models.py                                                    1      0   100%
apps\dashboard\utils_pdf.py                                               373    373     0%   9-751
apps\dashboard\views.py                                                   216    193    11%   23-66, 72-130, 136-319, 325-381, 386-407, 417-552, 558-613, 619-651, 657-690
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212     89    58%   67, 111-114, 181, 196, 201-204, 223, 234, 245, 256, 269-358, 371-415, 430-519
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51     23    55%   25, 39, 67-81, 87-95, 101-112
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122     25    80%   104-106, 130-132, 135-137, 140-142, 145-147, 150-152, 155-160, 201, 206
apps\eventos\views.py                                                       1      1     0%   1
apps\interessados\__init__.py                                               0      0   100%
apps\interessados\admin.py                                                218    117    46%   178-183, 188, 193-194, 201-207, 216-222, 231-243, 248-260, 265-269, 280-282, 296-316, 329-330, 337-338, 347-431, 475, 480-481, 485-500, 509, 514, 523-527, 535-538, 546-552
apps\interessados\apps.py                                                   5      0   100%
apps\interessados\authentication.py                                        25     25     0%   9-73
apps\interessados\forms.py                                                157    106    32%   167-171, 179-213, 220-230, 234-235, 239-243, 247, 251, 255, 259, 263, 267, 271, 275-280, 287-302, 335-358, 392-396, 401-402, 406-410, 414, 418, 422, 426, 430, 434, 438, 445-453
apps\interessados\management\__init__.py                                    0      0   100%
apps\interessados\management\commands\__init__.py                           0      0   100%
apps\interessados\management\commands\criptografar_cpfs.py                 22     22     0%   11-47
apps\interessados\management\commands\limpar_tokens.py                     59     59     0%   13-155
apps\interessados\management\commands\popular_cpf_hash.py                  22     22     0%   9-40
apps\interessados\models.py                                               139     18    87%   22, 29, 41, 135, 138, 141, 144, 147, 151, 155, 158, 162, 166, 172, 188, 191-192, 260
apps\interessados\urls.py                                                   5      0   100%
apps\interessados\utils.py                                                 14     14     0%   10-38
apps\interessados\views.py                                                202    167    17%   49-67, 81-107, 113-115, 129-181, 194-216, 232-250, 266-323, 342-414, 422, 430-472, 477, 482, 496-519
apps\interessados\views_exclusao.py                                        29     20    31%   22-67, 76
apps\portal\__init__.py                                                     1      0   100%
apps\portal\admin.py                                                        1      0   100%
apps\portal\apps.py                                                         5      0   100%
apps\portal\forms.py                                                       34     24    29%   45-51, 55-76, 98-104
apps\portal\models.py                                                       1      0   100%
apps\portal\urls.py                                                         4      0   100%
apps\portal\views.py                                                       99     79    20%   30-39, 45-74, 79-82, 87-116, 122-163, 168-189, 196-220, 225-242, 247
apps\scripts_admin\__init__.py                                              0      0   100%
apps\scripts_admin\management\__init__.py                                   0      0   100%
apps\scripts_admin\management\commands\__init__.py                          0      0   100%
apps\scripts_admin\management\commands\classificar_evento.py              133    133     0%   8-291
apps\scripts_admin\management\commands\configurar_criterios_evento.py      57     57     0%   5-91
apps\scripts_admin\management\commands\popular_criterios.py                21     21     0%   4-117
apps\scripts_admin\management\commands\popular_dados_iniciais.py           66     66     0%   8-234
apps\selecao\__init__.py                                                    0      0   100%
apps\selecao\admin.py                                                     275    158    43%   66-72, 87, 110-115, 152, 223, 233, 240-241, 247, 254-255, 266-275, 293-456, 466-503, 507-544, 552, 558, 564, 570, 580, 586, 592, 598, 661, 667
apps\selecao\apps.py                                                        5      0   100%
apps\selecao\management\__init__.py                                         0      0   100%
apps\selecao\management\commands\__init__.py                                0      0   100%
apps\selecao\models.py                                                     71     15    79%   38, 74, 124-137, 145-146, 155, 188
apps\selecao\reports.py                                                   301    270    10%   27-31, 35-115, 126-132, 140-146, 151-163, 179-286, 302-420, 440-565, 580-711
apps\selecao\services.py                                                  125    125     0%   28-443
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4195   3064    27%
Coverage HTML written to dir htmlcov


========================================================== 30 passed in 16.21s ===========================================================



##  apps/eventos/tests/test_models_evento_expanded.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> pytest apps/eventos/tests/test_models_evento_expanded.py -v
=========================================================================== test session starts ===========================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 15 items                                                                                                                                                         

apps/eventos/tests/test_models_evento_expanded.py::TestEventoCreation::test_criar_evento PASSED                                                                      [  6%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoCreation::test_str_evento PASSED                                                                        [ 13%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoCreation::test_defaults_evento PASSED                                                                   [ 20%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoCreation::test_status_evento PASSED                                                                     [ 26%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoCreation::test_multiplos_eventos PASSED                                                                 [ 33%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoDatas::test_fim_inscricao_antes_inicio PASSED                                                  [ 40%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoDatas::test_fim_evento_antes_inicio PASSED                                                     [ 46%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoDatas::test_datas_validas PASSED                                                               [ 53%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoDatas::test_datas_iguais PASSED                                                                [ 60%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoVagas::test_vagas_negativas PASSED                                                             [ 66%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoVagas::test_vagas_altas PASSED                                                                 [ 73%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoRelacionamentos::test_has_status PASSED                                                                 [ 80%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoRelacionamentos::test_status_has_eventos PASSED                                                         [ 86%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoRelacionamentos::test_protect_status PASSED                                                             [ 93%]
apps/eventos/tests/test_models_evento_expanded.py::TestTurmaHorario::test_turma_horario_relation PASSED                                                              [100%]

---------- coverage: platform win32, python 3.13.2-final-0 -----------
Name                                                                    Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------------------
apps\__init__.py                                                            0      0   100%
apps\academico\__init__.py                                                  0      0   100%
apps\academico\admin.py                                                   316    246    22%   64-70, 124, 129, 200, 205, 211-216, 225-266, 270-276, 284-440, 450-613, 623-653, 663-671
apps\academico\apps.py                                                      5      0   100%
apps\academico\certificado.py                                             136    136     0%   9-254
apps\academico\models.py                                                  110     51    54%   45, 122, 128-154, 167-176, 191-214, 282-283, 300-316, 330-342
apps\academico\services.py                                                134    134     0%   8-396
apps\academico\urls.py                                                      5      5     0%   8-19
apps\academico\views.py                                                    63     63     0%   8-124
apps\accounts\__init__.py                                                   0      0   100%
apps\accounts\admin.py                                                     52     19    63%   40-44, 48-63, 149-169
apps\accounts\apps.py                                                       5      0   100%
apps\accounts\forms.py                                                      5      5     0%   8-27
apps\accounts\middleware.py                                                20     20     0%   17-83
apps\accounts\models.py                                                    22      4    82%   103-106
apps\accounts\urls.py                                                       5      5     0%   9-17
apps\accounts\views.py                                                     47     47     0%   16-114
apps\accounts\views_exclusao.py                                            77     77     0%   9-125
apps\dashboard\__init__.py                                                  0      0   100%
apps\dashboard\admin.py                                                     0      0   100%
apps\dashboard\apps.py                                                      4      0   100%
apps\dashboard\models.py                                                    1      0   100%
apps\dashboard\utils_pdf.py                                               373    373     0%   9-751
apps\dashboard\views.py                                                   216    216     0%   13-690
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212    117    45%   61-67, 95, 110-114, 118-119, 122-124, 173-181, 187-206, 218-223, 229-234, 240-245, 251-256, 269-358, 371-415, 430-519, 537
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51     51     0%   8-114
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122     23    81%   28, 104-106, 130-132, 135-137, 140-142, 145-147, 150-152, 201, 206, 247, 280
apps\eventos\views.py                                                       1      1     0%   1
apps\interessados\__init__.py                                               0      0   100%
apps\interessados\admin.py                                                218    120    45%   178-183, 188, 193-194, 201-207, 216-222, 231-243, 248-260, 265-269, 280-282, 296-316, 329-330, 337-338, 347-431, 475, 480-481, 485-500, 509, 514, 523-527, 535-538, 546-552, 564, 567, 570
apps\interessados\apps.py                                                   5      0   100%
apps\interessados\authentication.py                                        25     25     0%   9-73
apps\interessados\forms.py                                                157    157     0%   20-453
apps\interessados\management\__init__.py                                    0      0   100%
apps\interessados\management\commands\__init__.py                           0      0   100%
apps\interessados\management\commands\criptografar_cpfs.py                 22     22     0%   11-47
apps\interessados\management\commands\limpar_tokens.py                     59     59     0%   13-155
apps\interessados\management\commands\popular_cpf_hash.py                  22     22     0%   9-40
apps\interessados\models.py                                               139     19    86%   22, 29, 41, 132, 135, 138, 141, 144, 147, 151, 155, 158, 162, 166, 172, 188, 191-192, 260
apps\interessados\urls.py                                                   5      5     0%   11-17
apps\interessados\utils.py                                                 14     14     0%   10-38
apps\interessados\views.py                                                202    202     0%   24-519
apps\interessados\views_exclusao.py                                        29     29     0%   8-76
apps\portal\__init__.py                                                     1      0   100%
apps\portal\admin.py                                                        1      0   100%
apps\portal\apps.py                                                         5      0   100%
apps\portal\forms.py                                                       34     34     0%   14-104
apps\portal\models.py                                                       1      0   100%
apps\portal\urls.py                                                         4      4     0%   8-13
apps\portal\views.py                                                       99     99     0%   13-247
apps\scripts_admin\__init__.py                                              0      0   100%
apps\scripts_admin\management\__init__.py                                   0      0   100%
apps\scripts_admin\management\commands\__init__.py                          0      0   100%
apps\scripts_admin\management\commands\classificar_evento.py              133    133     0%   8-291
apps\scripts_admin\management\commands\configurar_criterios_evento.py      57     57     0%   5-91
apps\scripts_admin\management\commands\popular_criterios.py                21     21     0%   4-117
apps\scripts_admin\management\commands\popular_dados_iniciais.py           66     66     0%   8-234
apps\selecao\__init__.py                                                    0      0   100%
apps\selecao\admin.py                                                     275    163    41%   66-72, 87, 110-115, 152, 223, 233, 240-241, 247, 254-255, 266-275, 293-456, 466-503, 507-544, 552, 558, 564, 570, 580, 586, 592, 598, 608, 612, 616, 661, 667, 673, 677
apps\selecao\apps.py                                                        5      0   100%
apps\selecao\management\__init__.py                                         0      0   100%
apps\selecao\management\commands\__init__.py                                0      0   100%
apps\selecao\models.py                                                     71     15    79%   38, 74, 124-137, 145-146, 155, 188
apps\selecao\reports.py                                                   301    270    10%   27-31, 35-115, 126-132, 140-146, 151-163, 179-286, 302-420, 440-565, 580-711
apps\selecao\services.py                                                  125    125     0%   28-443
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4189   3360    20%
Coverage HTML written to dir htmlcov


=========================================================================== 15 passed in 3.15s ============================================================================



##  pytest apps/eventos/tests/test_models_evento.py em 09/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> pytest apps/eventos/tests/test_models_evento.py -v
========================================================== test session starts ===========================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 35 items                                                                                                                        

apps/eventos/tests/test_models_evento.py::TestEventoCRUD::test_criar_evento_valido PASSED                                           [  2%]
apps/eventos/tests/test_models_evento.py::TestEventoCRUD::test_ler_evento PASSED                                                    [  5%]
apps/eventos/tests/test_models_evento.py::TestEventoCRUD::test_atualizar_evento PASSED                                              [  8%]
apps/eventos/tests/test_models_evento.py::TestEventoCRUD::test_deletar_evento PASSED                                                [ 11%]
apps/eventos/tests/test_models_evento.py::TestEventoCRUD::test_multiplos_eventos PASSED                                             [ 14%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_data_inicio_inscricao_antes_fim_inscricao PASSED               [ 17%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_data_fim_inscricao_antes_inicio_evento PASSED                  [ 20%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_data_inicio_evento_antes_fim_evento PASSED                     [ 22%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_datas_validas_factory PASSED                                   [ 25%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_clean_valida_datas PASSED                                      [ 28%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_total_vagas_positivo PASSED                                    [ 31%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_total_vagas_grande_numero PASSED                               [ 34%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_total_vagas_zero_permitido PASSED                              [ 37%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_com_status PASSED                                           [ 40%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_sem_status_invalido PASSED                                  [ 42%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_com_turmas PASSED                                           [ 45%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_multiplas_turmas PASSED                                     [ 48%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_com_criterios PASSED                                        [ 51%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_multiplos_criterios PASSED                                  [ 54%]
apps/eventos/tests/test_models_evento.py::TestEventoTimestamps::test_evento_sem_criterios PASSED                                    [ 57%]
apps/eventos/tests/test_models_evento.py::TestEventoTimestamps::test_deletar_evento_deleta_turmas PASSED                            [ 60%]
apps/eventos/tests/test_models_evento.py::TestEventoTimestamps::test_criado_em_existe PASSED                                        [ 62%]
apps/eventos/tests/test_models_evento.py::TestEventoTimestamps::test_atualizado_em_existe PASSED                                    [ 65%]
apps/eventos/tests/test_models_evento.py::TestEventoTimestamps::test_atualizado_em_atualiza PASSED                                  [ 68%]
apps/eventos/tests/test_models_evento.py::TestEventoMetodos::test_inscricoes_abertas PASSED                                         [ 71%]
apps/eventos/tests/test_models_evento.py::TestEventoMetodos::test_inscricoes_fechadas PASSED                                        [ 74%]
apps/eventos/tests/test_models_evento.py::TestEventoMetodos::test_validacao_datas_inscricao PASSED                                  [ 77%]
apps/eventos/tests/test_models_evento.py::TestEventoMetodos::test_validacao_datas_evento PASSED                                     [ 80%]
apps/eventos/tests/test_models_evento.py::TestEventoMetodos::test_formatacao_datas PASSED                                           [ 82%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_filtro_por_status PASSED                                         [ 85%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_filtro_por_ativo PASSED                                          [ 88%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_queryset_count PASSED                                            [ 91%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_queryset_exists PASSED                                           [ 94%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_nome_obrigatorio PASSED                                          [ 97%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_str_representation PASSED                                        [100%]

---------- coverage: platform win32, python 3.13.2-final-0 -----------
Name                                                                    Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------------------
apps\__init__.py                                                            0      0   100%
apps\academico\__init__.py                                                  0      0   100%
apps\academico\admin.py                                                   320    248    22%   64-70, 124, 129, 200, 205, 211-216, 225-266, 270-276, 284-440, 450-613, 623-653, 663-671, 678, 681
apps\academico\apps.py                                                      5      0   100%
apps\academico\certificado.py                                             136    136     0%   9-254
apps\academico\models.py                                                  110     51    54%   45, 122, 128-154, 167-176, 191-214, 282-283, 300-316, 330-342
apps\academico\services.py                                                136    136     0%   8-402
apps\academico\urls.py                                                      5      5     0%   8-19
apps\academico\views.py                                                    63     63     0%   8-124
apps\accounts\__init__.py                                                   0      0   100%
apps\accounts\admin.py                                                     52     19    63%   40-44, 48-63, 149-169
apps\accounts\apps.py                                                       5      0   100%
apps\accounts\forms.py                                                      5      5     0%   8-27
apps\accounts\middleware.py                                                20     20     0%   17-83
apps\accounts\models.py                                                    22      4    82%   103-106
apps\accounts\urls.py                                                       5      5     0%   9-17
apps\accounts\views.py                                                     47     47     0%   16-114
apps\accounts\views_exclusao.py                                            77     77     0%   9-125
apps\dashboard\__init__.py                                                  0      0   100%
apps\dashboard\admin.py                                                     0      0   100%
apps\dashboard\apps.py                                                      4      0   100%
apps\dashboard\models.py                                                    1      0   100%
apps\dashboard\utils_pdf.py                                               373    373     0%   9-751
apps\dashboard\views.py                                                   216    216     0%   13-690
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212    117    45%   61-67, 95, 110-114, 118-119, 122-124, 173-181, 187-206, 218-223, 229-234, 240-245, 251-256, 269-358, 371-415, 430-519, 537
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51     51     0%   8-114
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122     12    90%   28, 104-106, 137, 142, 147, 152, 201, 206, 247, 280
apps\eventos\views.py                                                       1      1     0%   1
apps\interessados\__init__.py                                               0      0   100%
apps\interessados\admin.py                                                218    120    45%   178-183, 188, 193-194, 201-207, 216-222, 231-243, 248-260, 265-269, 280-282, 296-316, 329-330, 337-338, 347-431, 475, 480-481, 485-500, 509, 514, 523-527, 535-538, 546-552, 564, 567, 570
apps\interessados\apps.py                                                   5      0   100%
apps\interessados\authentication.py                                        25     25     0%   9-73
apps\interessados\forms.py                                                157    157     0%   20-453
apps\interessados\management\__init__.py                                    0      0   100%
apps\interessados\management\commands\__init__.py                           0      0   100%
apps\interessados\management\commands\criptografar_cpfs.py                 22     22     0%   11-47
apps\interessados\management\commands\limpar_tokens.py                     59     59     0%   13-155
apps\interessados\management\commands\popular_cpf_hash.py                  22     22     0%   9-40
apps\interessados\models.py                                               139     19    86%   22, 29, 41, 132, 135, 138, 141, 144, 147, 151, 155, 158, 162, 166, 172, 188, 191-192, 260
apps\interessados\urls.py                                                   5      5     0%   11-17
apps\interessados\utils.py                                                 14     14     0%   10-38
apps\interessados\views.py                                                202    202     0%   24-519
apps\interessados\views_exclusao.py                                        29     29     0%   8-76
apps\portal\__init__.py                                                     1      0   100%
apps\portal\admin.py                                                        1      0   100%
apps\portal\apps.py                                                         5      0   100%
apps\portal\forms.py                                                       34     34     0%   14-104
apps\portal\models.py                                                       1      0   100%
apps\portal\urls.py                                                         4      4     0%   8-13
apps\portal\views.py                                                       99     99     0%   13-247
apps\scripts_admin\__init__.py                                              0      0   100%
apps\scripts_admin\management\__init__.py                                   0      0   100%
apps\scripts_admin\management\commands\__init__.py                          0      0   100%
apps\scripts_admin\management\commands\classificar_evento.py              133    133     0%   8-291
apps\scripts_admin\management\commands\configurar_criterios_evento.py      57     57     0%   5-91
apps\scripts_admin\management\commands\popular_criterios.py                21     21     0%   4-117
apps\scripts_admin\management\commands\popular_dados_iniciais.py           66     66     0%   8-234
apps\selecao\__init__.py                                                    0      0   100%
apps\selecao\admin.py                                                     275    163    41%   66-72, 87, 110-115, 152, 223, 233, 240-241, 247, 254-255, 266-275, 293-456, 466-503, 507-544, 552, 558, 564, 570, 580, 586, 592, 598, 608, 612, 616, 661, 667, 673, 677
apps\selecao\apps.py                                                        5      0   100%
apps\selecao\management\__init__.py                                         0      0   100%
apps\selecao\management\commands\__init__.py                                0      0   100%
apps\selecao\models.py                                                     71     15    79%   38, 74, 124-137, 145-146, 155, 188
apps\selecao\reports.py                                                   301    270    10%   27-31, 35-115, 126-132, 140-146, 151-163, 179-286, 302-420, 440-565, 580-711
apps\selecao\services.py                                                  125    125     0%   28-443
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4195   3353    20%
Coverage HTML written to dir htmlcov


=========================================================== 35 passed in 4.19s ===========================================================



##  apps/eventos/tests/test_models_turma.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> pytest apps/eventos/tests/test_models_turma.py -v
========================================================== test session starts ===========================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 21 items                                                                                                                        

apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_criar_turma_valida PASSED                                             [  4%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_ler_turma PASSED                                                      [  9%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_atualizar_turma PASSED                                                [ 14%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_deletar_turma PASSED                                                  [ 19%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_multiplas_turmas PASSED                                               [ 23%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_datas_validas_factory PASSED                                          [ 28%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_capacidade_positiva PASSED                                            [ 33%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_capacidade_grande_numero PASSED                                       [ 38%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_capacidade_zero_permitido PASSED                                      [ 42%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_turma_com_evento PASSED                                               [ 47%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_turma_sem_evento_invalido PASSED                                      [ 52%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_turma_com_horarios PASSED                                             [ 57%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_turma_multiplos_horarios PASSED                                       [ 61%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_deletar_turma_deleta_horarios PASSED                                  [ 66%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_criado_em_existe PASSED                                               [ 71%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_atualizado_em_atualiza PASSED                                         [ 76%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_str_representation PASSED                                             [ 80%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_nome_obrigatorio PASSED                                               [ 85%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_filtro_por_evento PASSED                                              [ 90%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_filtro_por_turno PASSED                                               [ 95%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_queryset_count PASSED                                                 [100%]

============================================================ warnings summary ============================================================
..\.venv\Lib\site-packages\_pytest\config\__init__.py:1373
  c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\_pytest\config\__init__.py:1373: PytestConfigWarning: Unknown config option: python_path
  
    self._warn_or_fail_if_strict(f"Unknown config option: {key}\n")

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
===================================================== 21 passed, 1 warning in 1.83s ======================================================



##  apps/eventos/tests/test_models_horario.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> pytest apps/eventos/tests/test_models_horario.py -v
========================================================== test session starts ===========================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 14 items                                                                                                                        

apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_criar_horario_valido PASSED                                       [  7%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_ler_horario PASSED                                                [ 14%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_atualizar_horario PASSED                                          [ 21%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_deletar_horario PASSED                                            [ 28%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_dia_semana_valido PASSED                                          [ 35%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_multiplos_horarios_mesma_turma PASSED                             [ 42%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_hora_inicio_antes_fim PASSED                                      [ 50%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_hora_inicio_igual_fim_permitido PASSED                            [ 57%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_horario_com_turma PASSED                                          [ 64%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_horario_sem_turma_invalido PASSED                                 [ 71%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_turma_tem_multiplos_horarios PASSED                               [ 78%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_str_representation PASSED                                         [ 85%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_filtro_por_turma PASSED                                           [ 92%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_queryset_count PASSED                                             [100%]

============================================================ warnings summary ============================================================
..\.venv\Lib\site-packages\_pytest\config\__init__.py:1373
  c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\_pytest\config\__init__.py:1373: PytestConfigWarning: Unknown config option: python_path
  
    self._warn_or_fail_if_strict(f"Unknown config option: {key}\n")

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
===================================================== 14 passed, 1 warning in 1.77s =====================================================



##  apps/eventos/tests/test_models_criterio.py

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> pytest apps/eventos/tests/test_models_criterio.py -v
========================================================== test session starts ===========================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 15 items                                                                                                                        

apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_criar_criterio_valido PASSED                                    [  6%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_ler_criterio PASSED                                             [ 13%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_atualizar_criterio PASSED                                       [ 20%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_deletar_criterio PASSED                                         [ 26%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_codigo_unico PASSED                                             [ 33%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_codigo_valido PASSED                                            [ 40%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_pontos_positivo PASSED                                          [ 46%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_pontos_zero_permitido PASSED                                    [ 53%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_criterio_ativo_padrao PASSED                                    [ 60%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_criterio_inativo PASSED                                         [ 66%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_criterio_com_eventos PASSED                                     [ 73%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_criterio_sem_eventos PASSED                                     [ 80%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_str_representation PASSED                                       [ 86%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_filtro_por_ativo PASSED                                         [ 93%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_queryset_count PASSED                                           [100%]

============================================================ warnings summary ============================================================
..\.venv\Lib\site-packages\_pytest\config\__init__.py:1373
  c:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Lib\site-packages\_pytest\config\__init__.py:1373: PytestConfigWarning: Unknown config option: python_path
  
    self._warn_or_fail_if_strict(f"Unknown config option: {key}\n")

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
===================================================== 15 passed, 1 warning in 1.82s ======================================================


























