# Testes do Admin - Eventos

## Status
- 29 testes passando (100%)
- Cobertura: admin.py completo (5 classes de modelo)
- Data: 26/05/2026

## Executar Testes
python manage.py test apps.eventos.tests.test_admin -v 2

## Cobertura por Classe
- StatusAdminTest (5 testes)
- EventoAdminTest (12 testes)
- TurmaAdminTest (6 testes)
- HorarioAdminTest (6 testes)




## O que está abaixo coloquei por minha conta (Marcos)

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
