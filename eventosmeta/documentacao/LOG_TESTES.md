## Saída do LOG de execução de testes


##  apps.academico.tests.test_admin.py em 09/06/2026, 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/academico/tests/test_admin.py -v  
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 11 items                                                                                                                                          

apps/academico/tests/test_admin.py::TestStatusMatriculaAdmin::test_cor_display_com_cor PASSED                                                         [  9%]
apps/academico/tests/test_admin.py::TestStatusMatriculaAdmin::test_cor_display_sem_cor PASSED                                                         [ 18%]
apps/academico/tests/test_admin.py::TestMatriculaAdmin::test_get_interessado PASSED                                                                   [ 27%]
apps/academico/tests/test_admin.py::TestMatriculaAdmin::test_get_evento PASSED                                                                        [ 36%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_acoes_certificado_aprovado PASSED                                                        [ 45%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_acoes_certificado_nao_aprovado PASSED                                                    [ 54%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_changelist_view_contexto PASSED                                                          [ 63%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_gerar_certificados_marca_emitidos PASSED                                                 [ 72%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_gerar_certificados_sem_aprovados PASSED                                                  [ 81%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_gerar_certificados_ja_emitido PASSED                                                     [ 90%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_download_certificados_lote_action_redirect PASSED                                        [100%]

---------- coverage: platform win32, python 3.13.2-final-0 -----------
Name                                                                    Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------------------
apps\__init__.py                                                            0      0   100%
apps\academico\__init__.py                                                  0      0   100%
apps\academico\admin.py                                                   320    199    38%   245-264, 270-276, 284-440, 450-613, 641-642, 666-667, 678, 681
apps\academico\apps.py                                                      5      0   100%
apps\academico\certificado.py                                             136    118    13%   24-37, 43-67, 72-79, 83-104, 108-116, 120-163, 167-208, 212-254
apps\academico\models.py                                                  110     34    69%   45, 122, 133, 142, 154, 168, 174, 191-214, 300-316, 339-342
apps\academico\services.py                                                136    136     0%   8-402
apps\academico\urls.py                                                      5      0   100%
apps\academico\views.py                                                    63     45    29%   31-52, 61-77, 87-124
apps\accounts\__init__.py                                                   0      0   100%
apps\accounts\admin.py                                                     52     16    69%   50-65, 141-158
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
apps\dashboard\services.py                                                157    105    33%   23-26, 34-43, 47-56, 60-81, 85-93, 108-116, 131-152, 156-199, 203, 220-222, 233-236, 247-249, 255-257, 265, 278-293, 304-311, 315-317, 325-326, 338-343, 367-381, 390-392, 400
apps\dashboard\utils_pdf.py                                               373    350     6%   25-56, 61-80, 86-87, 90-91, 94-99, 102-107, 112-298, 303-464, 469-608, 613-751
apps\dashboard\views.py                                                    71     47    34%   33-42, 47-56, 61-70, 75-84, 89-109, 118-125, 130-137, 142-149, 154-161
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   2956    30%
Coverage HTML written to dir htmlcov


=================================================================== 11 passed in 12.49s ====================================================================




##  apps.academico.tests.test_certificad.py em 17/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/academico/tests/test_certificado.py -v
================================================================================ test session starts ================================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 10 items                                                                                                                                                                   

apps/academico/tests/test_certificado.py::TestAtributos::test_inicializacao_atributos PASSED                                                                                   [ 10%]
apps/academico/tests/test_certificado.py::TestAtributos::test_pagesize_a4_paisagem PASSED                                                                                      [ 20%]
apps/academico/tests/test_certificado.py::TestAtributos::test_static_path_construido PASSED                                                                                    [ 30%]
apps/academico/tests/test_certificado.py::TestFormatacao::test_cpf_formatado PASSED                                                                                            [ 40%]
apps/academico/tests/test_certificado.py::TestTraducaoMes::test_traducao_mes[data0-15 de janeiro de 2026] PASSED                                                               [ 50%]
apps/academico/tests/test_certificado.py::TestTraducaoMes::test_traducao_mes[data1-03 de agosto de 2026] PASSED                                                                [ 60%]
apps/academico/tests/test_certificado.py::TestFallback::test_data_emissao_fallback_para_agora PASSED                                                                           [ 70%]
apps/academico/tests/test_certificado.py::TestFallback::test_carga_horaria_fallback_40h PASSED                                                                                 [ 80%]
apps/academico/tests/test_certificado.py::TestGeracaoPDF::test_gerar_pdf_retorna_buffer_valido PASSED                                                                          [ 90%]
apps/academico/tests/test_certificado.py::TestGeracaoPDF::test_gerar_pdf_multiplas_chamadas PASSED                                                                             [100%]

---------- coverage: platform win32, python 3.13.2-final-0 -----------
Name                                                                    Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------------------
apps\__init__.py                                                            0      0   100%
apps\academico\__init__.py                                                  0      0   100%
apps\academico\admin.py                                                   320    248    22%   64-70, 124, 129, 200, 205, 211-216, 225-266, 270-276, 284-440, 450-613, 623-653, 663-671, 678, 681
apps\academico\apps.py                                                      5      0   100%
apps\academico\certificado.py                                             136      3    98%   103-104, 193
apps\academico\models.py                                                  110     36    67%   45, 122, 133, 142, 154, 168, 174, 191-214, 282-283, 300-316, 339-342
apps\academico\services.py                                                136    136     0%   8-402
apps\academico\urls.py                                                      5      5     0%   8-19
apps\academico\views.py                                                    63     63     0%   8-124
apps\accounts\__init__.py                                                   0      0   100%
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3233    23%
Coverage HTML written to dir htmlcov


================================================================================ 10 passed in 7.43s =================================================================================



##  apps.academico.tests.test_models.py em 17/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/academico/tests/test_models.py -v
================================================================================ test session starts ================================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 4 items                                                                                                                                                                    

apps/academico/tests/test_models.py::TestStatusMatriculaModel::test_status_criado_corretamente PASSED                                                                          [ 25%]
apps/academico/tests/test_models.py::TestStatusMatriculaModel::test_status_nome_unique_no_banco PASSED                                                                         [ 50%]
apps/academico/tests/test_models.py::TestMatriculaModel::test_matricula_criada_corretamente PASSED                                                                             [ 75%]
apps/academico/tests/test_models.py::TestMatriculaModel::test_matricula_unique_together_turma_interessado PASSED                                                               [100%]

---------- coverage: platform win32, python 3.13.2-final-0 -----------
Name                                                                    Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------------------
apps\__init__.py                                                            0      0   100%
apps\academico\__init__.py                                                  0      0   100%
apps\academico\admin.py                                                   320    248    22%   64-70, 124, 129, 200, 205, 211-216, 225-266, 270-276, 284-440, 450-613, 623-653, 663-671, 678, 681
apps\academico\apps.py                                                      5      0   100%
apps\academico\certificado.py                                             136    136     0%   9-254
apps\academico\models.py                                                  110     27    75%   45, 122, 133, 142, 168, 201-206, 282-283, 300-316, 339-342
apps\academico\services.py                                                136    136     0%   8-402
apps\academico\urls.py                                                      5      5     0%   8-19
apps\academico\views.py                                                    63     63     0%   8-124
apps\accounts\__init__.py                                                   0      0   100%
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3357    20%
Coverage HTML written to dir htmlcov


================================================================================= 4 passed in 3.55s =================================================================================



##  apps.academico.tests.test_services.py em 09/06/2026, 18/06/2026, 22/06/2026 (aumento de cobertura)

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/academico/tests/test_services.py -v --tb=short
=========================================================================== test session starts ===========================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 35 items                                                                                                                                                         

apps/academico/tests/test_services.py::TestVerificacaoDisponibilidade::test_verificar_disponibilidade_turma_com_vagas PASSED                                         [  2%]
apps/academico/tests/test_services.py::TestVerificacaoDisponibilidade::test_verificar_disponibilidade_turma_lotada PASSED                                            [  5%]
apps/academico/tests/test_services.py::TestVerificacaoDisponibilidade::test_verificar_disponibilidade_turma_parcial PASSED                                           [  8%]
apps/academico/tests/test_services.py::TestVerificacaoDisponibilidade::test_verificar_disponibilidade_turma_exatamente_cheia PASSED                                  [ 11%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_aprovado PASSED                                                                        [ 14%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_reprovado_por_nota PASSED                                                              [ 17%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_reprovado_por_frequencia PASSED                                                        [ 20%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_nota_invalida PASSED                                                                   [ 22%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_frequencia_invalida PASSED                                                             [ 25%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_nota_limite_minimo_aprovado PASSED                                                     [ 28%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_nota_limite_maximo PASSED                                                              [ 31%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_frequencia_limite_minimo PASSED                                                        [ 34%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_frequencia_limite_maximo PASSED                                                        [ 37%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_atualiza_status_matricula PASSED                                                       [ 40%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_cria_ou_atualiza PASSED                                                                [ 42%]
apps/academico/tests/test_services.py::TestRelatorioTurma::test_gerar_relatorio_turma PASSED                                                                         [ 45%]
apps/academico/tests/test_services.py::TestRelatorioTurma::test_gerar_relatorio_turma_vazia PASSED                                                                   [ 48%]
apps/academico/tests/test_services.py::TestRelatorioTurma::test_gerar_relatorio_turma_parcialmente_avaliada PASSED                                                   [ 51%]
apps/academico/tests/test_services.py::TestRelatorioTurma::test_gerar_relatorio_turma_valida_valores PASSED                                                          [ 54%]
apps/academico/tests/test_services.py::TestMatricularClassificado::test_matricular_classificado_com_sucesso PASSED                                                   [ 57%]
apps/academico/tests/test_services.py::TestMatricularClassificado::test_matricular_classificado_nao_classificado PASSED                                              [ 60%]
apps/academico/tests/test_services.py::TestMatricularClassificado::test_matricular_classificado_turma_lotada PASSED                                                  [ 62%]
apps/academico/tests/test_services.py::TestMatricularClassificado::test_matricular_classificado_ja_matriculado PASSED                                                [ 65%]
apps/academico/tests/test_services.py::TestMatricularClassificado::test_matricular_classificado_sem_status_ativa PASSED                                              [ 68%]
apps/academico/tests/test_services.py::TestMatricularLote::test_matricular_lote_todos_sucesso PASSED                                                                 [ 71%]
apps/academico/tests/test_services.py::TestMatricularLote::test_matricular_lote_um_erro PASSED                                                                       [ 74%]
apps/academico/tests/test_services.py::TestMatricularLote::test_matricular_lote_todos_erro PASSED                                                                    [ 77%]
apps/academico/tests/test_services.py::TestMatricularAlunos::test_matricular_alunos_com_sucesso PASSED                                                               [ 80%]
apps/academico/tests/test_services.py::TestMatricularAlunos::test_matricular_alunos_sem_turma PASSED                                                                 [ 82%]
apps/academico/tests/test_services.py::TestMatricularAlunos::test_matricular_alunos_ja_matriculado PASSED                                                            [ 85%]
apps/academico/tests/test_services.py::TestMatricularAlunos::test_matricular_alunos_sem_status_ativa PASSED                                                          [ 88%]
apps/academico/tests/test_services.py::TestMatricularAlunos::test_matricular_alunos_multiplos PASSED                                                                 [ 91%]
apps/academico/tests/test_services.py::TestAlterarStatusInscricao::test_alterar_status_todas PASSED                                                                  [ 94%]
apps/academico/tests/test_services.py::TestAlterarStatusInscricao::test_alterar_status_uma PASSED                                                                    [ 97%]
apps/academico/tests/test_services.py::TestAlterarStatusInscricao::test_alterar_status_inexistente PASSED                                                            [100%]

---------- coverage: platform win32, python 3.13.2-final-0 -----------
Name                                                                    Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------------------
apps\__init__.py                                                            0      0   100%
apps\academico\__init__.py                                                  0      0   100%
apps\academico\admin.py                                                   320    248    22%   64-70, 124, 129, 200, 205, 211-216, 225-266, 270-276, 284-440, 450-613, 623-653, 663-671, 678, 681
apps\academico\apps.py                                                      5      0   100%
apps\academico\certificado.py                                             136    136     0%   9-254
apps\academico\models.py                                                  110     25    77%   45, 122, 133, 142, 154, 168, 204-206, 282-283, 300-316, 339-342
apps\academico\services.py                                                136      8    94%   172-173, 230-232, 281-283
apps\academico\urls.py                                                      5      5     0%   8-19
apps\academico\views.py                                                    63     63     0%   8-124
apps\accounts\__init__.py                                                   0      0   100%
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\views.py                                                       0      0   100%
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4207   3219    23%
Coverage HTML written to dir htmlcov


=========================================================================== 35 passed in 28.11s ======================================================================



##  apps.academico.tests.test_views.py em 17/06/2026, 22/06/2026 (aumento de cobertura)

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/academico/tests/test_views.py -v --tb=short     
================================================================= test session starts =================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 16 items                                                                                                                                     

apps/academico/tests/test_views.py::TestDownloadCertificadoIndividual::test_sem_autenticacao_redireciona PASSED                                  [  6%]
apps/academico/tests/test_views.py::TestDownloadCertificadoIndividual::test_aluno_aprovado_gera_pdf PASSED                                       [ 12%]
apps/academico/tests/test_views.py::TestDownloadCertificadoIndividual::test_aluno_reprovado_retorna_400 PASSED                                   [ 18%]
apps/academico/tests/test_views.py::TestDownloadCertificadoIndividual::test_avaliacao_inexistente_retorna_404 PASSED                             [ 25%]
apps/academico/tests/test_views.py::TestPreviewCertificado::test_sem_autenticacao_redireciona PASSED                                             [ 31%]
apps/academico/tests/test_views.py::TestPreviewCertificado::test_aluno_aprovado_inline PASSED                                                    [ 37%]
apps/academico/tests/test_views.py::TestPreviewCertificado::test_aluno_reprovado_retorna_400 PASSED                                              [ 43%]
apps/academico/tests/test_views.py::TestDownloadCertificadosLote::test_sem_ids_retorna_400 PASSED                                                [ 50%]
apps/academico/tests/test_views.py::TestDownloadCertificadosLote::test_ids_todos_invalidos_retorna_400 PASSED                                    [ 56%]
apps/academico/tests/test_views.py::TestDownloadCertificadosLote::test_sem_aprovados_entre_ids_validos_retorna_400 PASSED                        [ 62%]
apps/academico/tests/test_views.py::TestDownloadCertificadosLote::test_apenas_aprovados_no_zip PASSED                                            [ 68%]
apps/academico/tests/test_views.py::TestDownloadCertificadosLote::test_zip_com_multiplos_certificados PASSED                                     [ 75%]
apps/academico/tests/test_views.py::TestDownloadCertificadosLote::test_zip_filename_contem_contagem PASSED                                       [ 81%]
apps/academico/tests/test_views.py::TestMetodosHttpNaoPermitidos::test_download_certificado_post_retorna_405 PASSED                              [ 87%]
apps/academico/tests/test_views.py::TestMetodosHttpNaoPermitidos::test_preview_certificado_put_retorna_405 PASSED                                [ 93%]
apps/academico/tests/test_views.py::TestMetodosHttpNaoPermitidos::test_lote_post_retorna_405 PASSED                                              [100%]

---------- coverage: platform win32, python 3.13.2-final-0 -----------
Name                                                                    Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------------------
apps\__init__.py                                                            0      0   100%
apps\academico\__init__.py                                                  0      0   100%
apps\academico\admin.py                                                   320    248    22%   64-70, 124, 129, 200, 205, 211-216, 225-266, 270-276, 284-440, 450-613, 623-653, 663-671, 678, 681
apps\academico\apps.py                                                      5      0   100%
apps\academico\certificado.py                                             136      4    97%   103-104, 193, 219
apps\academico\models.py                                                  110     25    77%   45, 122, 133, 142, 154, 168, 204-206, 282-283, 300-316, 339-342
apps\academico\services.py                                                136    136     0%   8-404
apps\academico\urls.py                                                      5      0   100%
apps\academico\views.py                                                    63      0   100%
apps\accounts\__init__.py                                                   0      0   100%
apps\accounts\admin.py                                                     52     16    69%   50-65, 141-158
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
apps\dashboard\services.py                                                157    105    33%   23-26, 34-43, 47-56, 60-81, 85-93, 108-116, 131-152, 156-199, 203, 220-222, 233-236, 247-249, 255-257, 265, 278-293, 304-311, 315-317, 325-326, 338-343, 367-381, 390-392, 400
apps\dashboard\utils_pdf.py                                               373    350     6%   25-56, 61-80, 86-87, 90-91, 94-99, 102-107, 112-298, 303-464, 469-608, 613-751
apps\dashboard\views.py                                                    71     47    34%   33-42, 47-56, 61-70, 75-84, 89-109, 118-125, 130-137, 142-149, 154-161
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       0      0   100%
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4207   2882    31%
Coverage HTML written to dir htmlcov


================================================================= 16 passed in 17.16s ==========================================================



##  apps.accounts.test.test_models.py em 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/accounts/tests/test_models.py -v     
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 11 items                                                                                                                                          

apps/accounts/tests/test_models.py::test_criar_usuario_com_cpf_valido PASSED                                                                          [  9%]
apps/accounts/tests/test_models.py::test_criar_usuario_com_cpf_invalido[1234567890] PASSED                                                            [ 18%]
apps/accounts/tests/test_models.py::test_criar_usuario_com_cpf_invalido[123456789012] PASSED                                                          [ 27%]
apps/accounts/tests/test_models.py::test_cpf_unico PASSED                                                                                             [ 36%]
apps/accounts/tests/test_models.py::test_usuario_staff_pode_login PASSED                                                                              [ 45%]
apps/accounts/tests/test_models.py::test_usuario_nao_staff_nao_pode_login_staff PASSED                                                                [ 54%]
apps/accounts/tests/test_models.py::test_criar_usuario_sem_username_falha PASSED                                                                      [ 63%]
apps/accounts/tests/test_models.py::test_criar_usuario_sem_password_falha PASSED                                                                      [ 72%]
apps/accounts/tests/test_models.py::test_criar_superuser_is_staff PASSED                                                                              [ 81%]
apps/accounts/tests/test_models.py::test_criar_superuser_is_superuser PASSED                                                                          [ 90%]
apps/accounts/tests/test_models.py::test_usuario_str_retorna_username PASSED                                                                          [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
apps\accounts\apps.py                                                       5      0   100%
apps\accounts\forms.py                                                      5      5     0%   8-27
apps\accounts\middleware.py                                                20     20     0%   17-83
apps\accounts\models.py                                                    22      1    95%   105
apps\accounts\urls.py                                                       5      5     0%   9-17
apps\accounts\views.py                                                     47     47     0%   16-114
apps\accounts\views_exclusao.py                                            77     77     0%   9-125
apps\dashboard\__init__.py                                                  0      0   100%
apps\dashboard\admin.py                                                     0      0   100%
apps\dashboard\apps.py                                                      4      0   100%
apps\dashboard\models.py                                                    1      0   100%
apps\dashboard\services.py                                                157    157     0%   12-400
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3380    20%
Coverage HTML written to dir htmlcov


==================================================================== 11 passed in 7.35s ====================================================================



##  apps.accounts.test.test_views.py em 17/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/accounts/tests/test_views.py -v
=============================================================== test session starts ================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 10 items                                                                                                                                  

apps/accounts/tests/test_views.py::AccountsViewsTest::test_login_staff_form_tem_csrf PASSED                                                   [ 10%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_login_staff_get PASSED                                                             [ 20%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_login_staff_inativo_falha PASSED                                                   [ 30%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_login_staff_invalido PASSED                                                        [ 40%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_login_staff_nao_staff PASSED                                                       [ 50%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_login_staff_valido PASSED                                                          [ 60%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_logout_staff PASSED                                                                [ 70%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_logout_staff_get_desloga PASSED                                                    [ 80%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_nao_staff_redirecionado_ao_acessar_pagina_staff PASSED                             [ 90%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_staff_acessa_pagina_restrita_apos_login PASSED                                     [100%]

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
apps\accounts\views.py                                                     47     20    57%   27, 83-114
apps\accounts\views_exclusao.py                                            77     66    14%   19, 25-33, 43-83, 94-125
apps\dashboard\__init__.py                                                  0      0   100%
apps\dashboard\admin.py                                                     0      0   100%
apps\dashboard\apps.py                                                      4      0   100%
apps\dashboard\models.py                                                    1      0   100%
apps\dashboard\services.py                                                157    105    33%   23-26, 34-43, 47-56, 60-81, 85-93, 108-116, 131-152, 156-199, 203, 220-222, 233-236, 247-249, 255-257, 265, 278-293, 304-311, 315-317, 325-326, 338-343, 367-381, 390-392, 400
apps\dashboard\utils_pdf.py                                               373    350     6%   25-56, 61-80, 86-87, 90-91, 94-99, 102-107, 112-298, 303-464, 469-608, 613-751
apps\dashboard\views.py                                                    71     47    34%   33-42, 47-56, 61-70, 75-84, 89-109, 118-125, 130-137, 142-149, 154-161
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212    117    45%   61-67, 95, 110-114, 118-119, 122-124, 173-181, 187-206, 218-223, 229-234, 240-245, 251-256, 269-358, 371-415, 430-519, 537
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51     40    22%   37-112
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122     29    76%   28, 104-106, 127, 130-132, 135-137, 140-142, 145-147, 150-152, 155-160, 201, 206, 247, 280
apps\eventos\views.py                                                       1      1     0%   1
apps\interessados\__init__.py                                               0      0   100%
apps\interessados\admin.py                                                218    120    45%   178-183, 188, 193-194, 201-207, 216-222, 231-243, 248-260, 265-269, 280-282, 296-316, 329-330, 337-338, 347-431, 475, 480-481, 485-500, 509, 514, 523-527, 535-538, 546-552, 564, 567, 570
apps\interessados\apps.py                                                   5      0   100%
apps\interessados\authentication.py                                        25     18    28%   37-52, 65-73
apps\interessados\forms.py                                                157    106    32%   167-171, 179-213, 220-230, 234-235, 239-243, 247, 251, 255, 259, 263, 267, 271, 275-280, 287-302, 335-358, 392-396, 401-402, 406-410, 414, 418, 422, 426, 430, 434, 438, 445-453
apps\interessados\management\__init__.py                                    0      0   100%
apps\interessados\management\commands\__init__.py                           0      0   100%
apps\interessados\management\commands\criptografar_cpfs.py                 22     22     0%   11-47
apps\interessados\management\commands\limpar_tokens.py                     59     59     0%   13-155
apps\interessados\management\commands\popular_cpf_hash.py                  22     22     0%   9-40
apps\interessados\models.py                                               139     19    86%   22, 29, 41, 132, 135, 138, 141, 144, 147, 151, 155, 158, 162, 166, 172, 188, 191-192, 260
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3034    28%
Coverage HTML written to dir htmlcov


=============================================================== 10 passed in 15.62s ================================================================


##  apps.accounts.test.test_views_exclusao.py em 17/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/accounts/tests/test_views_exclusao.py -v
=============================================================== test session starts ================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 15 items                                                                                                                                  

apps/accounts/tests/test_views_exclusao.py::TestListarSolicitacoesView::test_listar_solicitacoes_status_200 PASSED                            [  6%]
apps/accounts/tests/test_views_exclusao.py::TestListarSolicitacoesView::test_listar_solicitacoes_sem_login_redirect PASSED                    [ 13%]
apps/accounts/tests/test_views_exclusao.py::TestListarSolicitacoesView::test_listar_solicitacoes_nao_staff_redirect PASSED                    [ 20%]
apps/accounts/tests/test_views_exclusao.py::TestListarSolicitacoesView::test_listar_solicitacoes_contexto_tem_pendentes PASSED                [ 26%]
apps/accounts/tests/test_views_exclusao.py::TestListarSolicitacoesView::test_listar_solicitacoes_contexto_tem_aprovadas PASSED                [ 33%]
apps/accounts/tests/test_views_exclusao.py::TestListarSolicitacoesView::test_listar_solicitacoes_contexto_tem_recusadas PASSED                [ 40%]
apps/accounts/tests/test_views_exclusao.py::TestDetalheSolicitacaoView::test_detalhe_solicitacao_status_200 PASSED                            [ 46%]
apps/accounts/tests/test_views_exclusao.py::TestDetalheSolicitacaoView::test_detalhe_solicitacao_sem_login_redirect PASSED                    [ 53%]
apps/accounts/tests/test_views_exclusao.py::TestDetalheSolicitacaoView::test_detalhe_solicitacao_404 PASSED                                   [ 60%]
apps/accounts/tests/test_views_exclusao.py::TestDetalheSolicitacaoView::test_detalhe_solicitacao_aprovar PASSED                               [ 66%]
apps/accounts/tests/test_views_exclusao.py::TestDetalheSolicitacaoView::test_detalhe_solicitacao_recusar PASSED                               [ 73%]
apps/accounts/tests/test_views_exclusao.py::TestDetalheSolicitacaoView::test_detalhe_solicitacao_acao_invalida PASSED                         [ 80%]
apps/accounts/tests/test_views_exclusao.py::TestDetalheSolicitacaoView::test_detalhe_solicitacao_sem_parecer PASSED                           [ 86%]
apps/accounts/tests/test_views_exclusao.py::TestAnonimizarInteressado::test_anonimizar_interessado_limpa_campos PASSED                        [ 93%]
apps/accounts/tests/test_views_exclusao.py::TestAnonimizarInteressado::test_anonimizar_interessado_mantem_registro PASSED                     [100%]

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
apps\accounts\views_exclusao.py                                            77      2    97%   44-45
apps\dashboard\__init__.py                                                  0      0   100%
apps\dashboard\admin.py                                                     0      0   100%
apps\dashboard\apps.py                                                      4      0   100%
apps\dashboard\models.py                                                    1      0   100%
apps\dashboard\services.py                                                157    105    33%   23-26, 34-43, 47-56, 60-81, 85-93, 108-116, 131-152, 156-199, 203, 220-222, 233-236, 247-249, 255-257, 265, 278-293, 304-311, 315-317, 325-326, 338-343, 367-381, 390-392, 400
apps\dashboard\utils_pdf.py                                               373    350     6%   25-56, 61-80, 86-87, 90-91, 94-99, 102-107, 112-298, 303-464, 469-608, 613-751
apps\dashboard\views.py                                                    71     47    34%   33-42, 47-56, 61-70, 75-84, 89-109, 118-125, 130-137, 142-149, 154-161
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212    117    45%   61-67, 95, 110-114, 118-119, 122-124, 173-181, 187-206, 218-223, 229-234, 240-245, 251-256, 269-358, 371-415, 430-519, 537
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51     41    20%   25, 37-112
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122     29    76%   28, 104-106, 127, 130-132, 135-137, 140-142, 145-147, 150-152, 155-160, 201, 206, 247, 280
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   2994    29%
Coverage HTML written to dir htmlcov


=============================================================== 15 passed in 26.90s ================================================================



##  apps.accounts.test.test_admin.py em 17/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/accounts/tests/test_admin.py -v
================================================================================ test session starts ================================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 11 items                                                                                                                                                                   

apps/accounts/tests/test_admin.py::TestCustomAdminSite::test_admin_index_status_200 PASSED                                                                                     [  9%]
apps/accounts/tests/test_admin.py::TestCustomAdminSite::test_admin_index_sem_login_redirect PASSED                                                                             [ 18%]
apps/accounts/tests/test_admin.py::TestCustomAdminSite::test_dashboard_status_200 PASSED                                                                                       [ 27%]
apps/accounts/tests/test_admin.py::TestCustomAdminSite::test_dashboard_sem_login_redirect PASSED                                                                               [ 36%]
apps/accounts/tests/test_admin.py::TestUsuarioAdminList::test_usuario_admin_list_status_200 PASSED                                                                             [ 45%]
apps/accounts/tests/test_admin.py::TestUsuarioAdminList::test_usuario_admin_list_sem_login_redirect PASSED                                                                     [ 54%]
apps/accounts/tests/test_admin.py::TestUsuarioAdminList::test_usuario_admin_list_pesquisa_por_username PASSED                                                                  [ 63%]
apps/accounts/tests/test_admin.py::TestUsuarioAdminAdd::test_usuario_admin_add_status_200 PASSED                                                                               [ 72%]
apps/accounts/tests/test_admin.py::TestUsuarioAdminAdd::test_usuario_admin_add_usuario PASSED                                                                                  [ 81%]
apps/accounts/tests/test_admin.py::TestUsuarioAdminActionGerarSenhaProvisoria::test_gerar_senha_provisoria_seleciona_1 PASSED                                                  [ 90%]
apps/accounts/tests/test_admin.py::TestUsuarioAdminActionGerarSenhaProvisoria::test_gerar_senha_provisoria_seleciona_2_falha PASSED                                            [100%]

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
apps\accounts\admin.py                                                     52      0   100%
apps\accounts\apps.py                                                       5      0   100%
apps\accounts\forms.py                                                      5      5     0%   8-27
apps\accounts\middleware.py                                                20      9    55%   66-81
apps\accounts\models.py                                                    22      1    95%   105
apps\accounts\urls.py                                                       5      0   100%
apps\accounts\views.py                                                     47     38    19%   26-52, 60-62, 83-114
apps\accounts\views_exclusao.py                                            77     66    14%   19, 25-33, 43-83, 94-125
apps\dashboard\__init__.py                                                  0      0   100%
apps\dashboard\admin.py                                                     0      0   100%
apps\dashboard\apps.py                                                      4      0   100%
apps\dashboard\models.py                                                    1      0   100%
apps\dashboard\services.py                                                157    105    33%   23-26, 34-43, 47-56, 60-81, 85-93, 108-116, 131-152, 156-199, 203, 220-222, 233-236, 247-249, 255-257, 265, 278-293, 304-311, 315-317, 325-326, 338-343, 367-381, 390-392, 400
apps\dashboard\utils_pdf.py                                               373    350     6%   25-56, 61-80, 86-87, 90-91, 94-99, 102-107, 112-298, 303-464, 469-608, 613-751
apps\dashboard\views.py                                                    71     47    34%   33-42, 47-56, 61-70, 75-84, 89-109, 118-125, 130-137, 142-149, 154-161
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212    116    45%   61-67, 110-114, 118-119, 122-124, 173-181, 187-206, 218-223, 229-234, 240-245, 251-256, 269-358, 371-415, 430-519, 537
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51     41    20%   25, 37-112
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122     29    76%   28, 104-106, 127, 130-132, 135-137, 140-142, 145-147, 150-152, 155-160, 201, 206, 247, 280
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
apps\interessados\models.py                                               139     19    86%   22, 29, 41, 132, 135, 138, 141, 144, 147, 151, 155, 158, 162, 166, 172, 188, 191-192, 260
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3032    28%
Coverage HTML written to dir htmlcov


================================================================================ 11 passed in 13.84s ================================================================================



##  apps.accounts.tests.test_middleware.py em 17/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/accounts/tests/test_middleware.py -v
================================================================================ test session starts ================================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 9 items                                                                                                                                                                    

apps/accounts/tests/test_middleware.py::test_usuario_nao_autenticado_passa PASSED                                                                                              [ 11%]
apps/accounts/tests/test_middleware.py::test_usuario_sem_must_change_password_passa PASSED                                                                                     [ 22%]
apps/accounts/tests/test_middleware.py::test_usuario_com_must_change_password_url_liberada_staff PASSED                                                                        [ 33%]
apps/accounts/tests/test_middleware.py::test_usuario_com_must_change_password_url_restrita_staff PASSED                                                                        [ 44%]
apps/accounts/tests/test_middleware.py::test_interessado_com_must_change_password_url_restrita PASSED                                                                          [ 55%]
apps/accounts/tests/test_middleware.py::test_static_url_liberada_mesmo_com_must_change_password PASSED                                                                         [ 66%]
apps/accounts/tests/test_middleware.py::test_media_url_liberada_mesmo_com_must_change_password PASSED                                                                          [ 77%]
apps/accounts/tests/test_middleware.py::test_url_admin_login_liberada PASSED                                                                                                   [ 88%]
apps/accounts/tests/test_middleware.py::test_url_admin_logout_liberada PASSED                                                                                                  [100%]

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
apps\accounts\admin.py                                                     52     16    69%   50-65, 141-158
apps\accounts\apps.py                                                       5      0   100%
apps\accounts\forms.py                                                      5      5     0%   8-27
apps\accounts\middleware.py                                                20      0   100%
apps\accounts\models.py                                                    22      4    82%   103-106
apps\accounts\urls.py                                                       5      0   100%
apps\accounts\views.py                                                     47     38    19%   26-52, 60-62, 83-114
apps\accounts\views_exclusao.py                                            77     66    14%   19, 25-33, 43-83, 94-125
apps\dashboard\__init__.py                                                  0      0   100%
apps\dashboard\admin.py                                                     0      0   100%
apps\dashboard\apps.py                                                      4      0   100%
apps\dashboard\models.py                                                    1      0   100%
apps\dashboard\services.py                                                157    105    33%   23-26, 34-43, 47-56, 60-81, 85-93, 108-116, 131-152, 156-199, 203, 220-222, 233-236, 247-249, 255-257, 265, 278-293, 304-311, 315-317, 325-326, 338-343, 367-381, 390-392, 400
apps\dashboard\utils_pdf.py                                               373    350     6%   25-56, 61-80, 86-87, 90-91, 94-99, 102-107, 112-298, 303-464, 469-608, 613-751
apps\dashboard\views.py                                                    71     47    34%   33-42, 47-56, 61-70, 75-84, 89-109, 118-125, 130-137, 142-149, 154-161
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
apps\interessados\forms.py                                                157    106    32%   167-171, 179-213, 220-230, 234-235, 239-243, 247, 251, 255, 259, 263, 267, 271, 275-280, 287-302, 335-358, 392-396, 401-402, 406-410, 414, 418, 422, 426, 430, 434, 438, 445-453
apps\interessados\management\__init__.py                                    0      0   100%
apps\interessados\management\commands\__init__.py                           0      0   100%
apps\interessados\management\commands\criptografar_cpfs.py                 22     22     0%   11-47
apps\interessados\management\commands\limpar_tokens.py                     59     59     0%   13-155
apps\interessados\management\commands\popular_cpf_hash.py                  22     22     0%   9-40
apps\interessados\models.py                                               139     16    88%   29, 41, 135, 138, 141, 144, 147, 151, 158, 162, 166, 172, 188, 191-192, 260
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3058    27%
Coverage HTML written to dir htmlcov


================================================================================= 9 passed in 6.99s =================================================================================




##  apps.dashboard.tests.test_utils_pdf.py em 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/dashboard/tests/test_utils_pdf.py -v  
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 9 items                                                                                                                                           

apps/dashboard/tests/test_utils_pdf.py::TestCriarGraficoPizza::test_dados_validos_retorna_buffer PASSED                                               [ 11%]
apps/dashboard/tests/test_utils_pdf.py::TestCriarGraficoPizza::test_todos_valores_zero_retorna_none PASSED                                            [ 22%]
apps/dashboard/tests/test_utils_pdf.py::TestCriarGraficoPizza::test_lista_vazia_retorna_none PASSED                                                   [ 33%]
apps/dashboard/tests/test_utils_pdf.py::TestCriarGraficoPizza::test_um_item_valido_retorna_buffer PASSED                                              [ 44%]
apps/dashboard/tests/test_utils_pdf.py::TestCriarGraficoBarras::test_dados_validos_retorna_buffer PASSED                                              [ 55%]
apps/dashboard/tests/test_utils_pdf.py::TestGerarPdfInteressados::test_context_minimo_retorna_buffer PASSED                                           [ 66%]
apps/dashboard/tests/test_utils_pdf.py::TestGerarPdfEventos::test_context_minimo_retorna_buffer PASSED                                                [ 77%]
apps/dashboard/tests/test_utils_pdf.py::TestGerarPdfAcademico::test_context_minimo_retorna_buffer PASSED                                              [ 88%]
apps/dashboard/tests/test_utils_pdf.py::TestGerarPdfProcessoSeletivo::test_context_minimo_retorna_buffer PASSED                                       [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
apps\dashboard\utils_pdf.py                                               373     90    76%   86-87, 90-91, 94-99, 102-107, 227-231, 235-239, 243-247, 250-252, 259-263, 267-271, 275-279, 282-284, 288-293, 416-435, 439-459, 583-603, 726-746
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3100    26%
Coverage HTML written to dir htmlcov


==================================================================== 9 passed in 5.03s =====================================================================


##  apps.dashboard.tests.test_views.py

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




##  apps.dashboard.tests.test_services.py em 12/06/2026, 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/dashboard/tests/test_services.py -v   
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 22 items                                                                                                                                          

apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_metricas_gerais PASSED                                         [  4%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_distribuicao_sexo PASSED                                       [  9%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_distribuicao_fototipo PASSED                                   [ 13%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_distribuicao_escolaridade PASSED                               [ 18%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_distribuicao_programas_sociais PASSED                          [ 22%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_distribuicao_deficiencias PASSED                               [ 27%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_tipos_deficiencia PASSED                                       [ 31%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_faixas_etarias PASSED                                          [ 36%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_obter_contexto_completo PASSED                                          [ 40%]
apps/dashboard/tests/test_services.py::TestDashboardEventosService::test_calcular_metricas_gerais PASSED                                              [ 45%]
apps/dashboard/tests/test_services.py::TestDashboardEventosService::test_calcular_turmas_por_status PASSED                                            [ 50%]
apps/dashboard/tests/test_services.py::TestDashboardEventosService::test_calcular_eventos_por_status PASSED                                           [ 54%]
apps/dashboard/tests/test_services.py::TestDashboardEventosService::test_calcular_top_eventos_inscricoes PASSED                                       [ 59%]
apps/dashboard/tests/test_services.py::TestDashboardEventosService::test_obter_contexto_completo PASSED                                               [ 63%]
apps/dashboard/tests/test_services.py::TestDashboardAcademicoService::test_calcular_metricas_avaliacoes PASSED                                        [ 68%]
apps/dashboard/tests/test_services.py::TestDashboardAcademicoService::test_calcular_taxa_aprovacao PASSED                                             [ 72%]
apps/dashboard/tests/test_services.py::TestDashboardAcademicoService::test_calcular_top_cursos_aprovados PASSED                                       [ 77%]
apps/dashboard/tests/test_services.py::TestDashboardAcademicoService::test_obter_contexto_completo PASSED                                             [ 81%]
apps/dashboard/tests/test_services.py::TestDashboardProcessoSeletivoService::test_calcular_metricas_inscricoes PASSED                                 [ 86%]
apps/dashboard/tests/test_services.py::TestDashboardProcessoSeletivoService::test_calcular_metricas_classificacoes PASSED                             [ 90%]
apps/dashboard/tests/test_services.py::TestDashboardProcessoSeletivoService::test_calcular_top_eventos_inscricoes PASSED                              [ 95%]
apps/dashboard/tests/test_services.py::TestDashboardProcessoSeletivoService::test_obter_contexto_completo PASSED                                      [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
TOTAL                                                                    4208   3200    24%
Coverage HTML written to dir htmlcov


=================================================================== 22 passed in 14.68s ====================================================================



##  apps.eventos.tests.test_admin.py em 17/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/eventos/tests/test_admin.py -v  
=============================================================== test session starts ================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 30 items                                                                                                                                  

apps/eventos/tests/test_admin.py::TestEventoAdminConfig::test_list_display PASSED                                                             [  3%]
apps/eventos/tests/test_admin.py::TestEventoAdminConfig::test_list_filter PASSED                                                              [  6%]
apps/eventos/tests/test_admin.py::TestEventoAdminConfig::test_search_fields PASSED                                                            [ 10%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_changelist_carrega PASSED                                                   [ 13%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_busca_por_nome PASSED                                                       [ 16%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_filtrar_por_status PASSED                                                   [ 20%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_paginacao PASSED                                                            [ 23%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_busca_vazia PASSED                                                          [ 26%]
apps/eventos/tests/test_admin.py::TestStatusAdminChangeList::test_changelist_carrega PASSED                                                   [ 30%]
apps/eventos/tests/test_admin.py::TestStatusAdminChangeList::test_busca_por_nome PASSED                                                       [ 33%]
apps/eventos/tests/test_admin.py::TestTurmaAdminChangeList::test_changelist_carrega PASSED                                                    [ 36%]
apps/eventos/tests/test_admin.py::TestTurmaAdminChangeList::test_busca_por_nome PASSED                                                        [ 40%]
apps/eventos/tests/test_admin.py::TestEventoAdminViews::test_add_view PASSED                                                                  [ 43%]
apps/eventos/tests/test_admin.py::TestEventoAdminViews::test_change_view PASSED                                                               [ 46%]
apps/eventos/tests/test_admin.py::TestEventoAdminViews::test_delete_view PASSED                                                               [ 50%]
apps/eventos/tests/test_admin.py::TestStatusAdminViews::test_add_view PASSED                                                                  [ 53%]
apps/eventos/tests/test_admin.py::TestStatusAdminViews::test_change_view PASSED                                                               [ 56%]
apps/eventos/tests/test_admin.py::TestStatusAdminViews::test_delete_view PASSED                                                               [ 60%]
apps/eventos/tests/test_admin.py::TestTurmaAdminViews::test_add_view PASSED                                                                   [ 63%]
apps/eventos/tests/test_admin.py::TestTurmaAdminViews::test_change_view PASSED                                                                [ 66%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_status_colorido PASSED                                                         [ 70%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_vagas_inscritos_sem_inscricoes PASSED                                          [ 73%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_vagas_inscritos_com_inscricoes PASSED                                          [ 76%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_data_inicio_inscricao_formatada PASSED                                         [ 80%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_data_fim_inscricao_formatada PASSED                                            [ 83%]
apps/eventos/tests/test_admin.py::TestEventoAdminInlines::test_exibe_inline_criterios PASSED                                                  [ 86%]
apps/eventos/tests/test_admin.py::TestEventoAdminInlines::test_exibe_inline_turmas PASSED                                                     [ 90%]
apps/eventos/tests/test_admin.py::TestEventoAdminInlines::test_change_view_carrega_com_inlines PASSED                                         [ 93%]
apps/eventos/tests/test_admin.py::TestHorarioAdminChangeList::test_changelist_carrega PASSED                                                  [ 96%]
apps/eventos/tests/test_admin.py::TestHorarioAdminChangeList::test_filtro_dia_semana PASSED                                                   [100%]

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
apps\dashboard\services.py                                                157    105    33%   23-26, 34-43, 47-56, 60-81, 85-93, 108-116, 131-152, 156-199, 203, 220-222, 233-236, 247-249, 255-257, 265, 278-293, 304-311, 315-317, 325-326, 338-343, 367-381, 390-392, 400
apps\dashboard\utils_pdf.py                                               373    350     6%   25-56, 61-80, 86-87, 90-91, 94-99, 102-107, 112-298, 303-464, 469-608, 613-751
apps\dashboard\views.py                                                    71     47    34%   33-42, 47-56, 61-70, 75-84, 89-109, 118-125, 130-137, 142-149, 154-161
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3000    29%
Coverage HTML written to dir htmlcov


=============================================================== 30 passed in 16.95s ================================================================



##  apps/eventos/tests/test_admin_config.py em 22/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/eventos/tests/test_admin_config.py -v                               
=========================================================================== test session starts ===========================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 29 items                                                                                                                                                         

apps/eventos/tests/test_admin_config.py::TestCriterioAdminConfig::test_list_display PASSED                                                                           [  3%]
apps/eventos/tests/test_admin_config.py::TestCriterioAdminConfig::test_list_filter PASSED                                                                            [  6%]
apps/eventos/tests/test_admin_config.py::TestCriterioAdminConfig::test_search_fields PASSED                                                                          [ 10%]
apps/eventos/tests/test_admin_config.py::TestCriterioAdminConfig::test_list_editable PASSED                                                                          [ 13%]
apps/eventos/tests/test_admin_config.py::TestCriterioAdminConfig::test_readonly_fields PASSED                                                                        [ 17%]
apps/eventos/tests/test_admin_config.py::TestCriterioAdminConfig::test_fieldsets PASSED                                                                              [ 20%]
apps/eventos/tests/test_admin_config.py::TestCriterioAdminConfig::test_has_delete_permission_retorna_false PASSED                                                    [ 24%]
apps/eventos/tests/test_admin_config.py::TestTurmaAdminConfig::test_list_display PASSED                                                                              [ 27%]
apps/eventos/tests/test_admin_config.py::TestTurmaAdminConfig::test_list_filter PASSED                                                                               [ 31%]
apps/eventos/tests/test_admin_config.py::TestTurmaAdminConfig::test_search_fields PASSED                                                                             [ 34%]
apps/eventos/tests/test_admin_config.py::TestHorarioAdminConfig::test_list_display PASSED                                                                            [ 37%]
apps/eventos/tests/test_admin_config.py::TestHorarioAdminConfig::test_list_filter PASSED                                                                             [ 41%]
apps/eventos/tests/test_admin_config.py::TestHorarioAdminMethods::test_dia_semana_display PASSED                                                                     [ 44%]
apps/eventos/tests/test_admin_config.py::TestStatusAdminConfig::test_list_editable PASSED                                                                            [ 48%]
apps/eventos/tests/test_admin_config.py::TestStatusAdminConfig::test_ordering PASSED                                                                                 [ 51%]
apps/eventos/tests/test_admin_config.py::TestStatusAdminConfig::test_fieldsets PASSED                                                                                [ 55%]
apps/eventos/tests/test_admin_config.py::TestEventoAdminConfigExtra::test_fieldsets PASSED                                                                           [ 58%]
apps/eventos/tests/test_admin_config.py::TestEventoAdminConfigExtra::test_actions_list PASSED                                                                        [ 62%]
apps/eventos/tests/test_admin_config.py::TestStatusForm::test_widget_color PASSED                                                                                    [ 65%]
apps/eventos/tests/test_admin_config.py::TestEventoCriterioInlineMethods::test_pontos_display_com_pontos PASSED                                                      [ 68%]
apps/eventos/tests/test_admin_config.py::TestEventoCriterioInlineMethods::test_pontos_display_ordenacao PASSED                                                       [ 72%]
apps/eventos/tests/test_admin_config.py::TestEventoCriterioInlineMethods::test_get_queryset_usar_select_related PASSED                                               [ 75%]
apps/eventos/tests/test_admin_config.py::TestEventoCriterioInlineMethods::test_formfield_for_foreignkey_filtra_ativos PASSED                                         [ 79%]
apps/eventos/tests/test_admin_config.py::TestEdgeCases::test_status_colorido_sem_status PASSED                                                                       [ 82%]
apps/eventos/tests/test_admin_config.py::TestEdgeCases::test_data_inicio_inscricao_sem_data PASSED                                                                   [ 86%]
apps/eventos/tests/test_admin_config.py::TestEdgeCases::test_data_fim_inscricao_sem_data PASSED                                                                      [ 89%]
apps/eventos/tests/test_admin_config.py::TestEdgeCases::test_data_inicio_evento_sem_data PASSED                                                                      [ 93%]
apps/eventos/tests/test_admin_config.py::TestEdgeCases::test_data_fim_evento_sem_data PASSED                                                                         [ 96%]
apps/eventos/tests/test_admin_config.py::TestEdgeCases::test_vagas_inscritos_zero_vagas PASSED                                                                       [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
apps\dashboard\utils_pdf.py                                               373    373     0%   9-751
apps\dashboard\views.py                                                    71     71     0%   13-161
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212     88    58%   61-67, 114, 174, 196, 201-204, 219, 230, 241, 252, 269-358, 371-415, 430-519
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       0      0   100%
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4207   3353    20%
Coverage HTML written to dir htmlcov


=========================================================================== 29 passed in 3.18s =================================================================




##  apps.eventos.tests.test_models.py em 17/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/eventos/tests/test_models.py -v
=============================================================== test session starts ================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 22 items                                                                                                                                  

apps/eventos/tests/test_models.py::TestStatusModel::test_create_status PASSED                                                                 [  4%]
apps/eventos/tests/test_models.py::TestStatusModel::test_status_str PASSED                                                                    [  9%]
apps/eventos/tests/test_models.py::TestStatusModel::test_status_ordem_unique PASSED                                                           [ 13%]
apps/eventos/tests/test_models.py::TestStatusModel::test_status_cor_valid_hex PASSED                                                          [ 18%]
apps/eventos/tests/test_models.py::TestEventoModel::test_create_evento PASSED                                                                 [ 22%]
apps/eventos/tests/test_models.py::TestEventoModel::test_evento_str PASSED                                                                    [ 27%]
apps/eventos/tests/test_models.py::TestEventoModel::test_evento_foreign_key_status PASSED                                                     [ 31%]
apps/eventos/tests/test_models.py::TestEventoModel::test_evento_total_vagas_positive PASSED                                                   [ 36%]
apps/eventos/tests/test_models.py::TestEventoModel::test_evento_data_inicio_inscricao_before_fim PASSED                                       [ 40%]
apps/eventos/tests/test_models.py::TestEventoModel::test_evento_data_inicio_evento_before_fim PASSED                                          [ 45%]
apps/eventos/tests/test_models.py::TestEventoModel::test_evento_datas_evento_validas PASSED                                                   [ 50%]
apps/eventos/tests/test_models.py::TestCriterioModel::test_create_criterio PASSED                                                             [ 54%]
apps/eventos/tests/test_models.py::TestCriterioModel::test_criterio_str PASSED                                                                [ 59%]
apps/eventos/tests/test_models.py::TestCriterioModel::test_criterio_codigo_unique PASSED                                                      [ 63%]
apps/eventos/tests/test_models.py::TestCriterioModel::test_criterio_pontos_non_negative PASSED                                                [ 68%]
apps/eventos/tests/test_models.py::TestCriterioModel::test_criterio_categoria_choices PASSED                                                  [ 72%]
apps/eventos/tests/test_models.py::TestTurmaModel::test_create_turma PASSED                                                                   [ 77%]
apps/eventos/tests/test_models.py::TestTurmaModel::test_turma_str PASSED                                                                      [ 81%]
apps/eventos/tests/test_models.py::TestTurmaModel::test_turma_foreign_key_evento PASSED                                                       [ 86%]
apps/eventos/tests/test_models.py::TestTurmaModel::test_turma_capacidade_positive PASSED                                                      [ 90%]
apps/eventos/tests/test_models.py::TestHorarioModel::test_create_horario PASSED                                                               [ 95%]
apps/eventos/tests/test_models.py::TestHorarioModel::test_horario_foreign_key_turma PASSED                                                    [100%]

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
apps\dashboard\services.py                                                157    157     0%   12-400
apps\dashboard\utils_pdf.py                                               373    373     0%   9-751
apps\dashboard\views.py                                                    71     71     0%   13-161
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212    117    45%   61-67, 95, 110-114, 118-119, 122-124, 173-181, 187-206, 218-223, 229-234, 240-245, 251-256, 269-358, 371-415, 430-519, 537
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51     51     0%   8-114
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122     19    84%   106, 130-132, 135-137, 140-142, 145-147, 150-152, 201, 206, 280
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3373    20%
Coverage HTML written to dir htmlcov


================================================================ 22 passed in 4.37s ================================================================



##  apps.eventos.tests.test_context_processors.py em 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/eventos/tests/test_context_processors.py -v          
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 13 items                                                                                                                                          

apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_usuario_anonimo_retorna_lista_vazia PASSED                               [  7%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_usuario_nao_staff_retorna_lista_vazia PASSED                             [ 15%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_sem_eventos_retorna_lista_vazia PASSED                                   [ 23%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao1_status_correto_sem_alerta PASSED                            [ 30%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao1_status_errado_gera_alerta PASSED                            [ 38%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao2_status_valido_sem_alerta PASSED                             [ 46%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao2_status_invalido_gera_alerta PASSED                          [ 53%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao3_status_correto_sem_alerta PASSED                            [ 61%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao3_status_errado_gera_alerta PASSED                            [ 69%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao4_status_valido_sem_alerta PASSED                             [ 76%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao4_status_invalido_gera_alerta PASSED                          [ 84%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao4_cancelado_sem_alerta PASSED                                 [ 92%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_multiplos_eventos_com_alerta PASSED                                      [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
apps\dashboard\utils_pdf.py                                               373    373     0%   9-751
apps\dashboard\views.py                                                    71     71     0%   13-161
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212    117    45%   61-67, 95, 110-114, 118-119, 122-124, 173-181, 187-206, 218-223, 229-234, 240-245, 251-256, 269-358, 371-415, 430-519, 537
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51      3    94%   39, 111-112
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3335    21%
Coverage HTML written to dir htmlcov


==================================================================== 13 passed in 8.13s ====================================================================




##  apps.eventos.tests.test_admin.py em 09/06/2026, 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/eventos/tests/test_admin.py -v
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 30 items                                                                                                                                          

apps/eventos/tests/test_admin.py::TestEventoAdminConfig::test_list_display PASSED                                                                     [  3%]
apps/eventos/tests/test_admin.py::TestEventoAdminConfig::test_list_filter PASSED                                                                      [  6%]
apps/eventos/tests/test_admin.py::TestEventoAdminConfig::test_search_fields PASSED                                                                    [ 10%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_changelist_carrega PASSED                                                           [ 13%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_busca_por_nome PASSED                                                               [ 16%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_filtrar_por_status PASSED                                                           [ 20%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_paginacao PASSED                                                                    [ 23%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_busca_vazia PASSED                                                                  [ 26%]
apps/eventos/tests/test_admin.py::TestStatusAdminChangeList::test_changelist_carrega PASSED                                                           [ 30%]
apps/eventos/tests/test_admin.py::TestStatusAdminChangeList::test_busca_por_nome PASSED                                                               [ 33%]
apps/eventos/tests/test_admin.py::TestTurmaAdminChangeList::test_changelist_carrega PASSED                                                            [ 36%]
apps/eventos/tests/test_admin.py::TestTurmaAdminChangeList::test_busca_por_nome PASSED                                                                [ 40%]
apps/eventos/tests/test_admin.py::TestEventoAdminViews::test_add_view PASSED                                                                          [ 43%]
apps/eventos/tests/test_admin.py::TestEventoAdminViews::test_change_view PASSED                                                                       [ 46%]
apps/eventos/tests/test_admin.py::TestEventoAdminViews::test_delete_view PASSED                                                                       [ 50%]
apps/eventos/tests/test_admin.py::TestStatusAdminViews::test_add_view PASSED                                                                          [ 53%]
apps/eventos/tests/test_admin.py::TestStatusAdminViews::test_change_view PASSED                                                                       [ 56%]
apps/eventos/tests/test_admin.py::TestStatusAdminViews::test_delete_view PASSED                                                                       [ 60%]
apps/eventos/tests/test_admin.py::TestTurmaAdminViews::test_add_view PASSED                                                                           [ 63%]
apps/eventos/tests/test_admin.py::TestTurmaAdminViews::test_change_view PASSED                                                                        [ 66%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_status_colorido PASSED                                                                 [ 70%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_vagas_inscritos_sem_inscricoes PASSED                                                  [ 73%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_vagas_inscritos_com_inscricoes PASSED                                                  [ 76%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_data_inicio_inscricao_formatada PASSED                                                 [ 80%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_data_fim_inscricao_formatada PASSED                                                    [ 83%]
apps/eventos/tests/test_admin.py::TestEventoAdminInlines::test_exibe_inline_criterios PASSED                                                          [ 86%]
apps/eventos/tests/test_admin.py::TestEventoAdminInlines::test_exibe_inline_turmas PASSED                                                             [ 90%]
apps/eventos/tests/test_admin.py::TestEventoAdminInlines::test_change_view_carrega_com_inlines PASSED                                                 [ 93%]
apps/eventos/tests/test_admin.py::TestHorarioAdminChangeList::test_changelist_carrega PASSED                                                          [ 96%]
apps/eventos/tests/test_admin.py::TestHorarioAdminChangeList::test_filtro_dia_semana PASSED                                                           [100%]

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
apps\accounts\admin.py                                                     52     16    69%   50-65, 141-158
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
apps\dashboard\services.py                                                157    105    33%   23-26, 34-43, 47-56, 60-81, 85-93, 108-116, 131-152, 156-199, 203, 220-222, 233-236, 247-249, 255-257, 265, 278-293, 304-311, 315-317, 325-326, 338-343, 367-381, 390-392, 400
apps\dashboard\utils_pdf.py                                               373    350     6%   25-56, 61-80, 86-87, 90-91, 94-99, 102-107, 112-298, 303-464, 469-608, 613-751
apps\dashboard\views.py                                                    71     47    34%   33-42, 47-56, 61-70, 75-84, 89-109, 118-125, 130-137, 142-149, 154-161
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3000    29%
Coverage HTML written to dir htmlcov


=================================================================== 30 passed in 16.88s ====================================================================




##  apps.eventos.tests.test_models_evento_expanded.py em 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/eventos/tests/test_models_evento_expanded.py -v
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 15 items                                                                                                                                          

apps/eventos/tests/test_models_evento_expanded.py::TestEventoCreation::test_criar_evento PASSED                                                       [  6%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoCreation::test_str_evento PASSED                                                         [ 13%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoCreation::test_defaults_evento PASSED                                                    [ 20%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoCreation::test_status_evento PASSED                                                      [ 26%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoCreation::test_multiplos_eventos PASSED                                                  [ 33%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoDatas::test_fim_inscricao_antes_inicio PASSED                                   [ 40%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoDatas::test_fim_evento_antes_inicio PASSED                                      [ 46%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoDatas::test_datas_validas PASSED                                                [ 53%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoDatas::test_datas_iguais PASSED                                                 [ 60%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoVagas::test_vagas_negativas PASSED                                              [ 66%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoVagas::test_vagas_altas PASSED                                                  [ 73%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoRelacionamentos::test_has_status PASSED                                                  [ 80%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoRelacionamentos::test_status_has_eventos PASSED                                          [ 86%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoRelacionamentos::test_protect_status PASSED                                              [ 93%]
apps/eventos/tests/test_models_evento_expanded.py::TestTurmaHorario::test_turma_horario_relation PASSED                                               [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
apps\dashboard\utils_pdf.py                                               373    373     0%   9-751
apps\dashboard\views.py                                                    71     71     0%   13-161
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3377    20%
Coverage HTML written to dir htmlcov


==================================================================== 15 passed in 3.01s ====================================================================



##  apps.eventos.tests.test_models_evento.py em 09/06/2026, 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/eventos/tests/test_models_evento.py -v         
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 35 items                                                                                                                                          

apps/eventos/tests/test_models_evento.py::TestEventoCRUD::test_criar_evento_valido PASSED                                                             [  2%]
apps/eventos/tests/test_models_evento.py::TestEventoCRUD::test_ler_evento PASSED                                                                      [  5%]
apps/eventos/tests/test_models_evento.py::TestEventoCRUD::test_atualizar_evento PASSED                                                                [  8%]
apps/eventos/tests/test_models_evento.py::TestEventoCRUD::test_deletar_evento PASSED                                                                  [ 11%]
apps/eventos/tests/test_models_evento.py::TestEventoCRUD::test_multiplos_eventos PASSED                                                               [ 14%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_data_inicio_inscricao_antes_fim_inscricao PASSED                                 [ 17%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_data_fim_inscricao_antes_inicio_evento PASSED                                    [ 20%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_data_inicio_evento_antes_fim_evento PASSED                                       [ 22%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_datas_validas_factory PASSED                                                     [ 25%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_clean_valida_datas PASSED                                                        [ 28%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_total_vagas_positivo PASSED                                                      [ 31%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_total_vagas_grande_numero PASSED                                                 [ 34%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_total_vagas_zero_permitido PASSED                                                [ 37%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_com_status PASSED                                                             [ 40%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_sem_status_invalido PASSED                                                    [ 42%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_com_turmas PASSED                                                             [ 45%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_multiplas_turmas PASSED                                                       [ 48%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_com_criterios PASSED                                                          [ 51%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_multiplos_criterios PASSED                                                    [ 54%]
apps/eventos/tests/test_models_evento.py::TestEventoTimestamps::test_evento_sem_criterios PASSED                                                      [ 57%]
apps/eventos/tests/test_models_evento.py::TestEventoTimestamps::test_deletar_evento_deleta_turmas PASSED                                              [ 60%]
apps/eventos/tests/test_models_evento.py::TestEventoTimestamps::test_criado_em_existe PASSED                                                          [ 62%]
apps/eventos/tests/test_models_evento.py::TestEventoTimestamps::test_atualizado_em_existe PASSED                                                      [ 65%]
apps/eventos/tests/test_models_evento.py::TestEventoTimestamps::test_atualizado_em_atualiza PASSED                                                    [ 68%]
apps/eventos/tests/test_models_evento.py::TestEventoMetodos::test_inscricoes_abertas PASSED                                                           [ 71%]
apps/eventos/tests/test_models_evento.py::TestEventoMetodos::test_inscricoes_fechadas PASSED                                                          [ 74%]
apps/eventos/tests/test_models_evento.py::TestEventoMetodos::test_validacao_datas_inscricao PASSED                                                    [ 77%]
apps/eventos/tests/test_models_evento.py::TestEventoMetodos::test_validacao_datas_evento PASSED                                                       [ 80%]
apps/eventos/tests/test_models_evento.py::TestEventoMetodos::test_formatacao_datas PASSED                                                             [ 82%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_filtro_por_status PASSED                                                           [ 85%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_filtro_por_ativo PASSED                                                            [ 88%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_queryset_count PASSED                                                              [ 91%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_queryset_exists PASSED                                                             [ 94%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_nome_obrigatorio PASSED                                                            [ 97%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_str_representation PASSED                                                          [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
apps\dashboard\utils_pdf.py                                               373    373     0%   9-751
apps\dashboard\views.py                                                    71     71     0%   13-161
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3366    20%
Coverage HTML written to dir htmlcov


==================================================================== 35 passed in 2.85s ====================================================================




##  apps.eventos.tests.test_models_turma.py em 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/eventos/tests/test_models_turma.py -v 
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 21 items                                                                                                                                          

apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_criar_turma_valida PASSED                                                               [  4%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_ler_turma PASSED                                                                        [  9%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_atualizar_turma PASSED                                                                  [ 14%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_deletar_turma PASSED                                                                    [ 19%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_multiplas_turmas PASSED                                                                 [ 23%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_datas_validas_factory PASSED                                                            [ 28%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_capacidade_positiva PASSED                                                              [ 33%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_capacidade_grande_numero PASSED                                                         [ 38%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_capacidade_zero_permitido PASSED                                                        [ 42%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_turma_com_evento PASSED                                                                 [ 47%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_turma_sem_evento_invalido PASSED                                                        [ 52%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_turma_com_horarios PASSED                                                               [ 57%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_turma_multiplos_horarios PASSED                                                         [ 61%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_deletar_turma_deleta_horarios PASSED                                                    [ 66%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_criado_em_existe PASSED                                                                 [ 71%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_atualizado_em_atualiza PASSED                                                           [ 76%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_str_representation PASSED                                                               [ 80%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_nome_obrigatorio PASSED                                                                 [ 85%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_filtro_por_evento PASSED                                                                [ 90%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_filtro_por_turno PASSED                                                                 [ 95%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_queryset_count PASSED                                                                   [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
apps\dashboard\utils_pdf.py                                               373    373     0%   9-751
apps\dashboard\views.py                                                    71     71     0%   13-161
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212    117    45%   61-67, 95, 110-114, 118-119, 122-124, 173-181, 187-206, 218-223, 229-234, 240-245, 251-256, 269-358, 371-415, 430-519, 537
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51     51     0%   8-114
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122     28    77%   28, 104-106, 127, 130-132, 135-137, 140-142, 145-147, 150-152, 155-160, 201, 206, 280
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3382    20%
Coverage HTML written to dir htmlcov


==================================================================== 21 passed in 2.76s ====================================================================


##  apps.eventos.tests.test_models_horario.py em 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/eventos/tests/test_models_horario.py -v
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 14 items                                                                                                                                          

apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_criar_horario_valido PASSED                                                         [  7%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_ler_horario PASSED                                                                  [ 14%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_atualizar_horario PASSED                                                            [ 21%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_deletar_horario PASSED                                                              [ 28%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_dia_semana_valido PASSED                                                            [ 35%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_multiplos_horarios_mesma_turma PASSED                                               [ 42%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_hora_inicio_antes_fim PASSED                                                        [ 50%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_hora_inicio_igual_fim_permitido PASSED                                              [ 57%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_horario_com_turma PASSED                                                            [ 64%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_horario_sem_turma_invalido PASSED                                                   [ 71%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_turma_tem_multiplos_horarios PASSED                                                 [ 78%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_str_representation PASSED                                                           [ 85%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_filtro_por_turma PASSED                                                             [ 92%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_queryset_count PASSED                                                               [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
apps\dashboard\utils_pdf.py                                               373    373     0%   9-751
apps\dashboard\views.py                                                    71     71     0%   13-161
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212    117    45%   61-67, 95, 110-114, 118-119, 122-124, 173-181, 187-206, 218-223, 229-234, 240-245, 251-256, 269-358, 371-415, 430-519, 537
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51     51     0%   8-114
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122     28    77%   28, 104-106, 127, 130-132, 135-137, 140-142, 145-147, 150-152, 155-160, 201, 206, 247
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3382    20%
Coverage HTML written to dir htmlcov


==================================================================== 14 passed in 2.77s ====================================================================



##  apps.eventos.tests.test_models_criterio.py em 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/eventos/tests/test_models_criterio.py -v
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 15 items                                                                                                                                          

apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_criar_criterio_valido PASSED                                                      [  6%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_ler_criterio PASSED                                                               [ 13%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_atualizar_criterio PASSED                                                         [ 20%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_deletar_criterio PASSED                                                           [ 26%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_codigo_unico PASSED                                                               [ 33%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_codigo_valido PASSED                                                              [ 40%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_pontos_positivo PASSED                                                            [ 46%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_pontos_zero_permitido PASSED                                                      [ 53%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_criterio_ativo_padrao PASSED                                                      [ 60%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_criterio_inativo PASSED                                                           [ 66%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_criterio_com_eventos PASSED                                                       [ 73%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_criterio_sem_eventos PASSED                                                       [ 80%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_str_representation PASSED                                                         [ 86%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_filtro_por_ativo PASSED                                                           [ 93%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_queryset_count PASSED                                                             [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
apps\dashboard\utils_pdf.py                                               373    373     0%   9-751
apps\dashboard\views.py                                                    71     71     0%   13-161
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212    117    45%   61-67, 95, 110-114, 118-119, 122-124, 173-181, 187-206, 218-223, 229-234, 240-245, 251-256, 269-358, 371-415, 430-519, 537
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51     51     0%   8-114
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122     27    78%   28, 106, 127, 130-132, 135-137, 140-142, 145-147, 150-152, 155-160, 201, 206, 247, 280
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3381    20%
Coverage HTML written to dir htmlcov


==================================================================== 15 passed in 2.68s ====================================================================



##  apps.interessados.tests.test_forms.py em 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/interessados/tests/test_forms.py -v
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 19 items                                                                                                                                          

apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_valido_dados_minimos PASSED                                         [  5%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_cpf_duplicado PASSED                                                [ 10%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_email_duplicado PASSED                                              [ 15%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_senhas_nao_conferem PASSED                                          [ 21%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_cpf_invalido_todos_iguais PASSED                                    [ 26%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cpf_valido_com_pontuacao PASSED                                              [ 31%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cpf_invalido_digito_verificador PASSED                                       [ 36%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cpf_muito_curto PASSED                                                       [ 42%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_sem_consentimento_lgpd PASSED                                       [ 47%]
apps/interessados/tests/test_forms.py::TestLoginInteressadoForm::test_login_valido PASSED                                                             [ 52%]
apps/interessados/tests/test_forms.py::TestLoginInteressadoForm::test_login_cpf_nao_cadastrado PASSED                                                 [ 57%]
apps/interessados/tests/test_forms.py::TestLoginInteressadoForm::test_login_senha_incorreta PASSED                                                    [ 63%]
apps/interessados/tests/test_forms.py::TestLoginInteressadoForm::test_login_interessado_inativo PASSED                                                [ 68%]
apps/interessados/tests/test_forms.py::TestLoginInteressadoForm::test_login_cpf_formatado_com_pontuacao PASSED                                        [ 73%]
apps/interessados/tests/test_forms.py::TestEdicaoInteressadoForm::test_edicao_valida_dados_minimos PASSED                                             [ 78%]
apps/interessados/tests/test_forms.py::TestEdicaoInteressadoForm::test_cpf_nao_aparece_na_edicao PASSED                                               [ 84%]
apps/interessados/tests/test_forms.py::TestEdicaoInteressadoForm::test_tentativa_alterar_cpf_ignorada PASSED                                          [ 89%]
apps/interessados/tests/test_forms.py::TestEdicaoInteressadoForm::test_edicao_sem_nome_rejeita PASSED                                                 [ 94%]
apps/interessados/tests/test_forms.py::TestEdicaoInteressadoForm::test_edicao_email_invalido_rejeita PASSED                                           [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
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
apps\interessados\forms.py                                                157     21    87%   170-171, 203, 222, 227, 242, 287-302, 395-396, 409, 447, 452
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3245    23%
Coverage HTML written to dir htmlcov


=================================================================== 19 passed in 10.31s ====================================================================




##  apps.interessados.tests.test_forms.py em 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/interessados/tests/test_forms.py -v
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 19 items                                                                                                                                          

apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_valido_dados_minimos PASSED                                         [  5%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_cpf_duplicado PASSED                                                [ 10%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_email_duplicado PASSED                                              [ 15%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_senhas_nao_conferem PASSED                                          [ 21%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_cpf_invalido_todos_iguais PASSED                                    [ 26%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cpf_valido_com_pontuacao PASSED                                              [ 31%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cpf_invalido_digito_verificador PASSED                                       [ 36%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cpf_muito_curto PASSED                                                       [ 42%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_sem_consentimento_lgpd PASSED                                       [ 47%]
apps/interessados/tests/test_forms.py::TestLoginInteressadoForm::test_login_valido PASSED                                                             [ 52%]
apps/interessados/tests/test_forms.py::TestLoginInteressadoForm::test_login_cpf_nao_cadastrado PASSED                                                 [ 57%]
apps/interessados/tests/test_forms.py::TestLoginInteressadoForm::test_login_senha_incorreta PASSED                                                    [ 63%]
apps/interessados/tests/test_forms.py::TestLoginInteressadoForm::test_login_interessado_inativo PASSED                                                [ 68%]
apps/interessados/tests/test_forms.py::TestLoginInteressadoForm::test_login_cpf_formatado_com_pontuacao PASSED                                        [ 73%]
apps/interessados/tests/test_forms.py::TestEdicaoInteressadoForm::test_edicao_valida_dados_minimos PASSED                                             [ 78%]
apps/interessados/tests/test_forms.py::TestEdicaoInteressadoForm::test_cpf_nao_aparece_na_edicao PASSED                                               [ 84%]
apps/interessados/tests/test_forms.py::TestEdicaoInteressadoForm::test_tentativa_alterar_cpf_ignorada PASSED                                          [ 89%]
apps/interessados/tests/test_forms.py::TestEdicaoInteressadoForm::test_edicao_sem_nome_rejeita PASSED                                                 [ 94%]
apps/interessados/tests/test_forms.py::TestEdicaoInteressadoForm::test_edicao_email_invalido_rejeita PASSED                                           [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
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
apps\interessados\forms.py                                                157     21    87%   170-171, 203, 222, 227, 242, 287-302, 395-396, 409, 447, 452
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3245    23%
Coverage HTML written to dir htmlcov


=================================================================== 19 passed in 10.05s ====================================================================




##  apps.interessados.tests.test_models.py em 16/06/2026, 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/interessados/tests/test_models.py -v
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 38 items                                                                                                                                          

apps/interessados/tests/test_models.py::TestHashCPF::test_mesmo_cpf_mesmo_hash PASSED                                                                 [  2%]
apps/interessados/tests/test_models.py::TestHashCPF::test_cpfs_diferentes_hashes_diferentes PASSED                                                    [  5%]
apps/interessados/tests/test_models.py::TestHashCPF::test_hash_tem_64_caracteres PASSED                                                               [  7%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_senha_nao_e_texto_puro PASSED                                                      [ 10%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_check_password_ok PASSED                                                           [ 13%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_check_password_errado PASSED                                                       [ 15%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_is_authenticated PASSED                                                            [ 18%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_is_anonymous PASSED                                                                [ 21%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_str_contem_nome PASSED                                                             [ 23%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_cpf_criptografado_no_banco PASSED                                                  [ 26%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_cpf_hash_unico PASSED                                                              [ 28%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_cpf_hash_busca_eficiente PASSED                                                    [ 31%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_nis_criptografado_no_banco PASSED                                                  [ 34%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_factory_cria_interessado_valido PASSED                                             [ 36%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_cpf_11_digitos_valido PASSED                                                       [ 39%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_cpf_formatado_aceito_pelo_model PASSED                                             [ 42%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_nis_valido PASSED                                                                  [ 44%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_nis_muito_curto_rejeita PASSED                                                     [ 47%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_cep_valido PASSED                                                                  [ 50%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_cep_muito_curto_rejeita PASSED                                                     [ 52%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_relacionamento_sexo PASSED                                                         [ 55%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_relacionamento_fototipo PASSED                                                     [ 57%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_relacionamentos_simultaneos PASSED                                                 [ 60%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_multiplas_deficiencias PASSED                                                      [ 63%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_tem_deficiencia_property PASSED                                                    [ 65%]
apps/interessados/tests/test_models.py::TestSolicitacaoExclusao::test_criada_com_status_pendente PASSED                                               [ 68%]
apps/interessados/tests/test_models.py::TestSolicitacaoExclusao::test_todos_os_status_sao_validos PASSED                                              [ 71%]
apps/interessados/tests/test_models.py::TestSolicitacaoExclusao::test_nome_solicitante_obrigatorio PASSED                                             [ 73%]
apps/interessados/tests/test_models.py::TestSolicitacaoExclusao::test_email_solicitante_opcional PASSED                                               [ 76%]
apps/interessados/tests/test_models.py::TestSolicitacaoExclusao::test_str_contem_status_e_nome PASSED                                                 [ 78%]
apps/interessados/tests/test_models.py::TestSexoModel::test_factory_cria_valido PASSED                                                                [ 81%]
apps/interessados/tests/test_models.py::TestSexoModel::test_str_retorna_nome PASSED                                                                   [ 84%]
apps/interessados/tests/test_models.py::TestSexoModel::test_unique_constraint_violado PASSED                                                          [ 86%]
apps/interessados/tests/test_models.py::TestFototipoModel::test_factory_cria_valido PASSED                                                            [ 89%]
apps/interessados/tests/test_models.py::TestFototipoModel::test_descricao_pode_ser_vazia PASSED                                                       [ 92%]
apps/interessados/tests/test_models.py::TestPasswordResetTokenModel::test_factory_cria_token_valido PASSED                                            [ 94%]
apps/interessados/tests/test_models.py::TestPasswordResetTokenModel::test_expiracao_futura PASSED                                                     [ 97%]
apps/interessados/tests/test_models.py::TestPasswordResetTokenModel::test_marca_como_usado PASSED                                                     [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
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
apps\interessados\models.py                                               139     10    93%   41, 138, 141, 144, 147, 158, 162, 188, 191-192
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3374    20%
Coverage HTML written to dir htmlcov


=================================================================== 38 passed in 18.17s ====================================================================




##  apps.interessados.tests.test_views.py em 16/06/2026, 19/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/interessados/tests/test_views.py -v --tb=short
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 48 items                                                                                                                                          

apps/interessados/tests/test_views.py::TestCadastroView::test_get_retorna_200 PASSED                                                                  [  2%]
apps/interessados/tests/test_views.py::TestCadastroView::test_post_valido_redirect_login PASSED                                                       [  4%]
apps/interessados/tests/test_views.py::TestCadastroView::test_post_com_dados_completos PASSED                                                         [  6%]
apps/interessados/tests/test_views.py::TestCadastroView::test_post_invalido_mostra_erro PASSED                                                        [  8%]
apps/interessados/tests/test_views.py::TestCadastroView::test_rejeita_senha_fraca PASSED                                                              [ 10%]
apps/interessados/tests/test_views.py::TestLoginView::test_get_retorna_200 PASSED                                                                     [ 12%]
apps/interessados/tests/test_views.py::TestLoginView::test_post_valido_redirect_dashboard PASSED                                                      [ 14%]
apps/interessados/tests/test_views.py::TestLoginView::test_post_inativo_mostra_erro PASSED                                                            [ 16%]
apps/interessados/tests/test_views.py::TestLoginView::test_post_senha_errada_mostra_erro PASSED                                                       [ 18%]
apps/interessados/tests/test_views.py::TestLoginView::test_sql_injection PASSED                                                                       [ 20%]
apps/interessados/tests/test_views.py::TestLoginView::test_nao_expoe_mensagem_diferenciada PASSED                                                     [ 22%]
apps/interessados/tests/test_views.py::TestLogoutView::test_logout_limpa_sessao PASSED                                                                [ 25%]
apps/interessados/tests/test_views.py::TestLogoutView::test_logout_redirect_login PASSED                                                              [ 27%]
apps/interessados/tests/test_views.py::TestDashboardView::test_sem_login_redirect PASSED                                                              [ 29%]
apps/interessados/tests/test_views.py::TestDashboardView::test_inativo_redirect PASSED                                                                [ 31%]
apps/interessados/tests/test_views.py::TestDashboardView::test_valido_retorna_200 PASSED                                                              [ 33%]
apps/interessados/tests/test_views.py::TestDashboardView::test_context_tem_chaves_esperadas PASSED                                                    [ 35%]
apps/interessados/tests/test_views.py::TestMeusDadosView::test_sem_login_redirect PASSED                                                              [ 37%]
apps/interessados/tests/test_views.py::TestMeusDadosView::test_get_valido_retorna_200 PASSED                                                          [ 39%]
apps/interessados/tests/test_views.py::TestMeusDadosView::test_edicao_valida_redirect PASSED                                                          [ 41%]
apps/interessados/tests/test_views.py::TestMeusDadosView::test_edicao_sem_nome_rejeita PASSED                                                         [ 43%]
apps/interessados/tests/test_views.py::TestDetalhesView::test_sem_login_redirect PASSED                                                               [ 45%]
apps/interessados/tests/test_views.py::TestDetalhesView::test_valido_retorna_200 PASSED                                                               [ 47%]
apps/interessados/tests/test_views.py::TestDetalhesView::test_inscricao_alheia_404 PASSED                                                             [ 50%]
apps/interessados/tests/test_views.py::TestInscreverEventoView::test_sem_login_redirect PASSED                                                        [ 52%]
apps/interessados/tests/test_views.py::TestInscreverEventoView::test_evento_inexistente_redirect_com_erro PASSED                                      [ 54%]
apps/interessados/tests/test_views.py::TestInscreverEventoView::test_inscricao_valida_redirect PASSED                                                 [ 56%]
apps/interessados/tests/test_views.py::TestInscreverEventoView::test_duplicata_mostra_aviso PASSED                                                    [ 58%]
apps/interessados/tests/test_views.py::TestSenhaRecuperarView::test_get_retorna_200 PASSED                                                            [ 60%]
apps/interessados/tests/test_views.py::TestSenhaRecuperarView::test_post_cpf_com_email_redirect_envio PASSED                                          [ 62%]
apps/interessados/tests/test_views.py::TestSenhaRecuperarView::test_post_cpf_sem_email_redirect_sem_email PASSED                                      [ 64%]
apps/interessados/tests/test_views.py::TestSenhaRecuperarView::test_post_cpf_inexistente_mostra_erro PASSED                                           [ 66%]
apps/interessados/tests/test_views.py::TestSenhaRecuperarView::test_falha_envio_email_mostra_erro PASSED                                              [ 68%]
apps/interessados/tests/test_views.py::TestSenhaRecuperarEnviadoView::test_get_retorna_200 PASSED                                                     [ 70%]
apps/interessados/tests/test_views.py::TestSenhaRedefinirView::test_token_valido_retorna_200 PASSED                                                   [ 72%]
apps/interessados/tests/test_views.py::TestSenhaRedefinirView::test_post_valido_redirect_concluido PASSED                                             [ 75%]
apps/interessados/tests/test_views.py::TestSenhaRedefinirView::test_token_expirado_mostra_tela_erro PASSED                                            [ 77%]
apps/interessados/tests/test_views.py::TestSenhaRedefinirView::test_token_ja_usado_mostra_tela_erro PASSED                                            [ 79%]
apps/interessados/tests/test_views.py::TestSenhaRedefinirView::test_post_senha_curta_mostra_erro PASSED                                               [ 81%]
apps/interessados/tests/test_views.py::TestSenhaRedefinirView::test_post_senhas_diferentes_mostra_erro PASSED                                         [ 83%]
apps/interessados/tests/test_views.py::TestSenhaRedefinirConcluidoView::test_get_retorna_200 PASSED                                                   [ 85%]
apps/interessados/tests/test_views.py::TestSenhaSemEmailView::test_get_retorna_200 PASSED                                                             [ 87%]
apps/interessados/tests/test_views.py::TestTrocarSenhaObrigatorioView::test_sem_login_redirect PASSED                                                 [ 89%]
apps/interessados/tests/test_views.py::TestTrocarSenhaObrigatorioView::test_sem_must_change_redirect_dashboard PASSED                                 [ 91%]
apps/interessados/tests/test_views.py::TestTrocarSenhaObrigatorioView::test_com_must_change_retorna_200 PASSED                                        [ 93%]
apps/interessados/tests/test_views.py::TestTrocarSenhaObrigatorioView::test_post_valido_redirect_dashboard PASSED                                     [ 95%]
apps/interessados/tests/test_views.py::TestTrocarSenhaObrigatorioView::test_post_senha_curta_mostra_erro PASSED                                       [ 97%]
apps/interessados/tests/test_views.py::TestTrocarSenhaObrigatorioView::test_post_senhas_diferentes_mostra_erro PASSED                                 [100%]

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
apps\accounts\admin.py                                                     52     16    69%   50-65, 141-158
apps\accounts\apps.py                                                       5      0   100%
apps\accounts\forms.py                                                      5      5     0%   8-27
apps\accounts\middleware.py                                                20      5    75%   68, 76-81
apps\accounts\models.py                                                    22      4    82%   103-106
apps\accounts\urls.py                                                       5      0   100%
apps\accounts\views.py                                                     47     38    19%   26-52, 60-62, 83-114
apps\accounts\views_exclusao.py                                            77     66    14%   19, 25-33, 43-83, 94-125
apps\dashboard\__init__.py                                                  0      0   100%
apps\dashboard\admin.py                                                     0      0   100%
apps\dashboard\apps.py                                                      4      0   100%
apps\dashboard\models.py                                                    1      0   100%
apps\dashboard\services.py                                                157    105    33%   23-26, 34-43, 47-56, 60-81, 85-93, 108-116, 131-152, 156-199, 203, 220-222, 233-236, 247-249, 255-257, 265, 278-293, 304-311, 315-317, 325-326, 338-343, 367-381, 390-392, 400
apps\dashboard\utils_pdf.py                                               373    350     6%   25-56, 61-80, 86-87, 90-91, 94-99, 102-107, 112-298, 303-464, 469-608, 613-751
apps\dashboard\views.py                                                    71     47    34%   33-42, 47-56, 61-70, 75-84, 89-109, 118-125, 130-137, 142-149, 154-161
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212    117    45%   61-67, 95, 110-114, 118-119, 122-124, 173-181, 187-206, 218-223, 229-234, 240-245, 251-256, 269-358, 371-415, 430-519, 537
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51     46    10%   27-114
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122     29    76%   28, 104-106, 127, 130-132, 135-137, 140-142, 145-147, 150-152, 155-160, 201, 206, 247, 280
apps\eventos\views.py                                                       1      1     0%   1
apps\interessados\__init__.py                                               0      0   100%
apps\interessados\admin.py                                                218    120    45%   178-183, 188, 193-194, 201-207, 216-222, 231-243, 248-260, 265-269, 280-282, 296-316, 329-330, 337-338, 347-431, 475, 480-481, 485-500, 509, 514, 523-527, 535-538, 546-552, 564, 567, 570
apps\interessados\apps.py                                                   5      0   100%
apps\interessados\authentication.py                                        25     15    40%   33-52, 72-73
apps\interessados\forms.py                                                157     16    90%   185, 189, 195, 197, 203, 205, 209, 227, 229, 242, 279, 395-396, 409, 447, 452
apps\interessados\management\__init__.py                                    0      0   100%
apps\interessados\management\commands\__init__.py                           0      0   100%
apps\interessados\management\commands\criptografar_cpfs.py                 22     22     0%   11-47
apps\interessados\management\commands\limpar_tokens.py                     59     59     0%   13-155
apps\interessados\management\commands\popular_cpf_hash.py                  22     22     0%   9-40
apps\interessados\models.py                                               139     15    89%   29, 41, 135, 138, 141, 144, 147, 151, 162, 166, 172, 188, 191-192, 260
apps\interessados\urls.py                                                   5      0   100%
apps\interessados\utils.py                                                 14     14     0%   10-38
apps\interessados\views.py                                                202     25    88%   60-61, 88-92, 132-134, 197-199, 209-210, 233-235, 247-248, 269-271, 282-286, 290-295
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
apps\scripts_admin\management\commands\configurar_criterios_evento.py      57     57     0%   5-91
apps\scripts_admin\management\commands\popular_criterios.py                21     21     0%   4-117
apps\scripts_admin\management\commands\popular_dados_iniciais.py           66     66     0%   8-234
apps\selecao\__init__.py                                                    0      0   100%
apps\selecao\admin.py                                                     275    163    41%   66-72, 87, 110-115, 152, 223, 233, 240-241, 247, 254-255, 266-275, 293-456, 466-503, 507-544, 552, 558, 564, 570, 580, 586, 592, 598, 608, 612, 616, 661, 667, 673, 677
apps\selecao\apps.py                                                        5      0   100%
apps\selecao\managem




##  apps.interessados.tests.test_admin.py em 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/interessados/tests/test_admin.py -v
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 39 items                                                                                                                                          

apps/interessados/tests/test_admin.py::TestSexoAdmin::test_list_display PASSED                                                                        [  2%]
apps/interessados/tests/test_admin.py::TestSexoAdmin::test_search_fields PASSED                                                                       [  5%]
apps/interessados/tests/test_admin.py::TestFototipoAdmin::test_list_display PASSED                                                                    [  7%]
apps/interessados/tests/test_admin.py::TestFototipoAdmin::test_search_fields PASSED                                                                   [ 10%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_data_nascimento_formatada_com_data PASSED                                    [ 12%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_data_nascimento_formatada_sem_data PASSED                                    [ 15%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_sexo_display_com_sexo PASSED                                                 [ 17%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_sexo_display_sem_sexo PASSED                                                 [ 20%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_fototipo_display_com_fototipo PASSED                                         [ 23%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_fototipo_display_sem_fototipo PASSED                                         [ 25%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_programa_social_display_true PASSED                                          [ 28%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_programa_social_display_false PASSED                                         [ 30%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_necessidades_especiais_display_true PASSED                                   [ 33%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_necessidades_especiais_display_false PASSED                                  [ 35%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_celular_formatado_11_digitos PASSED                                          [ 38%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_celular_formatado_vazio PASSED                                               [ 41%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_telefone_formatado_10_digitos PASSED                                         [ 43%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_telefone_formatado_vazio PASSED                                              [ 46%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_is_active_display_ativo PASSED                                               [ 48%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_is_active_display_inativo PASSED                                             [ 51%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_short_descriptions PASSED                                                    [ 53%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminSaveModel::test_save_model_com_senha_nova_aplica_set_password PASSED                       [ 56%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminActions::test_ativar_interessados PASSED                                                   [ 58%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminActions::test_desativar_interessados PASSED                                                [ 61%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminActions::test_gerar_senha_provisoria_rejeita_multiplos PASSED                              [ 64%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminActions::test_gerar_senha_provisoria_um_interessado PASSED                                 [ 66%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminActions::test_exportar_interessados_retorna_csv PASSED                                     [ 69%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminActions::test_exportar_interessados_conteudo_tem_cabecalho PASSED                          [ 71%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_get_interessado_retorna_nome PASSED                                          [ 74%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_get_status_valido PASSED                                                     [ 76%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_get_status_expirado PASSED                                                   [ 79%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_get_status_usado PASSED                                                      [ 82%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_limpar_tokens_expirados PASSED                                               [ 84%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_limpar_tokens_usados PASSED                                                  [ 87%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_limpar_todos_invalidos PASSED                                                [ 89%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_has_add_permission_false PASSED                                              [ 92%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_has_change_permission_false PASSED                                           [ 94%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_has_delete_permission_superuser_true PASSED                                  [ 97%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_has_delete_permission_normal_user_false PASSED                               [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
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
apps\interessados\admin.py                                                218     20    91%   235-238, 251, 255, 367, 380, 413-421, 480-481, 509, 514
apps\interessados\apps.py                                                   5      0   100%
apps\interessados\authentication.py                                        25     25     0%   9-73
apps\interessados\forms.py                                                157    157     0%   20-453
apps\interessados\management\__init__.py                                    0      0   100%
apps\interessados\management\commands\__init__.py                           0      0   100%
apps\interessados\management\commands\criptografar_cpfs.py                 22     22     0%   11-47
apps\interessados\management\commands\limpar_tokens.py                     59     59     0%   13-155
apps\interessados\management\commands\popular_cpf_hash.py                  22     22     0%   9-40
apps\interessados\models.py                                               139     15    89%   29, 41, 138, 141, 144, 147, 151, 155, 158, 162, 172, 188, 191-192, 260
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3279    22%
Coverage HTML written to dir htmlcov


=================================================================== 39 passed in 26.94s ====================================================================




##  apps.interessados.tests.test_authentication.py em 16/06/2026, 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/interessados/tests/test_authentication.py -v
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 10 items                                                                                                                                          

apps/interessados/tests/test_authentication.py::TestInteressadoBackendAuthenticate::test_autentica_com_cpf_e_senha_validos PASSED                     [ 10%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendAuthenticate::test_autentica_com_senha_errada_retorna_none PASSED               [ 20%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendAuthenticate::test_autentica_com_cpf_inexistente_retorna_none PASSED            [ 30%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendAuthenticate::test_autentica_com_cpf_none_retorna_none PASSED                   [ 40%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendAuthenticate::test_autentica_com_senha_none_retorna_none PASSED                 [ 50%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendAuthenticate::test_autentica_interessado_inativo_retorna_none PASSED            [ 60%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendAuthenticate::test_autentica_sem_request_mas_com_cpf_valido PASSED              [ 70%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendGetUser::test_get_user_com_id_valido_retorna_interessado PASSED                 [ 80%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendGetUser::test_get_user_com_id_inexistente_retorna_none PASSED                   [ 90%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendGetUser::test_get_user_interessado_inativo_retorna_none PASSED                  [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
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
apps\interessados\authentication.py                                        25      1    96%   52
apps\interessados\forms.py                                                157    157     0%   20-453
apps\interessados\management\__init__.py                                    0      0   100%
apps\interessados\management\commands\__init__.py                           0      0   100%
apps\interessados\management\commands\criptografar_cpfs.py                 22     22     0%   11-47
apps\interessados\management\commands\limpar_tokens.py                     59     59     0%   13-155
apps\interessados\management\commands\popular_cpf_hash.py                  22     22     0%   9-40
apps\interessados\models.py                                               139     16    88%   29, 41, 138, 141, 144, 147, 151, 155, 158, 162, 166, 172, 188, 191-192, 260
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3356    20%
Coverage HTML written to dir htmlcov


==================================================================== 10 passed in 5.73s ====================================================================




##  apps.interessados.tests.test_urls.py de 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/interessados/tests/test_urls.py -v          
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 28 items                                                                                                                                          

apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_cadastro_url PASSED                                                                      [  3%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_login_url PASSED                                                                         [  7%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_logout_url PASSED                                                                        [ 10%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_meus_dados_url PASSED                                                                    [ 14%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_dashboard_url PASSED                                                                     [ 17%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_detalhes_url PASSED                                                                      [ 21%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_inscrever_evento_url PASSED                                                              [ 25%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_senha_recuperar_url PASSED                                                               [ 28%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_senha_recuperar_enviado_url PASSED                                                       [ 32%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_senha_redefinir_url PASSED                                                               [ 35%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_senha_redefinir_concluido_url PASSED                                                     [ 39%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_senha_sem_email_url PASSED                                                               [ 42%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_solicitar_exclusao_url PASSED                                                            [ 46%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_exclusao_solicitada_url PASSED                                                           [ 50%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_cadastro_path PASSED                                                                         [ 53%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_login_path PASSED                                                                            [ 57%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_logout_path PASSED                                                                           [ 60%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_meus_dados_path PASSED                                                                       [ 64%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_dashboard_path PASSED                                                                        [ 67%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_detalhes_path PASSED                                                                         [ 71%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_inscrever_evento_path PASSED                                                                 [ 75%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_senha_recuperar_path PASSED                                                                  [ 78%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_senha_recuperar_enviado_path PASSED                                                          [ 82%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_senha_redefinir_path PASSED                                                                  [ 85%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_senha_redefinir_concluido_path PASSED                                                        [ 89%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_senha_sem_email_path PASSED                                                                  [ 92%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_solicitar_exclusao_path PASSED                                                               [ 96%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_exclusao_solicitada_path PASSED                                                              [100%]

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
apps\accounts\admin.py                                                     52     16    69%   50-65, 141-158
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
apps\dashboard\services.py                                                157    105    33%   23-26, 34-43, 47-56, 60-81, 85-93, 108-116, 131-152, 156-199, 203, 220-222, 233-236, 247-249, 255-257, 265, 278-293, 304-311, 315-317, 325-326, 338-343, 367-381, 390-392, 400
apps\dashboard\utils_pdf.py                                               373    350     6%   25-56, 61-80, 86-87, 90-91, 94-99, 102-107, 112-298, 303-464, 469-608, 613-751
apps\dashboard\views.py                                                    71     47    34%   33-42, 47-56, 61-70, 75-84, 89-109, 118-125, 130-137, 142-149, 154-161
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
apps\interessados\forms.py                                                157    106    32%   167-171, 179-213, 220-230, 234-235, 239-243, 247, 251, 255, 259, 263, 267, 271, 275-280, 287-302, 335-358, 392-396, 401-402, 406-410, 414, 418, 422, 426, 430, 434, 438, 445-453
apps\interessados\management\__init__.py                                    0      0   100%
apps\interessados\management\commands\__init__.py                           0      0   100%
apps\interessados\management\commands\criptografar_cpfs.py                 22     22     0%   11-47
apps\interessados\management\commands\limpar_tokens.py                     59     59     0%   13-155
apps\interessados\management\commands\popular_cpf_hash.py                  22     22     0%   9-40
apps\interessados\models.py                                               139     19    86%   22, 29, 41, 132, 135, 138, 141, 144, 147, 151, 155, 158, 162, 166, 172, 188, 191-192, 260
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3081    27%
Coverage HTML written to dir htmlcov


==================================================================== 28 passed in 3.79s ====================================================================



##  apps.interessados.tests.test_utils.py em 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/interessados/tests/test_utils.py -v
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 7 items                                                                                                                                           

apps/interessados/tests/test_utils.py::TestCustomEmailBackendSSLContext::test_sem_certificate_desabilita_verificacao PASSED                           [ 14%]
apps/interessados/tests/test_utils.py::TestCustomEmailBackendSSLContext::test_com_ssl_certfile_mantem_verificacao PASSED                              [ 28%]
apps/interessados/tests/test_utils.py::TestCustomEmailBackendSSLContext::test_context_e_cached_property PASSED                                        [ 42%]
apps/interessados/tests/test_utils.py::TestCustomEmailBackendSSLContext::test_ssl_context_sem_cert_e_sem_keyfile PASSED                               [ 57%]
apps/interessados/tests/test_utils.py::TestCustomEmailBackendHeranca::test_herda_de_emailbackend PASSED                                               [ 71%]
apps/interessados/tests/test_utils.py::TestCustomEmailBackend::test_timeout_padrao_nao_definido PASSED                                                [ 85%]
apps/interessados/tests/test_utils.py::TestCustomEmailBackend::test_timeout_personalizado PASSED                                                      [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
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
apps\interessados\models.py                                               139     19    86%   22, 29, 41, 132, 135, 138, 141, 144, 147, 151, 155, 158, 162, 166, 172, 188, 191-192, 260
apps\interessados\urls.py                                                   5      5     0%   11-17
apps\interessados\utils.py                                                 14      0   100%
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3369    20%
Coverage HTML written to dir htmlcov


==================================================================== 7 passed in 2.95s =====================================================================




##  apps.interessados.tests.test_views_exclusao.py em 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/interessados/tests/test_views_exclusao.py -v
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 12 items                                                                                                                                          

apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_sem_login_redirect_para_login PASSED                                  [  8%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_post_sem_login_redirect_para_login PASSED                             [ 16%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_interessado_inativo_logout_e_redirect PASSED                          [ 25%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_get_sem_pendente_retorna_200 PASSED                                   [ 33%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_get_com_pendente_redirect_dashboard PASSED                            [ 41%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_post_confirmacao_valida_cria_solicitacao PASSED                       [ 50%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_post_confirmacao_valida_sem_motivo PASSED                             [ 58%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_post_confirmacao_invalida_mostra_erro PASSED                          [ 66%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_post_confirmacao_vazia_mostra_erro PASSED                             [ 75%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_post_com_pendente_nao_cria_nova PASSED                                [ 83%]
apps/interessados/tests/test_views_exclusao.py::TestExclusaoSolicitadaView::test_sem_login_redirect_para_login PASSED                                 [ 91%]
apps/interessados/tests/test_views_exclusao.py::TestExclusaoSolicitadaView::test_get_com_login_retorna_200 PASSED                                     [100%]

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
apps\accounts\admin.py                                                     52     16    69%   50-65, 141-158
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
apps\dashboard\services.py                                                157    105    33%   23-26, 34-43, 47-56, 60-81, 85-93, 108-116, 131-152, 156-199, 203, 220-222, 233-236, 247-249, 255-257, 265, 278-293, 304-311, 315-317, 325-326, 338-343, 367-381, 390-392, 400
apps\dashboard\utils_pdf.py                                               373    350     6%   25-56, 61-80, 86-87, 90-91, 94-99, 102-107, 112-298, 303-464, 469-608, 613-751
apps\dashboard\views.py                                                    71     47    34%   33-42, 47-56, 61-70, 75-84, 89-109, 118-125, 130-137, 142-149, 154-161
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212    117    45%   61-67, 95, 110-114, 118-119, 122-124, 173-181, 187-206, 218-223, 229-234, 240-245, 251-256, 269-358, 371-415, 430-519, 537
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51     46    10%   27-114
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122     29    76%   28, 104-106, 127, 130-132, 135-137, 140-142, 145-147, 150-152, 155-160, 201, 206, 247, 280
apps\eventos\views.py                                                       1      1     0%   1
apps\interessados\__init__.py                                               0      0   100%
apps\interessados\admin.py                                                218    120    45%   178-183, 188, 193-194, 201-207, 216-222, 231-243, 248-260, 265-269, 280-282, 296-316, 329-330, 337-338, 347-431, 475, 480-481, 485-500, 509, 514, 523-527, 535-538, 546-552, 564, 567, 570
apps\interessados\apps.py                                                   5      0   100%
apps\interessados\authentication.py                                        25     15    40%   33-52, 72-73
apps\interessados\forms.py                                                157    106    32%   167-171, 179-213, 220-230, 234-235, 239-243, 247, 251, 255, 259, 263, 267, 271, 275-280, 287-302, 335-358, 392-396, 401-402, 406-410, 414, 418, 422, 426, 430, 434, 438, 445-453
apps\interessados\management\__init__.py                                    0      0   100%
apps\interessados\management\commands\__init__.py                           0      0   100%
apps\interessados\management\commands\criptografar_cpfs.py                 22     22     0%   11-47
apps\interessados\management\commands\limpar_tokens.py                     59     59     0%   13-155
apps\interessados\management\commands\popular_cpf_hash.py                  22     22     0%   9-40
apps\interessados\models.py                                               139     15    89%   29, 41, 135, 138, 141, 144, 147, 151, 162, 166, 172, 188, 191-192, 260
apps\interessados\urls.py                                                   5      0   100%
apps\interessados\utils.py                                                 14     14     0%   10-38
apps\interessados\views.py                                                202    167    17%   49-67, 81-107, 113-115, 129-181, 194-216, 232-250, 266-323, 342-414, 422, 430-472, 477, 482, 496-519
apps\interessados\views_exclusao.py                                        29      3    90%   25-27
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3034    28%
Coverage HTML written to dir htmlcov


==================================================================== 12 passed in 9.18s ====================================================================




##  apps.portal.tests.test_forms.py em 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/portal/tests/test_forms.py -v
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 11 items                                                                                                                                          

apps/portal/tests/test_forms.py::TestLoginInteressadoForm::test_form_valido_com_cpf_e_senha_corretos PASSED                                           [  9%]
apps/portal/tests/test_forms.py::TestLoginInteressadoForm::test_form_valido_com_cpf_formatado PASSED                                                  [ 18%]
apps/portal/tests/test_forms.py::TestLoginInteressadoForm::test_form_invalido_com_cpf_incorreto PASSED                                                [ 27%]
apps/portal/tests/test_forms.py::TestLoginInteressadoForm::test_form_invalido_com_senha_incorreta PASSED                                              [ 36%]
apps/portal/tests/test_forms.py::TestLoginInteressadoForm::test_form_invalido_interessado_inativo PASSED                                              [ 45%]
apps/portal/tests/test_forms.py::TestLoginInteressadoForm::test_form_invalido_cpf_com_menos_de_11_digitos PASSED                                      [ 54%]
apps/portal/tests/test_forms.py::TestLoginInteressadoForm::test_form_invalido_com_campos_vazios PASSED                                                [ 63%]
apps/portal/tests/test_forms.py::TestConsultaPublicaForm::test_cpf_valido_sem_formatacao PASSED                                                       [ 72%]
apps/portal/tests/test_forms.py::TestConsultaPublicaForm::test_cpf_valido_com_formatacao PASSED                                                       [ 81%]
apps/portal/tests/test_forms.py::TestConsultaPublicaForm::test_cpf_invalido_com_menos_de_11_digitos PASSED                                            [ 90%]
apps/portal/tests/test_forms.py::TestConsultaPublicaForm::test_cpf_invalido_vazio PASSED                                                              [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
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
apps\interessados\models.py                                               139     16    88%   29, 41, 138, 141, 144, 147, 151, 155, 158, 162, 166, 172, 188, 191-192, 260
apps\interessados\urls.py                                                   5      5     0%   11-17
apps\interessados\utils.py                                                 14     14     0%   10-38
apps\interessados\views.py                                                202    202     0%   24-519
apps\interessados\views_exclusao.py                                        29     29     0%   8-76
apps\portal\__init__.py                                                     1      0   100%
apps\portal\admin.py                                                        1      0   100%
apps\portal\apps.py                                                         5      0   100%
apps\portal\forms.py                                                       34      0   100%
apps\portal\models.py                                                       1      0   100%
apps\portal\urls.py                                                         4      4     0%   8-13
apps\portal\views.py                                                       99     99     0%   13-247
apps\scripts_admin\__init__.py                                              0      0   100%
apps\scripts_admin\management\__init__.py                                   0      0   100%
apps\scripts_admin\management\commands\__init__.py                          0      0   100%
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3346    20%
Coverage HTML written to dir htmlcov


=================================================================== 11 passed in 10.39s ====================================================================


##  apps.portal.tests.test_urls.py em 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/portal/tests/test_urls.py -v
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 18 items                                                                                                                                          

apps/portal/tests/test_urls.py::TestUrlsResolvem::test_index_url PASSED                                                                               [  5%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_login_url PASSED                                                                               [ 11%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_logout_url PASSED                                                                              [ 16%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_dashboard_url PASSED                                                                           [ 22%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_consulta_publica_url PASSED                                                                    [ 27%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_resultado_evento_url PASSED                                                                    [ 33%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_detalhes_evento_url PASSED                                                                     [ 38%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_contato_url PASSED                                                                             [ 44%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_privacidade_url PASSED                                                                         [ 50%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_index_path PASSED                                                                                  [ 55%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_login_path PASSED                                                                                  [ 61%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_logout_path PASSED                                                                                 [ 66%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_dashboard_path PASSED                                                                              [ 72%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_consulta_publica_path PASSED                                                                       [ 77%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_resultado_evento_path PASSED                                                                       [ 83%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_detalhes_evento_path PASSED                                                                        [ 88%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_contato_path PASSED                                                                                [ 94%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_privacidade_path PASSED                                                                            [100%]

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
apps\accounts\admin.py                                                     52     16    69%   50-65, 141-158
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
apps\dashboard\services.py                                                157    105    33%   23-26, 34-43, 47-56, 60-81, 85-93, 108-116, 131-152, 156-199, 203, 220-222, 233-236, 247-249, 255-257, 265, 278-293, 304-311, 315-317, 325-326, 338-343, 367-381, 390-392, 400
apps\dashboard\utils_pdf.py                                               373    350     6%   25-56, 61-80, 86-87, 90-91, 94-99, 102-107, 112-298, 303-464, 469-608, 613-751
apps\dashboard\views.py                                                    71     47    34%   33-42, 47-56, 61-70, 75-84, 89-109, 118-125, 130-137, 142-149, 154-161
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
apps\interessados\forms.py                                                157    106    32%   167-171, 179-213, 220-230, 234-235, 239-243, 247, 251, 255, 259, 263, 267, 271, 275-280, 287-302, 335-358, 392-396, 401-402, 406-410, 414, 418, 422, 426, 430, 434, 438, 445-453
apps\interessados\management\__init__.py                                    0      0   100%
apps\interessados\management\commands\__init__.py                           0      0   100%
apps\interessados\management\commands\criptografar_cpfs.py                 22     22     0%   11-47
apps\interessados\management\commands\limpar_tokens.py                     59     59     0%   13-155
apps\interessados\management\commands\popular_cpf_hash.py                  22     22     0%   9-40
apps\interessados\models.py                                               139     19    86%   22, 29, 41, 132, 135, 138, 141, 144, 147, 151, 155, 158, 162, 166, 172, 188, 191-192, 260
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
apps\scripts_admin\managemen




##  apps.portal.tests.test_views.py em 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/portal/tests/test_views.py -v
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 26 items                                                                                                                                          

apps/portal/tests/test_views.py::TestIndexView::test_index_get_200 PASSED                                                                             [  3%]
apps/portal/tests/test_views.py::TestIndexView::test_index_context_eventos PASSED                                                                     [  7%]
apps/portal/tests/test_views.py::TestIndexView::test_index_total_eventos_int PASSED                                                                   [ 11%]
apps/portal/tests/test_views.py::TestLoginInteressadoView::test_login_post_valido_redirect_302 PASSED                                                 [ 15%]
apps/portal/tests/test_views.py::TestLoginInteressadoView::test_login_post_valido_cria_sessao_id PASSED                                               [ 19%]
apps/portal/tests/test_views.py::TestLoginInteressadoView::test_login_post_valido_sessao_nome PASSED                                                  [ 23%]
apps/portal/tests/test_views.py::TestLoginInteressadoView::test_login_post_valido_sessao_cpf_mascarado PASSED                                         [ 26%]
apps/portal/tests/test_views.py::TestLoginInteressadoView::test_login_com_sessao_redirect_302 PASSED                                                  [ 30%]
apps/portal/tests/test_views.py::TestLogoutInteressadoView::test_logout_limpa_sessao PASSED                                                           [ 34%]
apps/portal/tests/test_views.py::TestLogoutInteressadoView::test_logout_redirect_302 PASSED                                                           [ 38%]
apps/portal/tests/test_views.py::TestDashboardView::test_dashboard_sem_sessao_redirect_302 PASSED                                                     [ 42%]
apps/portal/tests/test_views.py::TestDashboardView::test_dashboard_sessao_invalida_redirect_302 PASSED                                                [ 46%]
apps/portal/tests/test_views.py::TestDashboardView::test_dashboard_sessao_valida_nao_302 PASSED                                                       [ 50%]
apps/portal/tests/test_views.py::TestDashboardView::test_dashboard_sessao_valida_status_ok PASSED                                                     [ 53%]
apps/portal/tests/test_views.py::TestConsultaPublicaView::test_consulta_get_200 PASSED                                                                [ 57%]
apps/portal/tests/test_views.py::TestConsultaPublicaView::test_consulta_post_cpf_valido_context PASSED                                                [ 61%]
apps/portal/tests/test_views.py::TestConsultaPublicaView::test_consulta_post_cpf_invalido_mensagem PASSED                                             [ 65%]
apps/portal/tests/test_views.py::TestConsultaPublicaView::test_consulta_post_vazio_form PASSED                                                        [ 69%]
apps/portal/tests/test_views.py::TestResultadoEventoView::test_resultado_get_status_valido PASSED                                                     [ 73%]
apps/portal/tests/test_views.py::TestResultadoEventoView::test_resultado_get_nao_erro_500 PASSED                                                      [ 76%]
apps/portal/tests/test_views.py::TestDetalhesEventoView::test_detalhes_sem_sessao_redirect PASSED                                                     [ 80%]
apps/portal/tests/test_views.py::TestDetalhesEventoView::test_detalhes_com_sessao_status_valido PASSED                                                [ 84%]
apps/portal/tests/test_views.py::TestContatoView::test_contato_get_200 PASSED                                                                         [ 88%]
apps/portal/tests/test_views.py::TestContatoView::test_contato_context PASSED                                                                         [ 92%]
apps/portal/tests/test_views.py::TestPoliticaPrivacidadeView::test_politica_get_200 PASSED                                                            [ 96%]
apps/portal/tests/test_views.py::TestPoliticaPrivacidadeView::test_politica_content_existe PASSED                                                     [100%]

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
apps\accounts\admin.py                                                     52     16    69%   50-65, 141-158
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
apps\dashboard\services.py                                                157    105    33%   23-26, 34-43, 47-56, 60-81, 85-93, 108-116, 131-152, 156-199, 203, 220-222, 233-236, 247-249, 255-257, 265, 278-293, 304-311, 315-317, 325-326, 338-343, 367-381, 390-392, 400
apps\dashboard\utils_pdf.py                                               373    350     6%   25-56, 61-80, 86-87, 90-91, 94-99, 102-107, 112-298, 303-464, 469-608, 613-751
apps\dashboard\views.py                                                    71     47    34%   33-42, 47-56, 61-70, 75-84, 89-109, 118-125, 130-137, 142-149, 154-161
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212    117    45%   61-67, 95, 110-114, 118-119, 122-124, 173-181, 187-206, 218-223, 229-234, 240-245, 251-256, 269-358, 371-415, 430-519, 537
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51     46    10%   27-114
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122     29    76%   28, 104-106, 127, 130-132, 135-137, 140-142, 145-147, 150-152, 155-160, 201, 206, 247, 280
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
apps\interessados\models.py                                               139     16    88%   29, 41, 138, 141, 144, 147, 151, 155, 158, 162, 166, 172, 188, 191-192, 260
apps\interessados\urls.py                                                   5      0   100%
apps\interessados\utils.py                                                 14     14     0%   10-38
apps\interessados\views.py                                                202    167    17%   49-67, 81-107, 113-115, 129-181, 194-216, 232-250, 266-323, 342-414, 422, 430-472, 477, 482, 496-519
apps\interessados\views_exclusao.py                                        29     20    31%   22-67, 76
apps\portal\__init__.py                                                     1      0   100%
apps\portal\admin.py                                                        1      0   100%
apps\portal\apps.py                                                         5      0   100%
apps\portal\forms.py                                                       34      6    82%   49, 64, 69, 73-74, 102
apps\portal\models.py                                                       1      0   100%
apps\portal\urls.py                                                         4      0   100%
apps\portal\views.py                                                       99     11    89%   72-74, 174-189, 202-220
apps\scripts_admin\__init__.py                                              0      0   100%
apps\scripts_admin\management\__init__.py                                   0      0   100%
apps\scripts_admin\management\commands\__init__.py                          0      0   100%
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   2976    29%
Coverage HTML written to dir htmlcov


=================================================================== 26 passed in 15.27s ====================================================================





##  apps.scripts_admin.management.commands.tests.test_classificar_evento.py em 16/06/2026, 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/scripts_admin/management/commands/tests/test_classificar_evento.py -v
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 32 items                                                                                                                                          

apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoEventoNaoEncontrado::test_evento_inexistente_exibe_erro PASSED [  3%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoSemInscricoes::test_sem_inscricoes_confirmadas_exibe_aviso PASSED [  6%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoSemInscricoes::test_sem_inscricoes_nao_cria_classificacao PASSED [  9%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoSemCriterios::test_sem_criterios_exibe_aviso PASSED     [ 12%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_pcd_atribuido PASSED           [ 15%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_pcd_nao_atribuido_quando_sem_deficiencia PASSED [ 18%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_nis_atribuido PASSED           [ 21%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_nis_nao_atribuido_sem_nis PASSED [ 25%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_jovem_atribuido_16_anos PASSED [ 28%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_jovem_atribuido_24_anos PASSED [ 31%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_jovem_nao_atribuido_para_adulto PASSED [ 34%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_idoso_atribuido_50_anos PASSED [ 37%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_idoso_nao_atribuido_para_49_anos PASSED [ 40%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_cota_racial_preta PASSED       [ 43%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_cota_racial_parda PASSED       [ 46%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_cota_racial_indigena PASSED    [ 50%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_cota_racial_nao_atribuido_para_branca PASSED [ 53%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_cota_racial_sem_fototipo PASSED [ 56%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_escolaridade_fundamental_incompleto PASSED [ 59%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_escolaridade_medio_completo PASSED [ 62%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_multiplos_criterios_somam_pontos PASSED [ 65%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoCriterioOrdenacao::test_criterio_ordenacao_nao_soma_pontos PASSED [ 68%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPosicao::test_primeiro_colocado_esta_classificado PASSED [ 71%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPosicao::test_fora_das_vagas_esta_em_lista_espera PASSED [ 75%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPosicao::test_total_de_classificacoes_igual_ao_total_de_inscricoes PASSED [ 78%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPosicao::test_posicoes_sao_unicas PASSED                [ 81%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoDesempatePorIdade::test_desempate_jovem_prioriza_mais_novo PASSED [ 84%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoDesempatePorIdade::test_desempate_idoso_prioriza_mais_velho PASSED [ 87%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoIdempotencia::test_segunda_execucao_nao_duplica_classificacao PASSED [ 90%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoIdempotencia::test_segunda_execucao_nao_duplica_criterios_atendidos PASSED [ 93%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoStatusInscricao::test_inscricao_pendente_e_ignorada PASSED [ 96%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoStatusInscricao::test_inscricao_confirmada_e_processada PASSED [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
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
apps\interessados\models.py                                               139     18    87%   22, 29, 41, 132, 135, 138, 141, 144, 147, 151, 155, 158, 162, 172, 188, 191-192, 260
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
apps\scripts_admin\management\commands\classificar_evento.py              134      9    93%   82, 100-101, 182-184, 188-190
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
TOTAL                                                                    4208   3250    23%
Coverage HTML written to dir htmlcov


==================================================================== 32 passed in 3.80s ====================================================================



##  apps.scripts_admin.management.commands.tests.test_popular_dados_iniciais.py em 16/06/2026, 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py -v                                                                                 
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 53 items                                                                                                                                          

apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisComando::test_comando_executa_sem_erro PASSED    [  1%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisComando::test_comando_retorna_string PASSED      [  3%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisComando::test_comando_nao_vazio PASSED           [  5%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_planejamento PASSED   [  7%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_inscricoes_abertas PASSED [  9%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_inscricoes_encerradas PASSED [ 11%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_em_classificacao PASSED [ 13%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_resultado_divulgado PASSED [ 15%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_em_andamento PASSED   [ 16%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_finalizado PASSED     [ 18%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_cancelado PASSED      [ 20%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_total_status_eventos PASSED  [ 22%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_pendente PASSED    [ 24%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_classificado PASSED [ 26%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_confirmada PASSED  [ 28%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_lista_espera PASSED [ 30%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_cancelada PASSED   [ 32%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_expirada PASSED    [ 33%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_desistente PASSED  [ 35%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_nao_localizado PASSED [ 37%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_total_status_inscricoes PASSED [ 39%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusMatriculas::test_status_pendente PASSED    [ 41%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusMatriculas::test_status_ativa PASSED       [ 43%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusMatriculas::test_status_concluida PASSED   [ 45%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusMatriculas::test_status_trancada PASSED    [ 47%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusMatriculas::test_status_cancelada PASSED   [ 49%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusMatriculas::test_total_status_matriculas PASSED [ 50%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisCriterios::test_criterio_pcd PASSED              [ 52%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisCriterios::test_criterio_programa_social PASSED  [ 54%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisCriterios::test_criterio_jovem PASSED            [ 56%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisCriterios::test_criterio_idoso PASSED            [ 58%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisCriterios::test_criterio_ensino_fundamental PASSED [ 60%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisCriterios::test_criterio_renda_baixa PASSED      [ 62%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisCriterios::test_criterio_cota_racial PASSED      [ 64%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSexo::test_sexo_masculino PASSED                 [ 66%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSexo::test_sexo_feminino PASSED                  [ 67%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSexo::test_sexo_outro PASSED                     [ 69%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSexo::test_sexo_nao_informar PASSED              [ 71%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSexo::test_total_sexo PASSED                     [ 73%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisFototipes::test_fototipo_branca PASSED           [ 75%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisFototipes::test_fototipo_preta PASSED            [ 77%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisFototipes::test_fototipo_parda PASSED            [ 79%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisFototipes::test_fototipo_amarela PASSED          [ 81%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisFototipes::test_fototipo_indigena PASSED         [ 83%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisFototipes::test_total_fototipos PASSED           [ 84%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisIntegracao::test_todos_modelos_populados PASSED  [ 86%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisIntegracao::test_contagem_total_registros PASSED [ 88%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisIntegracao::test_integridade_dados PASSED        [ 90%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisIdempotencia::test_execucao_dupla_nao_duplica_dados PASSED [ 92%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisIdempotencia::test_execucao_tripla_nao_duplica_dados PASSED [ 94%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSaida::test_saida_contem_sucesso PASSED          [ 96%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSaida::test_saida_contem_nome_comando PASSED     [ 98%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSaida::test_saida_nao_contem_ansi PASSED         [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
apps\scripts_admin\management\commands\configurar_criterios_evento.py      57     57     0%   5-91
apps\scripts_admin\management\commands\popular_criterios.py                21     21     0%   4-117
apps\scripts_admin\management\commands\popular_dados_iniciais.py           66      0   100%
apps\selecao\__init__.py                                                    0      0   100%
apps\selecao\admin.py                                                     275    163    41%   66-72, 87, 110-115, 152, 223, 233, 240-241, 247, 254-255, 266-275, 293-456, 466-503, 507-544, 552, 558, 564, 570, 580, 586, 592, 598, 608, 612, 616, 661, 667, 673, 677
apps\selecao\apps.py                                                        5      0   100%
apps\selecao\management\__init__.py                                         0      0   100%
apps\selecao\management\commands\__init__.py                                0      0   100%
apps\selecao\models.py                                                     71     15    79%   38, 74, 124-137, 145-146, 155, 188
apps\selecao\reports.py                                                   301    270    10%   27-31, 35-115, 126-132, 140-146, 151-163, 179-286, 302-420, 440-565, 580-711
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3317    21%
Coverage HTML written to dir htmlcov





##  apps.selecao.tests.test_services.py em 10/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/selecao/tests/test_services.py -v
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 16 items                                                                                                                                          

apps/selecao/tests/test_services.py::TestClassificadorServicePontuacao::test_calcular_pontuacao_inscricao_com_criterios PASSED                        [  6%]
apps/selecao/tests/test_services.py::TestClassificadorServicePontuacao::test_calcular_pontuacao_inscricao_zero PASSED                                 [ 12%]
apps/selecao/tests/test_services.py::TestClassificadorServicePontuacao::test_calcular_pontuacao_multiplos_criterios PASSED                            [ 18%]
apps/selecao/tests/test_services.py::TestClassificadorServicePontuacao::test_classificar_sem_eventocriterio_vinculado PASSED                          [ 25%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_atribui_posicoes PASSED                           [ 31%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_classifica_dentro_vagas PASSED                    [ 37%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_lista_espera PASSED                               [ 43%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_atualiza_status_inscricao PASSED                  [ 50%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_com_criterios PASSED                              [ 56%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_zero_inscricoes PASSED                            [ 62%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_chamada_repetida PASSED                           [ 68%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_exatamente_1_vaga PASSED                          [ 75%]
apps/selecao/tests/test_services.py::TestClassificadorServiceDesempate::test_desempate_por_data_inscricao_igual_pontuacao PASSED                      [ 81%]
apps/selecao/tests/test_services.py::TestClassificadorServiceDesempate::test_desempate_com_lista_espera PASSED                                        [ 87%]
apps/selecao/tests/test_services.py::TestClassificadorServiceDesempate::test_desempate_misto_pontuacoes_diferentes_e_iguais PASSED                    [ 93%]
apps/selecao/tests/test_services.py::TestClassificadorServiceProcessamento::test_processar_inscricao_cria_classificacao PASSED                        [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
TOTAL                                                                    4208   3275    22%
Coverage HTML written to dir htmlcov


=================================================================== 16 passed in 17.67s ====================================================================




##  apps.selecao.tests.test_models.py em 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/selecao/tests/test_models.py -v
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 14 items                                                                                                                                          

apps/selecao/tests/test_models.py::TestStatusInscricaoModel::test_create_status_inscricao PASSED                                                      [  7%]
apps/selecao/tests/test_models.py::TestStatusInscricaoModel::test_status_inscricao_str PASSED                                                         [ 14%]
apps/selecao/tests/test_models.py::TestStatusInscricaoModel::test_status_inscricao_unique_name PASSED                                                 [ 21%]
apps/selecao/tests/test_models.py::TestInscricaoModel::test_create_inscricao PASSED                                                                   [ 28%]
apps/selecao/tests/test_models.py::TestInscricaoModel::test_inscricao_str PASSED                                                                      [ 35%]
apps/selecao/tests/test_models.py::TestInscricaoModel::test_inscricao_unique_together PASSED                                                          [ 42%]
apps/selecao/tests/test_models.py::TestInscricaoModel::test_inscricao_relacionamentos PASSED                                                          [ 50%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_create_classificacao PASSED                                                           [ 57%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_classificacao_str PASSED                                                              [ 64%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_classificacao_posicao_null_default PASSED                                             [ 71%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_classificacao_unique_inscricao PASSED                                                 [ 78%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_pontuacao_total_validacao_range PASSED                                                [ 85%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_flags_classificacao_mutuamente_exclusivas PASSED                                      [ 92%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_desempate_por_data_inscricao PASSED                                                   [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3367    20%
Coverage HTML written to dir htmlcov


==================================================================== 14 passed in 8.16s ====================================================================




##  apps.selecao.tests.test_admin.py em 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/selecao/tests/test_admin.py -v  
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 12 items                                                                                                                                          

apps/selecao/tests/test_admin.py::TestMatricularAlunosActionCapacity::test_matricular_alunos_capacidade_ultrapassada PASSED                           [  8%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionCapacity::test_matricular_alunos_capacidade_exata PASSED                                  [ 16%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionValidation::test_validacao_evento_unico PASSED                                            [ 25%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionValidation::test_validacao_turma_inexistente_para_evento PASSED                           [ 33%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionValidation::test_protecao_duplicidade_matricula PASSED                                    [ 41%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionValidation::test_validacao_turma_nao_pertence_ao_evento PASSED                            [ 50%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionSuccess::test_sucesso_matricula_dentro_capacidade PASSED                                  [ 58%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionSuccess::test_nenhuma_classificacao_selecionada PASSED                                    [ 66%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionErrorHandling::test_transacao_atomica_rollback_on_matricula_save_error PASSED             [ 75%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionErrorHandling::test_status_ativa_nao_encontrado PASSED                                    [ 83%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionErrorHandling::test_status_confirmada_nao_encontrado PASSED                               [ 91%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionErrorHandling::test_classificacoes_sem_evento_associado PASSED                            [100%]

---------- coverage: platform win32, python 3.13.2-final-0 -----------
Name                                                                    Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------------------
apps\__init__.py                                                            0      0   100%
apps\academico\__init__.py                                                  0      0   100%
apps\academico\admin.py                                                   320    248    22%   64-70, 124, 129, 200, 205, 211-216, 225-266, 270-276, 284-440, 450-613, 623-653, 663-671, 678, 681
apps\academico\apps.py                                                      5      0   100%
apps\academico\certificado.py                                             136    118    13%   24-37, 43-67, 72-79, 83-104, 108-116, 120-163, 167-208, 212-254
apps\academico\models.py                                                  110     25    77%   45, 122, 133, 142, 154, 168, 204-206, 282-283, 300-316, 339-342
apps\academico\services.py                                                136    136     0%   8-402
apps\academico\urls.py                                                      5      0   100%
apps\academico\views.py                                                    63     45    29%   31-52, 61-77, 87-124
apps\accounts\__init__.py                                                   0      0   100%
apps\accounts\admin.py                                                     52     16    69%   50-65, 141-158
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
apps\dashboard\services.py                                                157    105    33%   23-26, 34-43, 47-56, 60-81, 85-93, 108-116, 131-152, 156-199, 203, 220-222, 233-236, 247-249, 255-257, 265, 278-293, 304-311, 315-317, 325-326, 338-343, 367-381, 390-392, 400
apps\dashboard\utils_pdf.py                                               373    350     6%   25-56, 61-80, 86-87, 90-91, 94-99, 102-107, 112-298, 303-464, 469-608, 613-751
apps\dashboard\views.py                                                    71     47    34%   33-42, 47-56, 61-70, 75-84, 89-109, 118-125, 130-137, 142-149, 154-161
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   2947    30%
Coverage HTML written to dir htmlcov


=================================================================== 12 passed in 16.92s ====================================================================



##  apps.selecao.tests.test_validators.py em 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/selecao/tests/test_validators.py -v  
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 13 items                                                                                                                                          

apps/selecao/tests/test_validators.py::TestValidarEvento::test_evento_sem_vagas_falha PASSED                                                          [  7%]
apps/selecao/tests/test_validators.py::TestValidarEvento::test_evento_sem_inscricoes_falha PASSED                                                     [ 15%]
apps/selecao/tests/test_validators.py::TestValidarEvento::test_evento_datas_invalidas_falha PASSED                                                    [ 23%]
apps/selecao/tests/test_validators.py::TestValidarEvento::test_evento_sem_criterios_falha PASSED                                                      [ 30%]
apps/selecao/tests/test_validators.py::TestValidarEvento::test_evento_com_criterios_passa PASSED                                                      [ 38%]
apps/selecao/tests/test_validators.py::TestValidarInteressado::test_interessado_valido_passa PASSED                                                   [ 46%]
apps/selecao/tests/test_validators.py::TestValidarInteressado::test_interessado_sem_nome_falha PASSED                                                 [ 53%]
apps/selecao/tests/test_validators.py::TestValidarInteressado::test_interessado_data_nascimento_futura_falha PASSED                                   [ 61%]
apps/selecao/tests/test_validators.py::TestValidarInteressado::test_interessado_sem_sexo_gera_aviso PASSED                                            [ 69%]
apps/selecao/tests/test_validators.py::TestValidarInscricao::test_inscricao_valida_passa PASSED                                                       [ 76%]
apps/selecao/tests/test_validators.py::TestValidarInscricao::test_inscricao_sem_evento_falha PASSED                                                   [ 84%]
apps/selecao/tests/test_validators.py::TestValidarInscricao::test_inscricao_sem_interessado_falha PASSED                                              [ 92%]
apps/selecao/tests/test_validators.py::TestValidarInscricao::test_inscricao_com_data_futura_falha PASSED                                              [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
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
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105     35    67%   38-39, 47, 74, 101, 105, 116, 123, 126, 130, 149-175, 193-194, 199, 204, 213-215, 222-223
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   3311    21%
Coverage HTML written to dir htmlcov


==================================================================== 13 passed in 7.10s ====================================================================



##  apps.selecao.tests.test_reports.py em 22/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest apps/selecao/tests/test_reports.py -v --tb=short
=========================================================================== test session starts ===========================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 31 items                                                                                                                                                         

apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_valido PASSED                                                                   [  3%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_none PASSED                                                                     [  6%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_vazio PASSED                                                                    [  9%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_ja_formatado PASSED                                                             [ 12%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_menos_de_11 PASSED                                                              [ 16%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_mascarado_valido PASSED                                                         [ 19%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_mascarado_none PASSED                                                           [ 22%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_mascarado_vazio PASSED                                                          [ 25%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_telefone_celular PASSED                                                             [ 29%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_telefone_fixo PASSED                                                                [ 32%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_telefone_none PASSED                                                                [ 35%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_telefone_vazio PASSED                                                               [ 38%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_telefone_ja_formatado PASSED                                                        [ 41%]
apps/selecao/tests/test_reports.py::TestGerarRelatorioStaff::test_retorna_http_response PASSED                                                                       [ 45%]
apps/selecao/tests/test_reports.py::TestGerarRelatorioStaff::test_content_type_pdf PASSED                                                                            [ 48%]
apps/selecao/tests/test_reports.py::TestGerarRelatorioStaff::test_content_disposition_inline PASSED                                                                  [ 51%]
apps/selecao/tests/test_reports.py::TestGerarRelatorioStaff::test_conteudo_nao_vazio PASSED                                                                          [ 54%]
apps/selecao/tests/test_reports.py::TestGerarRelatorioStaff::test_filename_contem_staff PASSED                                                                       [ 58%]
apps/selecao/tests/test_reports.py::TestGerarRelatorioStaff::test_ordem_nome_altera_filename PASSED                                                                  [ 61%]
apps/selecao/tests/test_reports.py::TestGerarRelatorioMural::test_retorna_http_response PASSED                                                                       [ 64%]
apps/selecao/tests/test_reports.py::TestGerarRelatorioMural::test_content_type_pdf PASSED                                                                            [ 67%]
apps/selecao/tests/test_reports.py::TestGerarRelatorioMural::test_content_disposition_inline PASSED                                                                  [ 70%]
apps/selecao/tests/test_reports.py::TestGerarRelatorioMural::test_filename_contem_mural PASSED                                                                       [ 74%]
apps/selecao/tests/test_reports.py::TestGerarExcelStaff::test_retorna_http_response PASSED                                                                           [ 77%]
apps/selecao/tests/test_reports.py::TestGerarExcelStaff::test_content_type_excel PASSED                                                                              [ 80%]
apps/selecao/tests/test_reports.py::TestGerarExcelStaff::test_content_disposition_attachment PASSED                                                                  [ 83%]
apps/selecao/tests/test_reports.py::TestGerarExcelStaff::test_filename_contem_staff PASSED                                                                           [ 87%]
apps/selecao/tests/test_reports.py::TestGerarExcelStaff::test_conteudo_nao_vazio PASSED                                                                              [ 90%]
apps/selecao/tests/test_reports.py::TestGerarExcelMural::test_retorna_http_response PASSED                                                                           [ 93%]
apps/selecao/tests/test_reports.py::TestGerarExcelMural::test_content_type_excel PASSED                                                                              [ 96%]
apps/selecao/tests/test_reports.py::TestGerarExcelMural::test_filename_contem_mural PASSED                                                                           [100%]

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
apps\accounts\admin.py                                                     52     19    63%   42-46, 50-65, 141-158
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
apps\dashboard\services.py                                                157    157     0%   12-400
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
apps\scripts_admin\management\commands\classificar_evento.py              134    134     0%   9-295
apps\scripts_admin\management\commands\configurar_criterios_evento.py      57     57     0%   5-91
apps\scripts_admin\management\commands\popular_criterios.py                21     21     0%   4-117
apps\scripts_admin\management\commands\popular_dados_iniciais.py           66     66     0%   8-234
apps\selecao\__init__.py                                                    0      0   100%
apps\selecao\admin.py                                                     275    163    41%   66-72, 87, 110-115, 152, 223, 233, 240-241, 247, 254-255, 266-275, 293-456, 466-503, 507-544, 552, 558, 564, 570, 580, 586, 592, 598, 608, 612, 616, 661, 667, 673, 677
apps\selecao\apps.py                                                        5      0   100%
apps\selecao\management\__init__.py                                         0      0   100%
apps\selecao\management\commands\__init__.py                                0      0   100%
apps\selecao\models.py                                                     71      8    89%   38, 74, 129, 133-134, 137, 155, 188
apps\selecao\reports.py                                                   301     13    96%   54-55, 63-64, 95, 146, 163, 223, 346, 475, 513, 615, 653
apps\selecao\services.py                                                  125    125     0%   29-432
apps\selecao\validators.py                                                105    105     0%   10-225
apps\selecao\views.py                                                       0      0   100%
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4207   3116    26%
Coverage HTML written to dir htmlcov


=========================================================================== 31 passed in 31.07s =====================================================================




##   python -m pytest -x ==> para testar tudo em 18/06/2026

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest -x
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
testpaths: apps
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 775 items                                                                                                                                         

apps/academico/tests/test_admin.py::TestStatusMatriculaAdmin::test_cor_display_com_cor PASSED                                                         [  0%]
apps/academico/tests/test_admin.py::TestStatusMatriculaAdmin::test_cor_display_sem_cor PASSED                                                         [  0%]
apps/academico/tests/test_admin.py::TestMatriculaAdmin::test_get_interessado PASSED                                                                   [  0%]
apps/academico/tests/test_admin.py::TestMatriculaAdmin::test_get_evento PASSED                                                                        [  0%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_acoes_certificado_aprovado PASSED                                                        [  0%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_acoes_certificado_nao_aprovado PASSED                                                    [  0%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_changelist_view_contexto PASSED                                                          [  0%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_gerar_certificados_marca_emitidos PASSED                                                 [  1%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_gerar_certificados_sem_aprovados PASSED                                                  [  1%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_gerar_certificados_ja_emitido PASSED                                                     [  1%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_download_certificados_lote_action_redirect PASSED                                        [  1%]
apps/academico/tests/test_certificado.py::TestAtributos::test_inicializacao_atributos PASSED                                                          [  1%]
apps/academico/tests/test_certificado.py::TestAtributos::test_pagesize_a4_paisagem PASSED                                                             [  1%]
apps/academico/tests/test_certificado.py::TestAtributos::test_static_path_construido PASSED                                                           [  1%]
apps/academico/tests/test_certificado.py::TestFormatacao::test_cpf_formatado PASSED                                                                   [  1%]
apps/academico/tests/test_certificado.py::TestTraducaoMes::test_traducao_mes[data0-15 de janeiro de 2026] PASSED                                      [  2%]
apps/academico/tests/test_certificado.py::TestTraducaoMes::test_traducao_mes[data1-03 de agosto de 2026] PASSED                                       [  2%]
apps/academico/tests/test_certificado.py::TestFallback::test_data_emissao_fallback_para_agora PASSED                                                  [  2%]
apps/academico/tests/test_certificado.py::TestFallback::test_carga_horaria_fallback_40h PASSED                                                        [  2%]
apps/academico/tests/test_certificado.py::TestGeracaoPDF::test_gerar_pdf_retorna_buffer_valido PASSED                                                 [  2%]
apps/academico/tests/test_certificado.py::TestGeracaoPDF::test_gerar_pdf_multiplas_chamadas PASSED                                                    [  2%]
apps/academico/tests/test_models.py::TestStatusMatriculaModel::test_status_criado_corretamente PASSED                                                 [  2%]
apps/academico/tests/test_models.py::TestStatusMatriculaModel::test_status_nome_unique_no_banco PASSED                                                [  2%]
apps/academico/tests/test_models.py::TestMatriculaModel::test_matricula_criada_corretamente PASSED                                                    [  3%]
apps/academico/tests/test_models.py::TestMatriculaModel::test_matricula_unique_together_turma_interessado PASSED                                      [  3%]
apps/academico/tests/test_services.py::TestVerificacaoDisponibilidade::test_verificar_disponibilidade_turma_com_vagas PASSED                          [  3%]
apps/academico/tests/test_services.py::TestVerificacaoDisponibilidade::test_verificar_disponibilidade_turma_lotada PASSED                             [  3%]
apps/academico/tests/test_services.py::TestVerificacaoDisponibilidade::test_verificar_disponibilidade_turma_parcial PASSED                            [  3%]
apps/academico/tests/test_services.py::TestVerificacaoDisponibilidade::test_verificar_disponibilidade_turma_exatamente_cheia PASSED                   [  3%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_aprovado PASSED                                                         [  3%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_reprovado_por_nota PASSED                                               [  4%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_reprovado_por_frequencia PASSED                                         [  4%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_nota_invalida PASSED                                                    [  4%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_frequencia_invalida PASSED                                              [  4%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_nota_limite_minimo_aprovado PASSED                                      [  4%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_nota_limite_maximo PASSED                                               [  4%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_frequencia_limite_minimo PASSED                                         [  4%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_frequencia_limite_maximo PASSED                                         [  4%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_atualiza_status_matricula PASSED                                        [  5%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_cria_ou_atualiza PASSED                                                 [  5%]
apps/academico/tests/test_services.py::TestRelatorioTurma::test_gerar_relatorio_turma PASSED                                                          [  5%]
apps/academico/tests/test_services.py::TestRelatorioTurma::test_gerar_relatorio_turma_vazia PASSED                                                    [  5%]
apps/academico/tests/test_services.py::TestRelatorioTurma::test_gerar_relatorio_turma_parcialmente_avaliada PASSED                                    [  5%]
apps/academico/tests/test_services.py::TestRelatorioTurma::test_gerar_relatorio_turma_valida_valores PASSED                                           [  5%]
apps/academico/tests/test_views.py::TestDownloadCertificadoIndividual::test_sem_autenticacao_redireciona PASSED                                       [  5%]
apps/academico/tests/test_views.py::TestDownloadCertificadoIndividual::test_aluno_aprovado_gera_pdf PASSED                                            [  5%]
apps/academico/tests/test_views.py::TestDownloadCertificadoIndividual::test_aluno_reprovado_retorna_400 PASSED                                        [  6%]
apps/academico/tests/test_views.py::TestDownloadCertificadoIndividual::test_avaliacao_inexistente_retorna_404 PASSED                                  [  6%]
apps/academico/tests/test_views.py::TestPreviewCertificado::test_sem_autenticacao_redireciona PASSED                                                  [  6%]
apps/academico/tests/test_views.py::TestPreviewCertificado::test_aluno_aprovado_inline PASSED                                                         [  6%]
apps/academico/tests/test_views.py::TestPreviewCertificado::test_aluno_reprovado_retorna_400 PASSED                                                   [  6%]
apps/academico/tests/test_views.py::TestDownloadCertificadosLote::test_sem_ids_retorna_400 PASSED                                                     [  6%]
apps/academico/tests/test_views.py::TestDownloadCertificadosLote::test_ids_invalidos_retorna_400 PASSED                                               [  6%]
apps/academico/tests/test_views.py::TestDownloadCertificadosLote::test_apenas_aprovados_no_zip PASSED                                                 [  6%]
apps/academico/tests/test_views.py::TestDownloadCertificadosLote::test_zip_com_multiplos_certificados PASSED                                          [  7%]
apps/accounts/tests/test_admin.py::TestCustomAdminSite::test_admin_index_status_200 PASSED                                                            [  7%]
apps/accounts/tests/test_admin.py::TestCustomAdminSite::test_admin_index_sem_login_redirect PASSED                                                    [  7%]
apps/accounts/tests/test_admin.py::TestCustomAdminSite::test_dashboard_status_200 PASSED                                                              [  7%]
apps/accounts/tests/test_admin.py::TestCustomAdminSite::test_dashboard_sem_login_redirect PASSED                                                      [  7%]
apps/accounts/tests/test_admin.py::TestUsuarioAdminList::test_usuario_admin_list_status_200 PASSED                                                    [  7%]
apps/accounts/tests/test_admin.py::TestUsuarioAdminList::test_usuario_admin_list_sem_login_redirect PASSED                                            [  7%]
apps/accounts/tests/test_admin.py::TestUsuarioAdminList::test_usuario_admin_list_pesquisa_por_username PASSED                                         [  8%]
apps/accounts/tests/test_admin.py::TestUsuarioAdminAdd::test_usuario_admin_add_status_200 PASSED                                                      [  8%]
apps/accounts/tests/test_admin.py::TestUsuarioAdminAdd::test_usuario_admin_add_usuario PASSED                                                         [  8%]
apps/accounts/tests/test_admin.py::TestUsuarioAdminActionGerarSenhaProvisoria::test_gerar_senha_provisoria_seleciona_1 PASSED                         [  8%]
apps/accounts/tests/test_admin.py::TestUsuarioAdminActionGerarSenhaProvisoria::test_gerar_senha_provisoria_seleciona_2_falha PASSED                   [  8%]
apps/accounts/tests/test_middleware.py::test_usuario_nao_autenticado_passa PASSED                                                                     [  8%]
apps/accounts/tests/test_middleware.py::test_usuario_sem_must_change_password_passa PASSED                                                            [  8%]
apps/accounts/tests/test_middleware.py::test_usuario_com_must_change_password_url_liberada_staff PASSED                                               [  8%]
apps/accounts/tests/test_middleware.py::test_usuario_com_must_change_password_url_restrita_staff PASSED                                               [  9%]
apps/accounts/tests/test_middleware.py::test_interessado_com_must_change_password_url_restrita PASSED                                                 [  9%]
apps/accounts/tests/test_middleware.py::test_static_url_liberada_mesmo_com_must_change_password PASSED                                                [  9%]
apps/accounts/tests/test_middleware.py::test_media_url_liberada_mesmo_com_must_change_password PASSED                                                 [  9%]
apps/accounts/tests/test_middleware.py::test_url_admin_login_liberada PASSED                                                                          [  9%]
apps/accounts/tests/test_middleware.py::test_url_admin_logout_liberada PASSED                                                                         [  9%]
apps/accounts/tests/test_models.py::test_criar_usuario_com_cpf_valido PASSED                                                                          [  9%]
apps/accounts/tests/test_models.py::test_criar_usuario_com_cpf_invalido[1234567890] PASSED                                                            [  9%]
apps/accounts/tests/test_models.py::test_criar_usuario_com_cpf_invalido[123456789012] PASSED                                                          [ 10%]
apps/accounts/tests/test_models.py::test_cpf_unico PASSED                                                                                             [ 10%]
apps/accounts/tests/test_models.py::test_usuario_staff_pode_login PASSED                                                                              [ 10%]
apps/accounts/tests/test_models.py::test_usuario_nao_staff_nao_pode_login_staff PASSED                                                                [ 10%]
apps/accounts/tests/test_models.py::test_criar_usuario_sem_username_falha PASSED                                                                      [ 10%]
apps/accounts/tests/test_models.py::test_criar_usuario_sem_password_falha PASSED                                                                      [ 10%]
apps/accounts/tests/test_models.py::test_criar_superuser_is_staff PASSED                                                                              [ 10%]
apps/accounts/tests/test_models.py::test_criar_superuser_is_superuser PASSED                                                                          [ 10%]
apps/accounts/tests/test_models.py::test_usuario_str_retorna_username PASSED                                                                          [ 11%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_login_staff_form_tem_csrf PASSED                                                           [ 11%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_login_staff_get PASSED                                                                     [ 11%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_login_staff_inativo_falha PASSED                                                           [ 11%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_login_staff_invalido PASSED                                                                [ 11%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_login_staff_nao_staff PASSED                                                               [ 11%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_login_staff_valido PASSED                                                                  [ 11%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_logout_staff PASSED                                                                        [ 12%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_logout_staff_get_desloga PASSED                                                            [ 12%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_nao_staff_redirecionado_ao_acessar_pagina_staff PASSED                                     [ 12%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_staff_acessa_pagina_restrita_apos_login PASSED                                             [ 12%]
apps/accounts/tests/test_views_exclusao.py::TestListarSolicitacoesView::test_listar_solicitacoes_status_200 PASSED                                    [ 12%]
apps/accounts/tests/test_views_exclusao.py::TestListarSolicitacoesView::test_listar_solicitacoes_sem_login_redirect PASSED                            [ 12%]
apps/accounts/tests/test_views_exclusao.py::TestListarSolicitacoesView::test_listar_solicitacoes_nao_staff_redirect PASSED                            [ 12%]
apps/accounts/tests/test_views_exclusao.py::TestListarSolicitacoesView::test_listar_solicitacoes_contexto_tem_pendentes PASSED                        [ 12%]
apps/accounts/tests/test_views_exclusao.py::TestListarSolicitacoesView::test_listar_solicitacoes_contexto_tem_aprovadas PASSED                        [ 13%]
apps/accounts/tests/test_views_exclusao.py::TestListarSolicitacoesView::test_listar_solicitacoes_contexto_tem_recusadas PASSED                        [ 13%]
apps/accounts/tests/test_views_exclusao.py::TestDetalheSolicitacaoView::test_detalhe_solicitacao_status_200 PASSED                                    [ 13%]
apps/accounts/tests/test_views_exclusao.py::TestDetalheSolicitacaoView::test_detalhe_solicitacao_sem_login_redirect PASSED                            [ 13%]
apps/accounts/tests/test_views_exclusao.py::TestDetalheSolicitacaoView::test_detalhe_solicitacao_404 PASSED                                           [ 13%]
apps/accounts/tests/test_views_exclusao.py::TestDetalheSolicitacaoView::test_detalhe_solicitacao_aprovar PASSED                                       [ 13%]
apps/accounts/tests/test_views_exclusao.py::TestDetalheSolicitacaoView::test_detalhe_solicitacao_recusar PASSED                                       [ 13%]
apps/accounts/tests/test_views_exclusao.py::TestDetalheSolicitacaoView::test_detalhe_solicitacao_acao_invalida PASSED                                 [ 13%]
apps/accounts/tests/test_views_exclusao.py::TestDetalheSolicitacaoView::test_detalhe_solicitacao_sem_parecer PASSED                                   [ 14%]
apps/accounts/tests/test_views_exclusao.py::TestAnonimizarInteressado::test_anonimizar_interessado_limpa_campos PASSED                                [ 14%]
apps/accounts/tests/test_views_exclusao.py::TestAnonimizarInteressado::test_anonimizar_interessado_mantem_registro PASSED                             [ 14%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_metricas_gerais PASSED                                         [ 14%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_distribuicao_sexo PASSED                                       [ 14%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_distribuicao_fototipo PASSED                                   [ 14%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_distribuicao_escolaridade PASSED                               [ 14%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_distribuicao_programas_sociais PASSED                          [ 14%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_distribuicao_deficiencias PASSED                               [ 15%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_tipos_deficiencia PASSED                                       [ 15%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_faixas_etarias PASSED                                          [ 15%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_obter_contexto_completo PASSED                                          [ 15%]
apps/dashboard/tests/test_services.py::TestDashboardEventosService::test_calcular_metricas_gerais PASSED                                              [ 15%]
apps/dashboard/tests/test_services.py::TestDashboardEventosService::test_calcular_turmas_por_status PASSED                                            [ 15%]
apps/dashboard/tests/test_services.py::TestDashboardEventosService::test_calcular_eventos_por_status PASSED                                           [ 15%]
apps/dashboard/tests/test_services.py::TestDashboardEventosService::test_calcular_top_eventos_inscricoes PASSED                                       [ 16%]
apps/dashboard/tests/test_services.py::TestDashboardEventosService::test_obter_contexto_completo PASSED                                               [ 16%]
apps/dashboard/tests/test_services.py::TestDashboardAcademicoService::test_calcular_metricas_avaliacoes PASSED                                        [ 16%]
apps/dashboard/tests/test_services.py::TestDashboardAcademicoService::test_calcular_taxa_aprovacao PASSED                                             [ 16%]
apps/dashboard/tests/test_services.py::TestDashboardAcademicoService::test_calcular_top_cursos_aprovados PASSED                                       [ 16%]
apps/dashboard/tests/test_services.py::TestDashboardAcademicoService::test_obter_contexto_completo PASSED                                             [ 16%]
apps/dashboard/tests/test_services.py::TestDashboardProcessoSeletivoService::test_calcular_metricas_inscricoes PASSED                                 [ 16%]
apps/dashboard/tests/test_services.py::TestDashboardProcessoSeletivoService::test_calcular_metricas_classificacoes PASSED                             [ 16%]
apps/dashboard/tests/test_services.py::TestDashboardProcessoSeletivoService::test_calcular_top_eventos_inscricoes PASSED                              [ 17%]
apps/dashboard/tests/test_services.py::TestDashboardProcessoSeletivoService::test_obter_contexto_completo PASSED                                      [ 17%]
apps/dashboard/tests/test_utils_pdf.py::TestCriarGraficoPizza::test_dados_validos_retorna_buffer PASSED                                               [ 17%]
apps/dashboard/tests/test_utils_pdf.py::TestCriarGraficoPizza::test_todos_valores_zero_retorna_none PASSED                                            [ 17%]
apps/dashboard/tests/test_utils_pdf.py::TestCriarGraficoPizza::test_lista_vazia_retorna_none PASSED                                                   [ 17%]
apps/dashboard/tests/test_utils_pdf.py::TestCriarGraficoPizza::test_um_item_valido_retorna_buffer PASSED                                              [ 17%]
apps/dashboard/tests/test_utils_pdf.py::TestCriarGraficoBarras::test_dados_validos_retorna_buffer PASSED                                              [ 17%]
apps/dashboard/tests/test_utils_pdf.py::TestGerarPdfInteressados::test_context_minimo_retorna_buffer PASSED                                           [ 17%]
apps/dashboard/tests/test_utils_pdf.py::TestGerarPdfEventos::test_context_minimo_retorna_buffer PASSED                                                [ 18%]
apps/dashboard/tests/test_utils_pdf.py::TestGerarPdfAcademico::test_context_minimo_retorna_buffer PASSED                                              [ 18%]
apps/dashboard/tests/test_utils_pdf.py::TestGerarPdfProcessoSeletivo::test_context_minimo_retorna_buffer PASSED                                       [ 18%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_academico_non_staff_redireciona PASSED                                         [ 18%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_academico_sem_auth_redireciona PASSED                                          [ 18%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_academico_sem_dados_nao_quebra PASSED                                          [ 18%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_academico_staff_200 PASSED                                                     [ 18%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_eventos_sem_auth_redireciona PASSED                                            [ 18%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_eventos_staff_200 PASSED                                                       [ 19%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_interessados_sem_auth_redireciona PASSED                                       [ 19%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_interessados_staff_200 PASSED                                                  [ 19%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_interessados_total_zero_nao_quebra PASSED                                      [ 19%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_lgpd_sem_auth_redireciona PASSED                                               [ 19%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_lgpd_staff_200 PASSED                                                          [ 19%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_processo_seletivo_sem_auth_redireciona PASSED                                  [ 19%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_processo_seletivo_staff_200 PASSED                                             [ 20%]
apps/dashboard/tests/test_views.py::TestDashboardPdfViews::test_pdf_academico_sem_auth_redireciona PASSED                                             [ 20%]
apps/dashboard/tests/test_views.py::TestDashboardPdfViews::test_pdf_academico_staff_200 PASSED                                                        [ 20%]
apps/dashboard/tests/test_views.py::TestDashboardPdfViews::test_pdf_eventos_sem_auth_redireciona PASSED                                               [ 20%]
apps/dashboard/tests/test_views.py::TestDashboardPdfViews::test_pdf_eventos_staff_200 PASSED                                                          [ 20%]
apps/dashboard/tests/test_views.py::TestDashboardPdfViews::test_pdf_interessados_sem_auth_redireciona PASSED                                          [ 20%]
apps/dashboard/tests/test_views.py::TestDashboardPdfViews::test_pdf_interessados_sem_dados_nao_quebra PASSED                                          [ 20%]
apps/dashboard/tests/test_views.py::TestDashboardPdfViews::test_pdf_interessados_staff_200 PASSED                                                     [ 20%]
apps/dashboard/tests/test_views.py::TestDashboardPdfViews::test_pdf_processo_seletivo_sem_auth_redireciona PASSED                                     [ 21%]
apps/dashboard/tests/test_views.py::TestDashboardPdfViews::test_pdf_processo_seletivo_staff_200 PASSED                                                [ 21%]
apps/eventos/tests/test_admin-copy1.py::EventoAdminTest::test_evento_add_view PASSED                                                                  [ 21%]
apps/eventos/tests/test_admin-copy1.py::EventoAdminTest::test_evento_change_view PASSED                                                               [ 21%]
apps/eventos/tests/test_admin-copy1.py::EventoAdminTest::test_evento_criterios_inline PASSED                                                          [ 21%]
apps/eventos/tests/test_admin-copy1.py::EventoAdminTest::test_evento_delete_view PASSED                                                               [ 21%]
apps/eventos/tests/test_admin-copy1.py::EventoAdminTest::test_evento_individual_date_methods PASSED                                                   [ 21%]
apps/eventos/tests/test_admin-copy1.py::EventoAdminTest::test_evento_list_display PASSED                                                              [ 21%]
apps/eventos/tests/test_admin-copy1.py::EventoAdminTest::test_evento_list_view PASSED                                                                 [ 22%]
apps/eventos/tests/test_admin-copy1.py::EventoAdminTest::test_evento_search PASSED                                                                    [ 22%]
apps/eventos/tests/test_admin-copy1.py::EventoAdminTest::test_evento_turmas_inline PASSED                                                             [ 22%]
apps/eventos/tests/test_admin-copy1.py::StatusAdminTest::test_status_add_view PASSED                                                                  [ 22%]
apps/eventos/tests/test_admin-copy1.py::StatusAdminTest::test_status_change_view PASSED                                                               [ 22%]
apps/eventos/tests/test_admin-copy1.py::StatusAdminTest::test_status_delete_view PASSED                                                               [ 22%]
apps/eventos/tests/test_admin-copy1.py::StatusAdminTest::test_status_list_view PASSED                                                                 [ 22%]
apps/eventos/tests/test_admin-copy1.py::StatusAdminTest::test_status_search PASSED                                                                    [ 22%]
apps/eventos/tests/test_admin-copy1.py::CriterioAdminTest::test_criterio_add_view PASSED                                                              [ 23%]
apps/eventos/tests/test_admin-copy1.py::CriterioAdminTest::test_criterio_list_filter PASSED                                                           [ 23%]
apps/eventos/tests/test_admin-copy1.py::TurmaAdminTest::test_turma_add_view PASSED                                                                    [ 23%]
apps/eventos/tests/test_admin-copy1.py::TurmaAdminTest::test_turma_change_view PASSED                                                                 [ 23%]
apps/eventos/tests/test_admin-copy1.py::TurmaAdminTest::test_turma_delete_view PASSED                                                                 [ 23%]
apps/eventos/tests/test_admin-copy1.py::TurmaAdminTest::test_turma_list_display_evento PASSED                                                         [ 23%]
apps/eventos/tests/test_admin-copy1.py::TurmaAdminTest::test_turma_list_view PASSED                                                                   [ 23%]
apps/eventos/tests/test_admin-copy1.py::TurmaAdminTest::test_turma_search PASSED                                                                      [ 24%]
apps/eventos/tests/test_admin-copy1.py::HorarioAdminTest::test_horario_add_view PASSED                                                                [ 24%]
apps/eventos/tests/test_admin-copy1.py::HorarioAdminTest::test_horario_change_view PASSED                                                             [ 24%]
apps/eventos/tests/test_admin-copy1.py::HorarioAdminTest::test_horario_delete_view PASSED                                                             [ 24%]
apps/eventos/tests/test_admin-copy1.py::HorarioAdminTest::test_horario_dia_semana_filter PASSED                                                       [ 24%]
apps/eventos/tests/test_admin-copy1.py::HorarioAdminTest::test_horario_list_filter PASSED                                                             [ 24%]
apps/eventos/tests/test_admin-copy1.py::HorarioAdminTest::test_horario_list_view PASSED                                                               [ 24%]
apps/eventos/tests/test_admin-copy1.py::HorarioAdminTest::test_horario_search PASSED                                                                  [ 24%]
apps/eventos/tests/test_admin.py::TestEventoAdminConfig::test_list_display PASSED                                                                     [ 25%]
apps/eventos/tests/test_admin.py::TestEventoAdminConfig::test_list_filter PASSED                                                                      [ 25%]
apps/eventos/tests/test_admin.py::TestEventoAdminConfig::test_search_fields PASSED                                                                    [ 25%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_changelist_carrega PASSED                                                           [ 25%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_busca_por_nome PASSED                                                               [ 25%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_filtrar_por_status PASSED                                                           [ 25%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_paginacao PASSED                                                                    [ 25%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_busca_vazia PASSED                                                                  [ 25%]
apps/eventos/tests/test_admin.py::TestStatusAdminChangeList::test_changelist_carrega PASSED                                                           [ 26%]
apps/eventos/tests/test_admin.py::TestStatusAdminChangeList::test_busca_por_nome PASSED                                                               [ 26%]
apps/eventos/tests/test_admin.py::TestTurmaAdminChangeList::test_changelist_carrega PASSED                                                            [ 26%]
apps/eventos/tests/test_admin.py::TestTurmaAdminChangeList::test_busca_por_nome PASSED                                                                [ 26%]
apps/eventos/tests/test_admin.py::TestEventoAdminViews::test_add_view PASSED                                                                          [ 26%]
apps/eventos/tests/test_admin.py::TestEventoAdminViews::test_change_view PASSED                                                                       [ 26%]
apps/eventos/tests/test_admin.py::TestEventoAdminViews::test_delete_view PASSED                                                                       [ 26%]
apps/eventos/tests/test_admin.py::TestStatusAdminViews::test_add_view PASSED                                                                          [ 26%]
apps/eventos/tests/test_admin.py::TestStatusAdminViews::test_change_view PASSED                                                                       [ 27%]
apps/eventos/tests/test_admin.py::TestStatusAdminViews::test_delete_view PASSED                                                                       [ 27%]
apps/eventos/tests/test_admin.py::TestTurmaAdminViews::test_add_view PASSED                                                                           [ 27%]
apps/eventos/tests/test_admin.py::TestTurmaAdminViews::test_change_view PASSED                                                                        [ 27%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_status_colorido PASSED                                                                 [ 27%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_vagas_inscritos_sem_inscricoes PASSED                                                  [ 27%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_vagas_inscritos_com_inscricoes PASSED                                                  [ 27%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_data_inicio_inscricao_formatada PASSED                                                 [ 28%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_data_fim_inscricao_formatada PASSED                                                    [ 28%]
apps/eventos/tests/test_admin.py::TestEventoAdminInlines::test_exibe_inline_criterios PASSED                                                          [ 28%]
apps/eventos/tests/test_admin.py::TestEventoAdminInlines::test_exibe_inline_turmas PASSED                                                             [ 28%]
apps/eventos/tests/test_admin.py::TestEventoAdminInlines::test_change_view_carrega_com_inlines PASSED                                                 [ 28%]
apps/eventos/tests/test_admin.py::TestHorarioAdminChangeList::test_changelist_carrega PASSED                                                          [ 28%]
apps/eventos/tests/test_admin.py::TestHorarioAdminChangeList::test_filtro_dia_semana PASSED                                                           [ 28%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_classificar_inscricoes_action_existe PASSED                                          [ 28%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_cor_visual_retorna_html_com_cor PASSED                                               [ 29%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_data_fim_evento_formatada PASSED                                                     [ 29%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_data_fim_inscricao_formatada PASSED                                                  [ 29%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_data_inicio_evento_formatada PASSED                                                  [ 29%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_data_inicio_inscricao_formatada PASSED                                               [ 29%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_desfazer_classificacao_action_existe PASSED                                          [ 29%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_exportar_classificacao_excel_action_existe PASSED                                    [ 29%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_status_admin_list_display PASSED                                                     [ 29%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_vagas_inscritos_cor_laranja PASSED                                                   [ 30%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_vagas_inscritos_cor_verde PASSED                                                     [ 30%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_vagas_inscritos_cor_vermelho PASSED                                                  [ 30%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_usuario_anonimo_retorna_lista_vazia PASSED                               [ 30%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_usuario_nao_staff_retorna_lista_vazia PASSED                             [ 30%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_sem_eventos_retorna_lista_vazia PASSED                                   [ 30%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao1_status_correto_sem_alerta PASSED                            [ 30%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao1_status_errado_gera_alerta PASSED                            [ 30%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao2_status_valido_sem_alerta PASSED                             [ 31%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao2_status_invalido_gera_alerta PASSED                          [ 31%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao3_status_correto_sem_alerta PASSED                            [ 31%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao3_status_errado_gera_alerta PASSED                            [ 31%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao4_status_valido_sem_alerta PASSED                             [ 31%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao4_status_invalido_gera_alerta PASSED                          [ 31%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao4_cancelado_sem_alerta PASSED                                 [ 31%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_multiplos_eventos_com_alerta PASSED                                      [ 32%]
apps/eventos/tests/test_models.py::TestStatusModel::test_create_status PASSED                                                                         [ 32%]
apps/eventos/tests/test_models.py::TestStatusModel::test_status_str PASSED                                                                            [ 32%]
apps/eventos/tests/test_models.py::TestStatusModel::test_status_ordem_unique PASSED                                                                   [ 32%]
apps/eventos/tests/test_models.py::TestStatusModel::test_status_cor_valid_hex PASSED                                                                  [ 32%]
apps/eventos/tests/test_models.py::TestEventoModel::test_create_evento PASSED                                                                         [ 32%]
apps/eventos/tests/test_models.py::TestEventoModel::test_evento_str PASSED                                                                            [ 32%]
apps/eventos/tests/test_models.py::TestEventoModel::test_evento_foreign_key_status PASSED                                                             [ 32%]
apps/eventos/tests/test_models.py::TestEventoModel::test_evento_total_vagas_positive PASSED                                                           [ 33%]
apps/eventos/tests/test_models.py::TestEventoModel::test_evento_data_inicio_inscricao_before_fim PASSED                                               [ 33%]
apps/eventos/tests/test_models.py::TestEventoModel::test_evento_data_inicio_evento_before_fim PASSED                                                  [ 33%]
apps/eventos/tests/test_models.py::TestEventoModel::test_evento_datas_evento_validas PASSED                                                           [ 33%]
apps/eventos/tests/test_models.py::TestCriterioModel::test_create_criterio PASSED                                                                     [ 33%]
apps/eventos/tests/test_models.py::TestCriterioModel::test_criterio_str PASSED                                                                        [ 33%]
apps/eventos/tests/test_models.py::TestCriterioModel::test_criterio_codigo_unique PASSED                                                              [ 33%]
apps/eventos/tests/test_models.py::TestCriterioModel::test_criterio_pontos_non_negative PASSED                                                        [ 33%]
apps/eventos/tests/test_models.py::TestCriterioModel::test_criterio_categoria_choices PASSED                                                          [ 34%]
apps/eventos/tests/test_models.py::TestTurmaModel::test_create_turma PASSED                                                                           [ 34%]
apps/eventos/tests/test_models.py::TestTurmaModel::test_turma_str PASSED                                                                              [ 34%]
apps/eventos/tests/test_models.py::TestTurmaModel::test_turma_foreign_key_evento PASSED                                                               [ 34%]
apps/eventos/tests/test_models.py::TestTurmaModel::test_turma_capacidade_positive PASSED                                                              [ 34%]
apps/eventos/tests/test_models.py::TestHorarioModel::test_create_horario PASSED                                                                       [ 34%]
apps/eventos/tests/test_models.py::TestHorarioModel::test_horario_foreign_key_turma PASSED                                                            [ 34%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_criar_criterio_valido PASSED                                                      [ 34%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_ler_criterio PASSED                                                               [ 35%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_atualizar_criterio PASSED                                                         [ 35%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_deletar_criterio PASSED                                                           [ 35%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_codigo_unico PASSED                                                               [ 35%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_codigo_valido PASSED                                                              [ 35%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_pontos_positivo PASSED                                                            [ 35%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_pontos_zero_permitido PASSED                                                      [ 35%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_criterio_ativo_padrao PASSED                                                      [ 36%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_criterio_inativo PASSED                                                           [ 36%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_criterio_com_eventos PASSED                                                       [ 36%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_criterio_sem_eventos PASSED                                                       [ 36%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_str_representation PASSED                                                         [ 36%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_filtro_por_ativo PASSED                                                           [ 36%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_queryset_count PASSED                                                             [ 36%]
apps/eventos/tests/test_models_evento.py::TestEventoCRUD::test_criar_evento_valido PASSED                                                             [ 36%]
apps/eventos/tests/test_models_evento.py::TestEventoCRUD::test_ler_evento PASSED                                                                      [ 37%]
apps/eventos/tests/test_models_evento.py::TestEventoCRUD::test_atualizar_evento PASSED                                                                [ 37%]
apps/eventos/tests/test_models_evento.py::TestEventoCRUD::test_deletar_evento PASSED                                                                  [ 37%]
apps/eventos/tests/test_models_evento.py::TestEventoCRUD::test_multiplos_eventos PASSED                                                               [ 37%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_data_inicio_inscricao_antes_fim_inscricao PASSED                                 [ 37%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_data_fim_inscricao_antes_inicio_evento PASSED                                    [ 37%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_data_inicio_evento_antes_fim_evento PASSED                                       [ 37%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_datas_validas_factory PASSED                                                     [ 37%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_clean_valida_datas PASSED                                                        [ 38%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_total_vagas_positivo PASSED                                                      [ 38%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_total_vagas_grande_numero PASSED                                                 [ 38%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_total_vagas_zero_permitido PASSED                                                [ 38%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_com_status PASSED                                                             [ 38%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_sem_status_invalido PASSED                                                    [ 38%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_com_turmas PASSED                                                             [ 38%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_multiplas_turmas PASSED                                                       [ 38%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_com_criterios PASSED                                                          [ 39%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_multiplos_criterios PASSED                                                    [ 39%]
apps/eventos/tests/test_models_evento.py::TestEventoTimestamps::test_evento_sem_criterios PASSED                                                      [ 39%]
apps/eventos/tests/test_models_evento.py::TestEventoTimestamps::test_deletar_evento_deleta_turmas PASSED                                              [ 39%]
apps/eventos/tests/test_models_evento.py::TestEventoTimestamps::test_criado_em_existe PASSED                                                          [ 39%]
apps/eventos/tests/test_models_evento.py::TestEventoTimestamps::test_atualizado_em_existe PASSED                                                      [ 39%]
apps/eventos/tests/test_models_evento.py::TestEventoTimestamps::test_atualizado_em_atualiza PASSED                                                    [ 39%]
apps/eventos/tests/test_models_evento.py::TestEventoMetodos::test_inscricoes_abertas PASSED                                                           [ 40%]
apps/eventos/tests/test_models_evento.py::TestEventoMetodos::test_inscricoes_fechadas PASSED                                                          [ 40%]
apps/eventos/tests/test_models_evento.py::TestEventoMetodos::test_validacao_datas_inscricao PASSED                                                    [ 40%]
apps/eventos/tests/test_models_evento.py::TestEventoMetodos::test_validacao_datas_evento PASSED                                                       [ 40%]
apps/eventos/tests/test_models_evento.py::TestEventoMetodos::test_formatacao_datas PASSED                                                             [ 40%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_filtro_por_status PASSED                                                           [ 40%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_filtro_por_ativo PASSED                                                            [ 40%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_queryset_count PASSED                                                              [ 40%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_queryset_exists PASSED                                                             [ 41%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_nome_obrigatorio PASSED                                                            [ 41%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_str_representation PASSED                                                          [ 41%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoCreation::test_criar_evento PASSED                                                       [ 41%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoCreation::test_str_evento PASSED                                                         [ 41%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoCreation::test_defaults_evento PASSED                                                    [ 41%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoCreation::test_status_evento PASSED                                                      [ 41%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoCreation::test_multiplos_eventos PASSED                                                  [ 41%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoDatas::test_fim_inscricao_antes_inicio PASSED                                   [ 42%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoDatas::test_fim_evento_antes_inicio PASSED                                      [ 42%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoDatas::test_datas_validas PASSED                                                [ 42%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoDatas::test_datas_iguais PASSED                                                 [ 42%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoVagas::test_vagas_negativas PASSED                                              [ 42%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoVagas::test_vagas_altas PASSED                                                  [ 42%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoRelacionamentos::test_has_status PASSED                                                  [ 42%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoRelacionamentos::test_status_has_eventos PASSED                                          [ 42%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoRelacionamentos::test_protect_status PASSED                                              [ 43%]
apps/eventos/tests/test_models_evento_expanded.py::TestTurmaHorario::test_turma_horario_relation PASSED                                               [ 43%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_criar_horario_valido PASSED                                                         [ 43%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_ler_horario PASSED                                                                  [ 43%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_atualizar_horario PASSED                                                            [ 43%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_deletar_horario PASSED                                                              [ 43%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_dia_semana_valido PASSED                                                            [ 43%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_multiplos_horarios_mesma_turma PASSED                                               [ 44%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_hora_inicio_antes_fim PASSED                                                        [ 44%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_hora_inicio_igual_fim_permitido PASSED                                              [ 44%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_horario_com_turma PASSED                                                            [ 44%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_horario_sem_turma_invalido PASSED                                                   [ 44%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_turma_tem_multiplos_horarios PASSED                                                 [ 44%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_str_representation PASSED                                                           [ 44%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_filtro_por_turma PASSED                                                             [ 44%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_queryset_count PASSED                                                               [ 45%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_criar_turma_valida PASSED                                                               [ 45%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_ler_turma PASSED                                                                        [ 45%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_atualizar_turma PASSED                                                                  [ 45%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_deletar_turma PASSED                                                                    [ 45%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_multiplas_turmas PASSED                                                                 [ 45%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_datas_validas_factory PASSED                                                            [ 45%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_capacidade_positiva PASSED                                                              [ 45%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_capacidade_grande_numero PASSED                                                         [ 46%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_capacidade_zero_permitido PASSED                                                        [ 46%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_turma_com_evento PASSED                                                                 [ 46%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_turma_sem_evento_invalido PASSED                                                        [ 46%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_turma_com_horarios PASSED                                                               [ 46%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_turma_multiplos_horarios PASSED                                                         [ 46%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_deletar_turma_deleta_horarios PASSED                                                    [ 46%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_criado_em_existe PASSED                                                                 [ 46%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_atualizado_em_atualiza PASSED                                                           [ 47%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_str_representation PASSED                                                               [ 47%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_nome_obrigatorio PASSED                                                                 [ 47%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_filtro_por_evento PASSED                                                                [ 47%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_filtro_por_turno PASSED                                                                 [ 47%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_queryset_count PASSED                                                                   [ 47%]
apps/interessados/tests/test_admin.py::TestSexoAdmin::test_list_display PASSED                                                                        [ 47%]
apps/interessados/tests/test_admin.py::TestSexoAdmin::test_search_fields PASSED                                                                       [ 48%]
apps/interessados/tests/test_admin.py::TestFototipoAdmin::test_list_display PASSED                                                                    [ 48%]
apps/interessados/tests/test_admin.py::TestFototipoAdmin::test_search_fields PASSED                                                                   [ 48%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_data_nascimento_formatada_com_data PASSED                                    [ 48%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_data_nascimento_formatada_sem_data PASSED                                    [ 48%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_sexo_display_com_sexo PASSED                                                 [ 48%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_sexo_display_sem_sexo PASSED                                                 [ 48%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_fototipo_display_com_fototipo PASSED                                         [ 48%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_fototipo_display_sem_fototipo PASSED                                         [ 49%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_programa_social_display_true PASSED                                          [ 49%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_programa_social_display_false PASSED                                         [ 49%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_necessidades_especiais_display_true PASSED                                   [ 49%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_necessidades_especiais_display_false PASSED                                  [ 49%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_celular_formatado_11_digitos PASSED                                          [ 49%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_celular_formatado_vazio PASSED                                               [ 49%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_telefone_formatado_10_digitos PASSED                                         [ 49%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_telefone_formatado_vazio PASSED                                              [ 50%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_is_active_display_ativo PASSED                                               [ 50%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_is_active_display_inativo PASSED                                             [ 50%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_short_descriptions PASSED                                                    [ 50%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminSaveModel::test_save_model_com_senha_nova_aplica_set_password PASSED                       [ 50%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminActions::test_ativar_interessados PASSED                                                   [ 50%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminActions::test_desativar_interessados PASSED                                                [ 50%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminActions::test_gerar_senha_provisoria_rejeita_multiplos PASSED                              [ 50%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminActions::test_gerar_senha_provisoria_um_interessado PASSED                                 [ 51%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminActions::test_exportar_interessados_retorna_csv PASSED                                     [ 51%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminActions::test_exportar_interessados_conteudo_tem_cabecalho PASSED                          [ 51%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_get_interessado_retorna_nome PASSED                                          [ 51%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_get_status_valido PASSED                                                     [ 51%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_get_status_expirado PASSED                                                   [ 51%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_get_status_usado PASSED                                                      [ 51%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_limpar_tokens_expirados PASSED                                               [ 52%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_limpar_tokens_usados PASSED                                                  [ 52%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_limpar_todos_invalidos PASSED                                                [ 52%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_has_add_permission_false PASSED                                              [ 52%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_has_change_permission_false PASSED                                           [ 52%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_has_delete_permission_superuser_true PASSED                                  [ 52%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_has_delete_permission_normal_user_false PASSED                               [ 52%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendAuthenticate::test_autentica_com_cpf_e_senha_validos PASSED                     [ 52%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendAuthenticate::test_autentica_com_senha_errada_retorna_none PASSED               [ 53%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendAuthenticate::test_autentica_com_cpf_inexistente_retorna_none PASSED            [ 53%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendAuthenticate::test_autentica_com_cpf_none_retorna_none PASSED                   [ 53%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendAuthenticate::test_autentica_com_senha_none_retorna_none PASSED                 [ 53%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendAuthenticate::test_autentica_interessado_inativo_retorna_none PASSED            [ 53%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendAuthenticate::test_autentica_sem_request_mas_com_cpf_valido PASSED              [ 53%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendGetUser::test_get_user_com_id_valido_retorna_interessado PASSED                 [ 53%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendGetUser::test_get_user_com_id_inexistente_retorna_none PASSED                   [ 53%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendGetUser::test_get_user_interessado_inativo_retorna_none PASSED                  [ 54%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_valido_dados_minimos PASSED                                         [ 54%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_cpf_duplicado PASSED                                                [ 54%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_email_duplicado PASSED                                              [ 54%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_senhas_nao_conferem PASSED                                          [ 54%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_cpf_invalido_todos_iguais PASSED                                    [ 54%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cpf_valido_com_pontuacao PASSED                                              [ 54%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cpf_invalido_digito_verificador PASSED                                       [ 54%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cpf_muito_curto PASSED                                                       [ 55%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_sem_consentimento_lgpd PASSED                                       [ 55%]
apps/interessados/tests/test_forms.py::TestLoginInteressadoForm::test_login_valido PASSED                                                             [ 55%]
apps/interessados/tests/test_forms.py::TestLoginInteressadoForm::test_login_cpf_nao_cadastrado PASSED                                                 [ 55%]
apps/interessados/tests/test_forms.py::TestLoginInteressadoForm::test_login_senha_incorreta PASSED                                                    [ 55%]
apps/interessados/tests/test_forms.py::TestLoginInteressadoForm::test_login_interessado_inativo PASSED                                                [ 55%]
apps/interessados/tests/test_forms.py::TestLoginInteressadoForm::test_login_cpf_formatado_com_pontuacao PASSED                                        [ 55%]
apps/interessados/tests/test_forms.py::TestEdicaoInteressadoForm::test_edicao_valida_dados_minimos PASSED                                             [ 56%]
apps/interessados/tests/test_forms.py::TestEdicaoInteressadoForm::test_cpf_nao_aparece_na_edicao PASSED                                               [ 56%]
apps/interessados/tests/test_forms.py::TestEdicaoInteressadoForm::test_tentativa_alterar_cpf_ignorada PASSED                                          [ 56%]
apps/interessados/tests/test_forms.py::TestEdicaoInteressadoForm::test_edicao_sem_nome_rejeita PASSED                                                 [ 56%]
apps/interessados/tests/test_forms.py::TestEdicaoInteressadoForm::test_edicao_email_invalido_rejeita PASSED                                           [ 56%]
apps/interessados/tests/test_models.py::TestHashCPF::test_mesmo_cpf_mesmo_hash PASSED                                                                 [ 56%]
apps/interessados/tests/test_models.py::TestHashCPF::test_cpfs_diferentes_hashes_diferentes PASSED                                                    [ 56%]
apps/interessados/tests/test_models.py::TestHashCPF::test_hash_tem_64_caracteres PASSED                                                               [ 56%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_senha_nao_e_texto_puro PASSED                                                      [ 57%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_check_password_ok PASSED                                                           [ 57%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_check_password_errado PASSED                                                       [ 57%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_is_authenticated PASSED                                                            [ 57%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_is_anonymous PASSED                                                                [ 57%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_str_contem_nome PASSED                                                             [ 57%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_cpf_criptografado_no_banco PASSED                                                  [ 57%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_cpf_hash_unico PASSED                                                              [ 57%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_cpf_hash_busca_eficiente PASSED                                                    [ 58%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_nis_criptografado_no_banco PASSED                                                  [ 58%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_factory_cria_interessado_valido PASSED                                             [ 58%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_cpf_11_digitos_valido PASSED                                                       [ 58%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_cpf_formatado_aceito_pelo_model PASSED                                             [ 58%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_nis_valido PASSED                                                                  [ 58%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_nis_muito_curto_rejeita PASSED                                                     [ 58%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_cep_valido PASSED                                                                  [ 58%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_cep_muito_curto_rejeita PASSED                                                     [ 59%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_relacionamento_sexo PASSED                                                         [ 59%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_relacionamento_fototipo PASSED                                                     [ 59%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_relacionamentos_simultaneos PASSED                                                 [ 59%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_multiplas_deficiencias PASSED                                                      [ 59%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_tem_deficiencia_property PASSED                                                    [ 59%]
apps/interessados/tests/test_models.py::TestSolicitacaoExclusao::test_criada_com_status_pendente PASSED                                               [ 59%]
apps/interessados/tests/test_models.py::TestSolicitacaoExclusao::test_todos_os_status_sao_validos PASSED                                              [ 60%]
apps/interessados/tests/test_models.py::TestSolicitacaoExclusao::test_nome_solicitante_obrigatorio PASSED                                             [ 60%]
apps/interessados/tests/test_models.py::TestSolicitacaoExclusao::test_email_solicitante_opcional PASSED                                               [ 60%]
apps/interessados/tests/test_models.py::TestSolicitacaoExclusao::test_str_contem_status_e_nome PASSED                                                 [ 60%]
apps/interessados/tests/test_models.py::TestSexoModel::test_factory_cria_valido PASSED                                                                [ 60%]
apps/interessados/tests/test_models.py::TestSexoModel::test_str_retorna_nome PASSED                                                                   [ 60%]
apps/interessados/tests/test_models.py::TestSexoModel::test_unique_constraint_violado PASSED                                                          [ 60%]
apps/interessados/tests/test_models.py::TestFototipoModel::test_factory_cria_valido PASSED                                                            [ 60%]
apps/interessados/tests/test_models.py::TestFototipoModel::test_descricao_pode_ser_vazia PASSED                                                       [ 61%]
apps/interessados/tests/test_models.py::TestPasswordResetTokenModel::test_factory_cria_token_valido PASSED                                            [ 61%]
apps/interessados/tests/test_models.py::TestPasswordResetTokenModel::test_expiracao_futura PASSED                                                     [ 61%]
apps/interessados/tests/test_models.py::TestPasswordResetTokenModel::test_marca_como_usado PASSED                                                     [ 61%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_cadastro_url PASSED                                                                      [ 61%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_login_url PASSED                                                                         [ 61%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_logout_url PASSED                                                                        [ 61%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_meus_dados_url PASSED                                                                    [ 61%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_dashboard_url PASSED                                                                     [ 62%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_detalhes_url PASSED                                                                      [ 62%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_inscrever_evento_url PASSED                                                              [ 62%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_senha_recuperar_url PASSED                                                               [ 62%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_senha_recuperar_enviado_url PASSED                                                       [ 62%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_senha_redefinir_url PASSED                                                               [ 62%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_senha_redefinir_concluido_url PASSED                                                     [ 62%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_senha_sem_email_url PASSED                                                               [ 62%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_solicitar_exclusao_url PASSED                                                            [ 63%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_exclusao_solicitada_url PASSED                                                           [ 63%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_cadastro_path PASSED                                                                         [ 63%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_login_path PASSED                                                                            [ 63%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_logout_path PASSED                                                                           [ 63%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_meus_dados_path PASSED                                                                       [ 63%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_dashboard_path PASSED                                                                        [ 63%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_detalhes_path PASSED                                                                         [ 64%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_inscrever_evento_path PASSED                                                                 [ 64%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_senha_recuperar_path PASSED                                                                  [ 64%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_senha_recuperar_enviado_path PASSED                                                          [ 64%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_senha_redefinir_path PASSED                                                                  [ 64%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_senha_redefinir_concluido_path PASSED                                                        [ 64%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_senha_sem_email_path PASSED                                                                  [ 64%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_solicitar_exclusao_path PASSED                                                               [ 64%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_exclusao_solicitada_path PASSED                                                              [ 65%]
apps/interessados/tests/test_utils.py::TestCustomEmailBackendSSLContext::test_sem_certificate_desabilita_verificacao PASSED                           [ 65%]
apps/interessados/tests/test_utils.py::TestCustomEmailBackendSSLContext::test_com_ssl_certfile_mantem_verificacao PASSED                              [ 65%]
apps/interessados/tests/test_utils.py::TestCustomEmailBackendSSLContext::test_context_e_cached_property PASSED                                        [ 65%]
apps/interessados/tests/test_utils.py::TestCustomEmailBackendSSLContext::test_ssl_context_sem_cert_e_sem_keyfile PASSED                               [ 65%]
apps/interessados/tests/test_utils.py::TestCustomEmailBackendHeranca::test_herda_de_emailbackend PASSED                                               [ 65%]
apps/interessados/tests/test_utils.py::TestCustomEmailBackend::test_timeout_padrao_nao_definido PASSED                                                [ 65%]
apps/interessados/tests/test_utils.py::TestCustomEmailBackend::test_timeout_personalizado PASSED                                                      [ 65%]
apps/interessados/tests/test_views.py::TestPortalViews::test_portal_index PASSED                                                                      [ 66%]
apps/interessados/tests/test_views.py::TestInteressadosViews::test_cadastro_view_get PASSED                                                           [ 66%]
apps/interessados/tests/test_views.py::TestInteressadosViews::test_cadastro_view_post_valido PASSED                                                   [ 66%]
apps/interessados/tests/test_views.py::TestInteressadosViews::test_cadastro_post_com_dados_completos PASSED                                           [ 66%]
apps/interessados/tests/test_views.py::TestInteressadosViews::test_cadastro_rejeita_senha_fraca PASSED                                                [ 66%]
apps/interessados/tests/test_views.py::TestInteressadosViews::test_login_view_valido PASSED                                                           [ 66%]
apps/interessados/tests/test_views.py::TestInteressadosViews::test_login_sql_injection PASSED                                                         [ 66%]
apps/interessados/tests/test_views.py::TestInteressadosViews::test_login_nao_expoe_mensagem_diferenciada PASSED                                       [ 66%]
apps/interessados/tests/test_views.py::TestInteressadosViews::test_dashboard_requer_login PASSED                                                      [ 67%]
apps/interessados/tests/test_views.py::TestInteressadosViews::test_dashboard_com_login PASSED                                                         [ 67%]
apps/interessados/tests/test_views.py::TestInteressadosViews::test_meus_dados_view_get PASSED                                                         [ 67%]
apps/interessados/tests/test_views.py::TestInteressadosViews::test_meus_dados_edicao_valida PASSED                                                    [ 67%]
apps/interessados/tests/test_views.py::TestInteressadosViews::test_meus_dados_edicao_sem_nome_rejeita PASSED                                          [ 67%]
apps/interessados/tests/test_views.py::TestInteressadosViews::test_senha_recuperar_view PASSED                                                        [ 67%]
apps/interessados/tests/test_views.py::TestDashboardAutenticacao::test_nao_autenticado_redireciona_login PASSED                                       [ 67%]
apps/interessados/tests/test_views.py::TestDashboardAutenticacao::test_usuario_inativo_redireciona_login PASSED                                       [ 68%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_sem_login_redirect_para_login PASSED                                  [ 68%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_post_sem_login_redirect_para_login PASSED                             [ 68%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_interessado_inativo_logout_e_redirect PASSED                          [ 68%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_get_sem_pendente_retorna_200 PASSED                                   [ 68%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_get_com_pendente_redirect_dashboard PASSED                            [ 68%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_post_confirmacao_valida_cria_solicitacao PASSED                       [ 68%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_post_confirmacao_valida_sem_motivo PASSED                             [ 68%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_post_confirmacao_invalida_mostra_erro PASSED                          [ 69%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_post_confirmacao_vazia_mostra_erro PASSED                             [ 69%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_post_com_pendente_nao_cria_nova PASSED                                [ 69%]
apps/interessados/tests/test_views_exclusao.py::TestExclusaoSolicitadaView::test_sem_login_redirect_para_login PASSED                                 [ 69%]
apps/interessados/tests/test_views_exclusao.py::TestExclusaoSolicitadaView::test_get_com_login_retorna_200 PASSED                                     [ 69%]
apps/interessados/tests/tests.py::TestHashCPF::test_hash_gerado_corretamente PASSED                                                                   [ 69%]
apps/interessados/tests/tests.py::TestHashCPF::test_hash_tem_64_caracteres PASSED                                                                     [ 69%]
apps/interessados/tests/tests.py::TestHashCPF::test_hashes_diferentes_para_cpfs_diferentes PASSED                                                     [ 69%]
apps/interessados/tests/tests.py::TestInteressadoModel::test_check_password_correto PASSED                                                            [ 70%]
apps/interessados/tests/tests.py::TestInteressadoModel::test_check_password_incorreto PASSED                                                          [ 70%]
apps/interessados/tests/tests.py::TestInteressadoModel::test_is_anonymous_false PASSED                                                                [ 70%]
apps/interessados/tests/tests.py::TestInteressadoModel::test_is_authenticated PASSED                                                                  [ 70%]
apps/interessados/tests/tests.py::TestInteressadoModel::test_senha_criptografada PASSED                                                               [ 70%]
apps/interessados/tests/tests.py::TestInteressadoModel::test_str PASSED                                                                               [ 70%]
apps/interessados/tests/tests.py::TestValidacaoCPF::test_cpf_digito_verificador_errado PASSED                                                         [ 70%]
apps/interessados/tests/tests.py::TestValidacaoCPF::test_cpf_duplicado_rejeitado PASSED                                                               [ 70%]
apps/interessados/tests/tests.py::TestValidacaoCPF::test_cpf_formatado_aceito PASSED                                                                  [ 71%]
apps/interessados/tests/tests.py::TestValidacaoCPF::test_cpf_sem_formatacao_aceito PASSED                                                             [ 71%]
apps/interessados/tests/tests.py::TestValidacaoCPF::test_cpf_todos_digitos_iguais_rejeitado PASSED                                                    [ 71%]
apps/interessados/tests/tests.py::TestValidacaoCPF::test_cpf_valido_aceito PASSED                                                                     [ 71%]
apps/interessados/tests/tests.py::TestLoginForm::test_login_conta_inativa PASSED                                                                      [ 71%]
apps/interessados/tests/tests.py::TestLoginForm::test_login_correto PASSED                                                                            [ 71%]
apps/interessados/tests/tests.py::TestLoginForm::test_login_cpf_nao_cadastrado PASSED                                                                 [ 71%]
apps/interessados/tests/tests.py::TestLoginForm::test_login_senha_errada PASSED                                                                       [ 72%]
apps/interessados/tests/tests.py::TestViews::test_dashboard_com_login_acessivel PASSED                                                                [ 72%]
apps/interessados/tests/tests.py::TestViews::test_dashboard_sem_login_redireciona PASSED                                                              [ 72%]
apps/interessados/tests/tests.py::TestViews::test_meus_dados_sem_login_redireciona PASSED                                                             [ 72%]
apps/interessados/tests/tests.py::TestViews::test_pagina_cadastro_acessivel PASSED                                                                    [ 72%]
apps/interessados/tests/tests.py::TestViews::test_pagina_login_acessivel PASSED                                                                       [ 72%]
apps/interessados/tests/tests.py::TestViews::test_solicitar_exclusao_sem_login_redireciona PASSED                                                     [ 72%]
apps/interessados/tests/tests.py::TestSolicitacaoExclusao::test_segunda_solicitacao_bloqueada PASSED                                                  [ 72%]
apps/interessados/tests/tests.py::TestSolicitacaoExclusao::test_solicitacao_criada_com_confirmacao PASSED                                             [ 73%]
apps/interessados/tests/tests.py::TestSolicitacaoExclusao::test_solicitacao_nao_criada_sem_confirmacao PASSED                                         [ 73%]
apps/portal/tests/test_forms.py::TestLoginInteressadoForm::test_form_valido_com_cpf_e_senha_corretos PASSED                                           [ 73%]
apps/portal/tests/test_forms.py::TestLoginInteressadoForm::test_form_valido_com_cpf_formatado PASSED                                                  [ 73%]
apps/portal/tests/test_forms.py::TestLoginInteressadoForm::test_form_invalido_com_cpf_incorreto PASSED                                                [ 73%]
apps/portal/tests/test_forms.py::TestLoginInteressadoForm::test_form_invalido_com_senha_incorreta PASSED                                              [ 73%]
apps/portal/tests/test_forms.py::TestLoginInteressadoForm::test_form_invalido_interessado_inativo PASSED                                              [ 73%]
apps/portal/tests/test_forms.py::TestLoginInteressadoForm::test_form_invalido_cpf_com_menos_de_11_digitos PASSED                                      [ 73%]
apps/portal/tests/test_forms.py::TestLoginInteressadoForm::test_form_invalido_com_campos_vazios PASSED                                                [ 74%]
apps/portal/tests/test_forms.py::TestConsultaPublicaForm::test_cpf_valido_sem_formatacao PASSED                                                       [ 74%]
apps/portal/tests/test_forms.py::TestConsultaPublicaForm::test_cpf_valido_com_formatacao PASSED                                                       [ 74%]
apps/portal/tests/test_forms.py::TestConsultaPublicaForm::test_cpf_invalido_com_menos_de_11_digitos PASSED                                            [ 74%]
apps/portal/tests/test_forms.py::TestConsultaPublicaForm::test_cpf_invalido_vazio PASSED                                                              [ 74%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_index_url PASSED                                                                               [ 74%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_login_url PASSED                                                                               [ 74%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_logout_url PASSED                                                                              [ 74%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_dashboard_url PASSED                                                                           [ 75%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_consulta_publica_url PASSED                                                                    [ 75%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_resultado_evento_url PASSED                                                                    [ 75%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_detalhes_evento_url PASSED                                                                     [ 75%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_contato_url PASSED                                                                             [ 75%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_privacidade_url PASSED                                                                         [ 75%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_index_path PASSED                                                                                  [ 75%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_login_path PASSED                                                                                  [ 76%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_logout_path PASSED                                                                                 [ 76%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_dashboard_path PASSED                                                                              [ 76%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_consulta_publica_path PASSED                                                                       [ 76%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_resultado_evento_path PASSED                                                                       [ 76%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_detalhes_evento_path PASSED                                                                        [ 76%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_contato_path PASSED                                                                                [ 76%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_privacidade_path PASSED                                                                            [ 76%]
apps/portal/tests/test_views.py::TestIndexView::test_index_get_200 PASSED                                                                             [ 77%]
apps/portal/tests/test_views.py::TestIndexView::test_index_context_eventos PASSED                                                                     [ 77%]
apps/portal/tests/test_views.py::TestIndexView::test_index_total_eventos_int PASSED                                                                   [ 77%]
apps/portal/tests/test_views.py::TestLoginInteressadoView::test_login_post_valido_redirect_302 PASSED                                                 [ 77%]
apps/portal/tests/test_views.py::TestLoginInteressadoView::test_login_post_valido_cria_sessao_id PASSED                                               [ 77%]
apps/portal/tests/test_views.py::TestLoginInteressadoView::test_login_post_valido_sessao_nome PASSED                                                  [ 77%]
apps/portal/tests/test_views.py::TestLoginInteressadoView::test_login_post_valido_sessao_cpf_mascarado PASSED                                         [ 77%]
apps/portal/tests/test_views.py::TestLoginInteressadoView::test_login_com_sessao_redirect_302 PASSED                                                  [ 77%]
apps/portal/tests/test_views.py::TestLogoutInteressadoView::test_logout_limpa_sessao PASSED                                                           [ 78%]
apps/portal/tests/test_views.py::TestLogoutInteressadoView::test_logout_redirect_302 PASSED                                                           [ 78%]
apps/portal/tests/test_views.py::TestDashboardView::test_dashboard_sem_sessao_redirect_302 PASSED                                                     [ 78%]
apps/portal/tests/test_views.py::TestDashboardView::test_dashboard_sessao_invalida_redirect_302 PASSED                                                [ 78%]
apps/portal/tests/test_views.py::TestDashboardView::test_dashboard_sessao_valida_nao_302 PASSED                                                       [ 78%]
apps/portal/tests/test_views.py::TestDashboardView::test_dashboard_sessao_valida_status_ok PASSED                                                     [ 78%]
apps/portal/tests/test_views.py::TestConsultaPublicaView::test_consulta_get_200 PASSED                                                                [ 78%]
apps/portal/tests/test_views.py::TestConsultaPublicaView::test_consulta_post_cpf_valido_context PASSED                                                [ 78%]
apps/portal/tests/test_views.py::TestConsultaPublicaView::test_consulta_post_cpf_invalido_mensagem PASSED                                             [ 79%]
apps/portal/tests/test_views.py::TestConsultaPublicaView::test_consulta_post_vazio_form PASSED                                                        [ 79%]
apps/portal/tests/test_views.py::TestResultadoEventoView::test_resultado_get_status_valido PASSED                                                     [ 79%]
apps/portal/tests/test_views.py::TestResultadoEventoView::test_resultado_get_nao_erro_500 PASSED                                                      [ 79%]
apps/portal/tests/test_views.py::TestDetalhesEventoView::test_detalhes_sem_sessao_redirect PASSED                                                     [ 79%]
apps/portal/tests/test_views.py::TestDetalhesEventoView::test_detalhes_com_sessao_status_valido PASSED                                                [ 79%]
apps/portal/tests/test_views.py::TestContatoView::test_contato_get_200 PASSED                                                                         [ 79%]
apps/portal/tests/test_views.py::TestContatoView::test_contato_context PASSED                                                                         [ 80%]
apps/portal/tests/test_views.py::TestPoliticaPrivacidadeView::test_politica_get_200 PASSED                                                            [ 80%]
apps/portal/tests/test_views.py::TestPoliticaPrivacidadeView::test_politica_content_existe PASSED                                                     [ 80%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoEventoNaoEncontrado::test_evento_inexistente_exibe_erro PASSED [ 80%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoSemInscricoes::test_sem_inscricoes_confirmadas_exibe_aviso PASSED [ 80%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoSemInscricoes::test_sem_inscricoes_nao_cria_classificacao PASSED [ 80%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoSemCriterios::test_sem_criterios_exibe_aviso PASSED     [ 80%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_pcd_atribuido PASSED           [ 80%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_pcd_nao_atribuido_quando_sem_deficiencia PASSED [ 81%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_nis_atribuido PASSED           [ 81%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_nis_nao_atribuido_sem_nis PASSED [ 81%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_jovem_atribuido_16_anos PASSED [ 81%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_jovem_atribuido_24_anos PASSED [ 81%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_jovem_nao_atribuido_para_adulto PASSED [ 81%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_idoso_atribuido_50_anos PASSED [ 81%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_idoso_nao_atribuido_para_49_anos PASSED [ 81%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_cota_racial_preta PASSED       [ 82%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_cota_racial_parda PASSED       [ 82%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_cota_racial_indigena PASSED    [ 82%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_cota_racial_nao_atribuido_para_branca PASSED [ 82%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_cota_racial_sem_fototipo PASSED [ 82%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_escolaridade_fundamental_incompleto PASSED [ 82%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_escolaridade_medio_completo PASSED [ 82%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_multiplos_criterios_somam_pontos PASSED [ 82%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoCriterioOrdenacao::test_criterio_ordenacao_nao_soma_pontos PASSED [ 83%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPosicao::test_primeiro_colocado_esta_classificado PASSED [ 83%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPosicao::test_fora_das_vagas_esta_em_lista_espera PASSED [ 83%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPosicao::test_total_de_classificacoes_igual_ao_total_de_inscricoes PASSED [ 83%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPosicao::test_posicoes_sao_unicas PASSED                [ 83%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoDesempatePorIdade::test_desempate_jovem_prioriza_mais_novo PASSED [ 83%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoDesempatePorIdade::test_desempate_idoso_prioriza_mais_velho PASSED [ 83%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoIdempotencia::test_segunda_execucao_nao_duplica_classificacao PASSED [ 84%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoIdempotencia::test_segunda_execucao_nao_duplica_criterios_atendidos PASSED [ 84%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoStatusInscricao::test_inscricao_pendente_e_ignorada PASSED [ 84%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoStatusInscricao::test_inscricao_confirmada_e_processada PASSED [ 84%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisComando::test_comando_executa_sem_erro PASSED    [ 84%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisComando::test_comando_retorna_string PASSED      [ 84%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisComando::test_comando_nao_vazio PASSED           [ 84%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_planejamento PASSED   [ 84%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_inscricoes_abertas PASSED [ 85%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_inscricoes_encerradas PASSED [ 85%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_em_classificacao PASSED [ 85%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_resultado_divulgado PASSED [ 85%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_em_andamento PASSED   [ 85%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_finalizado PASSED     [ 85%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_cancelado PASSED      [ 85%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_total_status_eventos PASSED  [ 85%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_pendente PASSED    [ 86%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_classificado PASSED [ 86%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_confirmada PASSED  [ 86%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_lista_espera PASSED [ 86%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_cancelada PASSED   [ 86%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_expirada PASSED    [ 86%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_desistente PASSED  [ 86%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_nao_localizado PASSED [ 86%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_total_status_inscricoes PASSED [ 87%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusMatriculas::test_status_pendente PASSED    [ 87%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusMatriculas::test_status_ativa PASSED       [ 87%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusMatriculas::test_status_concluida PASSED   [ 87%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusMatriculas::test_status_trancada PASSED    [ 87%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusMatriculas::test_status_cancelada PASSED   [ 87%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusMatriculas::test_total_status_matriculas PASSED [ 87%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisCriterios::test_criterio_pcd PASSED              [ 88%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisCriterios::test_criterio_programa_social PASSED  [ 88%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisCriterios::test_criterio_jovem PASSED            [ 88%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisCriterios::test_criterio_idoso PASSED            [ 88%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisCriterios::test_criterio_ensino_fundamental PASSED [ 88%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisCriterios::test_criterio_renda_baixa PASSED      [ 88%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisCriterios::test_criterio_cota_racial PASSED      [ 88%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSexo::test_sexo_masculino PASSED                 [ 88%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSexo::test_sexo_feminino PASSED                  [ 89%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSexo::test_sexo_outro PASSED                     [ 89%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSexo::test_sexo_nao_informar PASSED              [ 89%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSexo::test_total_sexo PASSED                     [ 89%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisFototipes::test_fototipo_branca PASSED           [ 89%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisFototipes::test_fototipo_preta PASSED            [ 89%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisFototipes::test_fototipo_parda PASSED            [ 89%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisFototipes::test_fototipo_amarela PASSED          [ 89%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisFototipes::test_fototipo_indigena PASSED         [ 90%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisFototipes::test_total_fototipos PASSED           [ 90%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisIntegracao::test_todos_modelos_populados PASSED  [ 90%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisIntegracao::test_contagem_total_registros PASSED [ 90%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisIntegracao::test_integridade_dados PASSED        [ 90%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisIdempotencia::test_execucao_dupla_nao_duplica_dados PASSED [ 90%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisIdempotencia::test_execucao_tripla_nao_duplica_dados PASSED [ 90%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSaida::test_saida_contem_sucesso PASSED          [ 90%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSaida::test_saida_contem_nome_comando PASSED     [ 91%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSaida::test_saida_nao_contem_ansi PASSED         [ 91%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionCapacity::test_matricular_alunos_capacidade_ultrapassada PASSED                           [ 91%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionCapacity::test_matricular_alunos_capacidade_exata PASSED                                  [ 91%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionValidation::test_validacao_evento_unico PASSED                                            [ 91%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionValidation::test_validacao_turma_inexistente_para_evento PASSED                           [ 91%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionValidation::test_protecao_duplicidade_matricula PASSED                                    [ 91%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionValidation::test_validacao_turma_nao_pertence_ao_evento PASSED                            [ 92%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionSuccess::test_sucesso_matricula_dentro_capacidade PASSED                                  [ 92%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionSuccess::test_nenhuma_classificacao_selecionada PASSED                                    [ 92%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionErrorHandling::test_transacao_atomica_rollback_on_matricula_save_error PASSED             [ 92%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionErrorHandling::test_status_ativa_nao_encontrado PASSED                                    [ 92%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionErrorHandling::test_status_confirmada_nao_encontrado PASSED                               [ 92%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionErrorHandling::test_classificacoes_sem_evento_associado PASSED                            [ 92%]
apps/selecao/tests/test_models.py::TestStatusInscricaoModel::test_create_status_inscricao PASSED                                                      [ 92%]
apps/selecao/tests/test_models.py::TestStatusInscricaoModel::test_status_inscricao_str PASSED                                                         [ 93%]
apps/selecao/tests/test_models.py::TestStatusInscricaoModel::test_status_inscricao_unique_name PASSED                                                 [ 93%]
apps/selecao/tests/test_models.py::TestInscricaoModel::test_create_inscricao PASSED                                                                   [ 93%]
apps/selecao/tests/test_models.py::TestInscricaoModel::test_inscricao_str PASSED                                                                      [ 93%]
apps/selecao/tests/test_models.py::TestInscricaoModel::test_inscricao_unique_together PASSED                                                          [ 93%]
apps/selecao/tests/test_models.py::TestInscricaoModel::test_inscricao_relacionamentos PASSED                                                          [ 93%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_create_classificacao PASSED                                                           [ 93%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_classificacao_str PASSED                                                              [ 93%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_classificacao_posicao_null_default PASSED                                             [ 94%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_classificacao_unique_inscricao PASSED                                                 [ 94%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_pontuacao_total_validacao_range PASSED                                                [ 94%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_flags_classificacao_mutuamente_exclusivas PASSED                                      [ 94%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_desempate_por_data_inscricao PASSED                                                   [ 94%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_valido PASSED                                                    [ 94%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_none PASSED                                                      [ 94%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_vazio PASSED                                                     [ 94%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_ja_formatado PASSED                                              [ 95%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_menos_de_11 PASSED                                               [ 95%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_mascarado_valido PASSED                                          [ 95%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_mascarado_none PASSED                                            [ 95%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_mascarado_vazio PASSED                                           [ 95%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_telefone_celular PASSED                                              [ 95%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_telefone_fixo PASSED                                                 [ 95%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_telefone_none PASSED                                                 [ 96%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_telefone_vazio PASSED                                                [ 96%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_telefone_ja_formatado PASSED                                         [ 96%]
apps/selecao/tests/test_services.py::TestClassificadorServicePontuacao::test_calcular_pontuacao_inscricao_com_criterios PASSED                        [ 96%]
apps/selecao/tests/test_services.py::TestClassificadorServicePontuacao::test_calcular_pontuacao_inscricao_zero PASSED                                 [ 96%]
apps/selecao/tests/test_services.py::TestClassificadorServicePontuacao::test_calcular_pontuacao_multiplos_criterios PASSED                            [ 96%]
apps/selecao/tests/test_services.py::TestClassificadorServicePontuacao::test_classificar_sem_eventocriterio_vinculado PASSED                          [ 96%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_atribui_posicoes PASSED                           [ 96%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_classifica_dentro_vagas PASSED                    [ 97%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_lista_espera PASSED                               [ 97%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_atualiza_status_inscricao PASSED                  [ 97%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_com_criterios PASSED                              [ 97%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_zero_inscricoes PASSED                            [ 97%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_chamada_repetida PASSED                           [ 97%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_exatamente_1_vaga PASSED                          [ 97%]
apps/selecao/tests/test_services.py::TestClassificadorServiceDesempate::test_desempate_por_data_inscricao_igual_pontuacao PASSED                      [ 97%]
apps/selecao/tests/test_services.py::TestClassificadorServiceDesempate::test_desempate_com_lista_espera PASSED                                        [ 98%]
apps/selecao/tests/test_services.py::TestClassificadorServiceDesempate::test_desempate_misto_pontuacoes_diferentes_e_iguais PASSED                    [ 98%]
apps/selecao/tests/test_services.py::TestClassificadorServiceProcessamento::test_processar_inscricao_cria_classificacao PASSED                        [ 98%]
apps/selecao/tests/test_validators.py::TestValidarEvento::test_evento_sem_vagas_falha PASSED                                                          [ 98%]
apps/selecao/tests/test_validators.py::TestValidarEvento::test_evento_sem_inscricoes_falha PASSED                                                     [ 98%]
apps/selecao/tests/test_validators.py::TestValidarEvento::test_evento_datas_invalidas_falha PASSED                                                    [ 98%]
apps/selecao/tests/test_validators.py::TestValidarEvento::test_evento_sem_criterios_falha PASSED                                                      [ 98%]
apps/selecao/tests/test_validators.py::TestValidarEvento::test_evento_com_criterios_passa PASSED                                                      [ 98%]
apps/selecao/tests/test_validators.py::TestValidarInteressado::test_interessado_valido_passa PASSED                                                   [ 99%]
apps/selecao/tests/test_validators.py::TestValidarInteressado::test_interessado_sem_nome_falha PASSED                                                 [ 99%]
apps/selecao/tests/test_validators.py::TestValidarInteressado::test_interessado_data_nascimento_futura_falha PASSED                                   [ 99%]
apps/selecao/tests/test_validators.py::TestValidarInteressado::test_interessado_sem_sexo_gera_aviso PASSED                                            [ 99%]
apps/selecao/tests/test_validators.py::TestValidarInscricao::test_inscricao_valida_passa PASSED                                                       [ 99%]
apps/selecao/tests/test_validators.py::TestValidarInscricao::test_inscricao_sem_evento_falha PASSED                                                   [ 99%]
apps/selecao/tests/test_validators.py::TestValidarInscricao::test_inscricao_sem_interessado_falha PASSED                                              [ 99%]
apps/selecao/tests/test_validators.py::TestValidarInscricao::test_inscricao_com_data_futura_falha PASSED                                              [100%]

---------- coverage: platform win32, python 3.13.2-final-0 -----------
Name                                                                    Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------------------
apps\__init__.py                                                            0      0   100%
apps\academico\__init__.py                                                  0      0   100%
apps\academico\admin.py                                                   320    199    38%   245-264, 270-276, 284-440, 450-613, 641-642, 666-667, 678, 681
apps\academico\apps.py                                                      5      0   100%
apps\academico\certificado.py                                             136      3    98%   103-104, 193
apps\academico\models.py                                                  110     22    80%   45, 122, 133, 142, 168, 204-206, 300-316, 339-342
apps\academico\services.py                                                136     72    47%   65-106, 121-144, 165-232, 255-283
apps\academico\urls.py                                                      5      0   100%
apps\academico\views.py                                                    63      0   100%
apps\accounts\__init__.py                                                   0      0   100%
apps\accounts\admin.py                                                     52      0   100%
apps\accounts\apps.py                                                       5      0   100%
apps\accounts\forms.py                                                      5      5     0%   8-27
apps\accounts\middleware.py                                                20      0   100%
apps\accounts\models.py                                                    22      1    95%   105
apps\accounts\urls.py                                                       5      0   100%
apps\accounts\views.py                                                     47     20    57%   27, 83-114
apps\accounts\views_exclusao.py                                            77      2    97%   44-45
apps\dashboard\__init__.py                                                  0      0   100%
apps\dashboard\admin.py                                                     0      0   100%
apps\dashboard\apps.py                                                      4      0   100%
apps\dashboard\models.py                                                    1      0   100%
apps\dashboard\services.py                                                157      0   100%
apps\dashboard\utils_pdf.py                                               373     90    76%   86-87, 90-91, 94-99, 102-107, 227-231, 235-239, 243-247, 250-252, 259-263, 267-271, 275-279, 282-284, 288-293, 416-435, 439-459, 583-603, 726-746
apps\dashboard\views.py                                                    71      0   100%
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212     86    59%   67, 111-114, 181, 196, 223, 234, 245, 256, 269-358, 371-415, 430-519
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51      3    94%   39, 111-112
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122      7    94%   106, 137, 142, 147, 152, 201, 206
apps\eventos\views.py                                                       1      1     0%   1
apps\interessados\__init__.py                                               0      0   100%
apps\interessados\admin.py                                                218     20    91%   235-238, 251, 255, 367, 380, 413-421, 480-481, 509, 514
apps\interessados\apps.py                                                   5      0   100%
apps\interessados\authentication.py                                        25      1    96%   52
apps\interessados\forms.py                                                157      7    96%   227, 242, 395-396, 409, 447, 452
apps\interessados\management\__init__.py                                    0      0   100%
apps\interessados\management\commands\__init__.py                           0      0   100%
apps\interessados\management\commands\criptografar_cpfs.py                 22     22     0%   11-47
apps\interessados\management\commands\limpar_tokens.py                     59     59     0%   13-155
apps\interessados\management\commands\popular_cpf_hash.py                  22     22     0%   9-40
apps\interessados\models.py                                               139      9    94%   41, 138, 141, 144, 147, 162, 188, 191-192
apps\interessados\urls.py                                                   5      0   100%
apps\interessados\utils.py                                                 14      0   100%
apps\interessados\views.py                                                202    104    49%   60-61, 88-92, 113-115, 132-134, 197-199, 209-210, 232-250, 266-323, 396-401, 409-414, 422, 430-472, 477, 482, 496-519
apps\interessados\views_exclusao.py                                        29      3    90%   25-27
apps\portal\__init__.py                                                     1      0   100%
apps\portal\admin.py                                                        1      0   100%
apps\portal\apps.py                                                         5      0   100%
apps\portal\forms.py                                                       34      0   100%
apps\portal\models.py                                                       1      0   100%
apps\portal\urls.py                                                         4      0   100%
apps\portal\views.py                                                       99     11    89%   72-74, 174-189, 202-220
apps\scripts_admin\__init__.py                                              0      0   100%
apps\scripts_admin\management\__init__.py                                   0      0   100%
apps\scripts_admin\management\commands\__init__.py                          0      0   100%
apps\scripts_admin\management\commands\classificar_evento.py              134      9    93%   82, 100-101, 182-184, 188-190
apps\scripts_admin\management\commands\configurar_criterios_evento.py      57     57     0%   5-91
apps\scripts_admin\management\commands\popular_criterios.py                21     21     0%   4-117
apps\scripts_admin\management\commands\popular_dados_iniciais.py           66      0   100%
apps\selecao\__init__.py                                                    0      0   100%
apps\selecao\admin.py                                                     275     88    68%   71-72, 87, 110-115, 152, 223, 233, 240-241, 247, 254-255, 266-275, 306-307, 338-343, 445, 466-503, 507-544, 552, 558, 564, 570, 580, 586, 592, 598, 661, 667
apps\selecao\apps.py                                                        5      0   100%
apps\selecao\management\__init__.py                                         0      0   100%
apps\selecao\management\commands\__init__.py                                0      0   100%
apps\selecao\models.py                                                     71      1    99%   188
apps\selecao\reports.py                                                   301    252    16%   27-31, 35-115, 146, 163, 179-286, 302-420, 440-565, 580-711
apps\selecao\services.py                                                  125     26    79%   82-85, 89-92, 102, 106, 110, 114, 383-392, 414-432
apps\selecao\validators.py                                                105     35    67%   38-39, 47, 74, 101, 105, 116, 123, 126, 130, 149-175, 193-194, 199, 204, 213-215, 222-223
apps\selecao\views.py                                                       1      1     0%   1
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4208   1259    70%
Coverage HTML written to dir htmlcov




##  coverage 

(.venv) PS C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta> python -m pytest --cov=apps --cov-report=html
=========================================================================== test session starts ===========================================================================
platform win32 -- Python 3.13.2, pytest-7.4.3, pluggy-1.6.0 -- C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.4, settings: config.settings (from ini)
rootdir: C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta
configfile: pytest.ini
testpaths: apps
plugins: anyio-4.13.0, Faker-40.11.1, cov-4.1.0, django-4.7.0, mock-3.15.1
collected 831 items                                                                                                                                                        

apps/academico/tests/test_admin.py::TestStatusMatriculaAdmin::test_cor_display_com_cor PASSED                                                                        [  0%]
apps/academico/tests/test_admin.py::TestStatusMatriculaAdmin::test_cor_display_sem_cor PASSED                                                                        [  0%]
apps/academico/tests/test_admin.py::TestMatriculaAdmin::test_get_interessado PASSED                                                                                  [  0%]
apps/academico/tests/test_admin.py::TestMatriculaAdmin::test_get_evento PASSED                                                                                       [  0%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_acoes_certificado_aprovado PASSED                                                                       [  0%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_acoes_certificado_nao_aprovado PASSED                                                                   [  0%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_changelist_view_contexto PASSED                                                                         [  0%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_gerar_certificados_marca_emitidos PASSED                                                                [  0%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_gerar_certificados_sem_aprovados PASSED                                                                 [  1%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_gerar_certificados_ja_emitido PASSED                                                                    [  1%]
apps/academico/tests/test_admin.py::TestAvaliacaoAdmin::test_download_certificados_lote_action_redirect PASSED                                                       [  1%]
apps/academico/tests/test_certificado.py::TestAtributos::test_inicializacao_atributos PASSED                                                                         [  1%]
apps/academico/tests/test_certificado.py::TestAtributos::test_pagesize_a4_paisagem PASSED                                                                            [  1%]
apps/academico/tests/test_certificado.py::TestAtributos::test_static_path_construido PASSED                                                                          [  1%]
apps/academico/tests/test_certificado.py::TestFormatacao::test_cpf_formatado PASSED                                                                                  [  1%]
apps/academico/tests/test_certificado.py::TestTraducaoMes::test_traducao_mes[data0-15 de janeiro de 2026] PASSED                                                     [  1%]
apps/academico/tests/test_certificado.py::TestTraducaoMes::test_traducao_mes[data1-03 de agosto de 2026] PASSED                                                      [  2%]
apps/academico/tests/test_certificado.py::TestFallback::test_data_emissao_fallback_para_agora PASSED                                                                 [  2%]
apps/academico/tests/test_certificado.py::TestFallback::test_carga_horaria_fallback_40h PASSED                                                                       [  2%]
apps/academico/tests/test_certificado.py::TestGeracaoPDF::test_gerar_pdf_retorna_buffer_valido PASSED                                                                [  2%]
apps/academico/tests/test_certificado.py::TestGeracaoPDF::test_gerar_pdf_multiplas_chamadas PASSED                                                                   [  2%]
apps/academico/tests/test_models.py::TestStatusMatriculaModel::test_status_criado_corretamente PASSED                                                                [  2%]
apps/academico/tests/test_models.py::TestStatusMatriculaModel::test_status_nome_unique_no_banco PASSED                                                               [  2%]
apps/academico/tests/test_models.py::TestMatriculaModel::test_matricula_criada_corretamente PASSED                                                                   [  2%]
apps/academico/tests/test_models.py::TestMatriculaModel::test_matricula_unique_together_turma_interessado PASSED                                                     [  3%]
apps/academico/tests/test_services.py::TestVerificacaoDisponibilidade::test_verificar_disponibilidade_turma_com_vagas PASSED                                         [  3%]
apps/academico/tests/test_services.py::TestVerificacaoDisponibilidade::test_verificar_disponibilidade_turma_lotada PASSED                                            [  3%]
apps/academico/tests/test_services.py::TestVerificacaoDisponibilidade::test_verificar_disponibilidade_turma_parcial PASSED                                           [  3%]
apps/academico/tests/test_services.py::TestVerificacaoDisponibilidade::test_verificar_disponibilidade_turma_exatamente_cheia PASSED                                  [  3%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_aprovado PASSED                                                                        [  3%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_reprovado_por_nota PASSED                                                              [  3%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_reprovado_por_frequencia PASSED                                                        [  3%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_nota_invalida PASSED                                                                   [  3%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_frequencia_invalida PASSED                                                             [  4%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_nota_limite_minimo_aprovado PASSED                                                     [  4%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_nota_limite_maximo PASSED                                                              [  4%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_frequencia_limite_minimo PASSED                                                        [  4%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_frequencia_limite_maximo PASSED                                                        [  4%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_atualiza_status_matricula PASSED                                                       [  4%]
apps/academico/tests/test_services.py::TestAvaliacaoAluno::test_avaliar_aluno_cria_ou_atualiza PASSED                                                                [  4%]
apps/academico/tests/test_services.py::TestRelatorioTurma::test_gerar_relatorio_turma PASSED                                                                         [  4%]
apps/academico/tests/test_services.py::TestRelatorioTurma::test_gerar_relatorio_turma_vazia PASSED                                                                   [  5%]
apps/academico/tests/test_services.py::TestRelatorioTurma::test_gerar_relatorio_turma_parcialmente_avaliada PASSED                                                   [  5%]
apps/academico/tests/test_services.py::TestRelatorioTurma::test_gerar_relatorio_turma_valida_valores PASSED                                                          [  5%]
apps/academico/tests/test_views.py::TestDownloadCertificadoIndividual::test_sem_autenticacao_redireciona PASSED                                                      [  5%]
apps/academico/tests/test_views.py::TestDownloadCertificadoIndividual::test_aluno_aprovado_gera_pdf PASSED                                                           [  5%]
apps/academico/tests/test_views.py::TestDownloadCertificadoIndividual::test_aluno_reprovado_retorna_400 PASSED                                                       [  5%]
apps/academico/tests/test_views.py::TestDownloadCertificadoIndividual::test_avaliacao_inexistente_retorna_404 PASSED                                                 [  5%]
apps/academico/tests/test_views.py::TestPreviewCertificado::test_sem_autenticacao_redireciona PASSED                                                                 [  5%]
apps/academico/tests/test_views.py::TestPreviewCertificado::test_aluno_aprovado_inline PASSED                                                                        [  6%]
apps/academico/tests/test_views.py::TestPreviewCertificado::test_aluno_reprovado_retorna_400 PASSED                                                                  [  6%]
apps/academico/tests/test_views.py::TestDownloadCertificadosLote::test_sem_ids_retorna_400 PASSED                                                                    [  6%]
apps/academico/tests/test_views.py::TestDownloadCertificadosLote::test_ids_invalidos_retorna_400 PASSED                                                              [  6%]
apps/academico/tests/test_views.py::TestDownloadCertificadosLote::test_apenas_aprovados_no_zip PASSED                                                                [  6%]
apps/academico/tests/test_views.py::TestDownloadCertificadosLote::test_zip_com_multiplos_certificados PASSED                                                         [  6%]
apps/accounts/tests/test_admin.py::TestCustomAdminSite::test_admin_index_status_200 PASSED                                                                           [  6%]
apps/accounts/tests/test_admin.py::TestCustomAdminSite::test_admin_index_sem_login_redirect PASSED                                                                   [  6%]
apps/accounts/tests/test_admin.py::TestCustomAdminSite::test_dashboard_status_200 PASSED                                                                             [  6%]
apps/accounts/tests/test_admin.py::TestCustomAdminSite::test_dashboard_sem_login_redirect PASSED                                                                     [  7%]
apps/accounts/tests/test_admin.py::TestUsuarioAdminList::test_usuario_admin_list_status_200 PASSED                                                                   [  7%]
apps/accounts/tests/test_admin.py::TestUsuarioAdminList::test_usuario_admin_list_sem_login_redirect PASSED                                                           [  7%]
apps/accounts/tests/test_admin.py::TestUsuarioAdminList::test_usuario_admin_list_pesquisa_por_username PASSED                                                        [  7%]
apps/accounts/tests/test_admin.py::TestUsuarioAdminAdd::test_usuario_admin_add_status_200 PASSED                                                                     [  7%]
apps/accounts/tests/test_admin.py::TestUsuarioAdminAdd::test_usuario_admin_add_usuario PASSED                                                                        [  7%]
apps/accounts/tests/test_admin.py::TestUsuarioAdminActionGerarSenhaProvisoria::test_gerar_senha_provisoria_seleciona_1 PASSED                                        [  7%]
apps/accounts/tests/test_admin.py::TestUsuarioAdminActionGerarSenhaProvisoria::test_gerar_senha_provisoria_seleciona_2_falha PASSED                                  [  7%]
apps/accounts/tests/test_forms.py::TestLoginStaffForm::test_form_tem_campos_esperados PASSED                                                                         [  8%]
apps/accounts/tests/test_forms.py::TestLoginStaffForm::test_form_placeholder_username PASSED                                                                         [  8%]
apps/accounts/tests/test_forms.py::TestLoginStaffForm::test_form_placeholder_password PASSED                                                                         [  8%]
apps/accounts/tests/test_forms.py::TestLoginStaffForm::test_form_com_dados_validos PASSED                                                                            [  8%]
apps/accounts/tests/test_forms.py::TestLoginStaffForm::test_form_com_dados_invalidos PASSED                                                                          [  8%]
apps/accounts/tests/test_forms.py::TestLoginStaffForm::test_form_renderiza_html PASSED                                                                               [  8%]
apps/accounts/tests/test_middleware.py::test_usuario_nao_autenticado_passa PASSED                                                                                    [  8%]
apps/accounts/tests/test_middleware.py::test_usuario_sem_must_change_password_passa PASSED                                                                           [  8%]
apps/accounts/tests/test_middleware.py::test_usuario_com_must_change_password_url_liberada_staff PASSED                                                              [  9%]
apps/accounts/tests/test_middleware.py::test_usuario_com_must_change_password_url_restrita_staff PASSED                                                              [  9%]
apps/accounts/tests/test_middleware.py::test_interessado_com_must_change_password_url_restrita PASSED                                                                [  9%]
apps/accounts/tests/test_middleware.py::test_static_url_liberada_mesmo_com_must_change_password PASSED                                                               [  9%]
apps/accounts/tests/test_middleware.py::test_media_url_liberada_mesmo_com_must_change_password PASSED                                                                [  9%]
apps/accounts/tests/test_middleware.py::test_url_admin_login_liberada PASSED                                                                                         [  9%]
apps/accounts/tests/test_middleware.py::test_url_admin_logout_liberada PASSED                                                                                        [  9%]
apps/accounts/tests/test_models.py::test_criar_usuario_com_cpf_valido PASSED                                                                                         [  9%]
apps/accounts/tests/test_models.py::test_criar_usuario_com_cpf_invalido[1234567890] PASSED                                                                           [  9%]
apps/accounts/tests/test_models.py::test_criar_usuario_com_cpf_invalido[123456789012] PASSED                                                                         [ 10%]
apps/accounts/tests/test_models.py::test_cpf_unico PASSED                                                                                                            [ 10%]
apps/accounts/tests/test_models.py::test_usuario_staff_pode_login PASSED                                                                                             [ 10%]
apps/accounts/tests/test_models.py::test_usuario_nao_staff_nao_pode_login_staff PASSED                                                                               [ 10%]
apps/accounts/tests/test_models.py::test_criar_usuario_sem_username_falha PASSED                                                                                     [ 10%]
apps/accounts/tests/test_models.py::test_criar_usuario_sem_password_falha PASSED                                                                                     [ 10%]
apps/accounts/tests/test_models.py::test_criar_superuser_is_staff PASSED                                                                                             [ 10%]
apps/accounts/tests/test_models.py::test_criar_superuser_is_superuser PASSED                                                                                         [ 10%]
apps/accounts/tests/test_models.py::test_usuario_str_retorna_username PASSED                                                                                         [ 11%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_login_staff_form_tem_csrf PASSED                                                                          [ 11%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_login_staff_get PASSED                                                                                    [ 11%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_login_staff_inativo_falha PASSED                                                                          [ 11%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_login_staff_invalido PASSED                                                                               [ 11%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_login_staff_nao_staff PASSED                                                                              [ 11%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_login_staff_valido PASSED                                                                                 [ 11%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_logout_staff PASSED                                                                                       [ 11%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_logout_staff_get_desloga PASSED                                                                           [ 12%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_nao_staff_redirecionado_ao_acessar_pagina_staff PASSED                                                    [ 12%]
apps/accounts/tests/test_views.py::AccountsViewsTest::test_staff_acessa_pagina_restrita_apos_login PASSED                                                            [ 12%]
apps/accounts/tests/test_views_exclusao.py::TestListarSolicitacoesView::test_listar_solicitacoes_status_200 PASSED                                                   [ 12%]
apps/accounts/tests/test_views_exclusao.py::TestListarSolicitacoesView::test_listar_solicitacoes_sem_login_redirect PASSED                                           [ 12%]
apps/accounts/tests/test_views_exclusao.py::TestListarSolicitacoesView::test_listar_solicitacoes_nao_staff_redirect PASSED                                           [ 12%]
apps/accounts/tests/test_views_exclusao.py::TestListarSolicitacoesView::test_listar_solicitacoes_contexto_tem_pendentes PASSED                                       [ 12%]
apps/accounts/tests/test_views_exclusao.py::TestListarSolicitacoesView::test_listar_solicitacoes_contexto_tem_aprovadas PASSED                                       [ 12%]
apps/accounts/tests/test_views_exclusao.py::TestListarSolicitacoesView::test_listar_solicitacoes_contexto_tem_recusadas PASSED                                       [ 12%]
apps/accounts/tests/test_views_exclusao.py::TestDetalheSolicitacaoView::test_detalhe_solicitacao_status_200 PASSED                                                   [ 13%]
apps/accounts/tests/test_views_exclusao.py::TestDetalheSolicitacaoView::test_detalhe_solicitacao_sem_login_redirect PASSED                                           [ 13%]
apps/accounts/tests/test_views_exclusao.py::TestDetalheSolicitacaoView::test_detalhe_solicitacao_404 PASSED                                                          [ 13%]
apps/accounts/tests/test_views_exclusao.py::TestDetalheSolicitacaoView::test_detalhe_solicitacao_aprovar PASSED                                                      [ 13%]
apps/accounts/tests/test_views_exclusao.py::TestDetalheSolicitacaoView::test_detalhe_solicitacao_recusar PASSED                                                      [ 13%]
apps/accounts/tests/test_views_exclusao.py::TestDetalheSolicitacaoView::test_detalhe_solicitacao_acao_invalida PASSED                                                [ 13%]
apps/accounts/tests/test_views_exclusao.py::TestDetalheSolicitacaoView::test_detalhe_solicitacao_sem_parecer PASSED                                                  [ 13%]
apps/accounts/tests/test_views_exclusao.py::TestAnonimizarInteressado::test_anonimizar_interessado_limpa_campos PASSED                                               [ 13%]
apps/accounts/tests/test_views_exclusao.py::TestAnonimizarInteressado::test_anonimizar_interessado_mantem_registro PASSED                                            [ 14%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_metricas_gerais PASSED                                                        [ 14%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_distribuicao_sexo PASSED                                                      [ 14%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_distribuicao_fototipo PASSED                                                  [ 14%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_distribuicao_escolaridade PASSED                                              [ 14%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_distribuicao_programas_sociais PASSED                                         [ 14%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_distribuicao_deficiencias PASSED                                              [ 14%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_tipos_deficiencia PASSED                                                      [ 14%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_calcular_faixas_etarias PASSED                                                         [ 15%]
apps/dashboard/tests/test_services.py::TestDashboardInteressadosService::test_obter_contexto_completo PASSED                                                         [ 15%]
apps/dashboard/tests/test_services.py::TestDashboardEventosService::test_calcular_metricas_gerais PASSED                                                             [ 15%]
apps/dashboard/tests/test_services.py::TestDashboardEventosService::test_calcular_turmas_por_status PASSED                                                           [ 15%]
apps/dashboard/tests/test_services.py::TestDashboardEventosService::test_calcular_eventos_por_status PASSED                                                          [ 15%]
apps/dashboard/tests/test_services.py::TestDashboardEventosService::test_calcular_top_eventos_inscricoes PASSED                                                      [ 15%]
apps/dashboard/tests/test_services.py::TestDashboardEventosService::test_obter_contexto_completo PASSED                                                              [ 15%]
apps/dashboard/tests/test_services.py::TestDashboardAcademicoService::test_calcular_metricas_avaliacoes PASSED                                                       [ 15%]
apps/dashboard/tests/test_services.py::TestDashboardAcademicoService::test_calcular_taxa_aprovacao PASSED                                                            [ 16%]
apps/dashboard/tests/test_services.py::TestDashboardAcademicoService::test_calcular_top_cursos_aprovados PASSED                                                      [ 16%]
apps/dashboard/tests/test_services.py::TestDashboardAcademicoService::test_obter_contexto_completo PASSED                                                            [ 16%]
apps/dashboard/tests/test_services.py::TestDashboardProcessoSeletivoService::test_calcular_metricas_inscricoes PASSED                                                [ 16%]
apps/dashboard/tests/test_services.py::TestDashboardProcessoSeletivoService::test_calcular_metricas_classificacoes PASSED                                            [ 16%]
apps/dashboard/tests/test_services.py::TestDashboardProcessoSeletivoService::test_calcular_top_eventos_inscricoes PASSED                                             [ 16%]
apps/dashboard/tests/test_services.py::TestDashboardProcessoSeletivoService::test_obter_contexto_completo PASSED                                                     [ 16%]
apps/dashboard/tests/test_utils_pdf.py::TestCriarGraficoPizza::test_dados_validos_retorna_buffer PASSED                                                              [ 16%]
apps/dashboard/tests/test_utils_pdf.py::TestCriarGraficoPizza::test_todos_valores_zero_retorna_none PASSED                                                           [ 16%]
apps/dashboard/tests/test_utils_pdf.py::TestCriarGraficoPizza::test_lista_vazia_retorna_none PASSED                                                                  [ 17%]
apps/dashboard/tests/test_utils_pdf.py::TestCriarGraficoPizza::test_um_item_valido_retorna_buffer PASSED                                                             [ 17%]
apps/dashboard/tests/test_utils_pdf.py::TestCriarGraficoBarras::test_dados_validos_retorna_buffer PASSED                                                             [ 17%]
apps/dashboard/tests/test_utils_pdf.py::TestGerarPdfInteressados::test_context_minimo_retorna_buffer PASSED                                                          [ 17%]
apps/dashboard/tests/test_utils_pdf.py::TestGerarPdfEventos::test_context_minimo_retorna_buffer PASSED                                                               [ 17%]
apps/dashboard/tests/test_utils_pdf.py::TestGerarPdfAcademico::test_context_minimo_retorna_buffer PASSED                                                             [ 17%]
apps/dashboard/tests/test_utils_pdf.py::TestGerarPdfProcessoSeletivo::test_context_minimo_retorna_buffer PASSED                                                      [ 17%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_academico_non_staff_redireciona PASSED                                                        [ 17%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_academico_sem_auth_redireciona PASSED                                                         [ 18%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_academico_sem_dados_nao_quebra PASSED                                                         [ 18%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_academico_staff_200 PASSED                                                                    [ 18%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_eventos_sem_auth_redireciona PASSED                                                           [ 18%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_eventos_staff_200 PASSED                                                                      [ 18%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_interessados_sem_auth_redireciona PASSED                                                      [ 18%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_interessados_staff_200 PASSED                                                                 [ 18%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_interessados_total_zero_nao_quebra PASSED                                                     [ 18%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_lgpd_sem_auth_redireciona PASSED                                                              [ 19%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_lgpd_staff_200 PASSED                                                                         [ 19%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_processo_seletivo_sem_auth_redireciona PASSED                                                 [ 19%]
apps/dashboard/tests/test_views.py::TestDashboardViews::test_dashboard_processo_seletivo_staff_200 PASSED                                                            [ 19%]
apps/dashboard/tests/test_views.py::TestDashboardPdfViews::test_pdf_academico_sem_auth_redireciona PASSED                                                            [ 19%]
apps/dashboard/tests/test_views.py::TestDashboardPdfViews::test_pdf_academico_staff_200 PASSED                                                                       [ 19%]
apps/dashboard/tests/test_views.py::TestDashboardPdfViews::test_pdf_eventos_sem_auth_redireciona PASSED                                                              [ 19%]
apps/dashboard/tests/test_views.py::TestDashboardPdfViews::test_pdf_eventos_staff_200 PASSED                                                                         [ 19%]
apps/dashboard/tests/test_views.py::TestDashboardPdfViews::test_pdf_interessados_sem_auth_redireciona PASSED                                                         [ 19%]
apps/dashboard/tests/test_views.py::TestDashboardPdfViews::test_pdf_interessados_sem_dados_nao_quebra PASSED                                                         [ 20%]
apps/dashboard/tests/test_views.py::TestDashboardPdfViews::test_pdf_interessados_staff_200 PASSED                                                                    [ 20%]
apps/dashboard/tests/test_views.py::TestDashboardPdfViews::test_pdf_processo_seletivo_sem_auth_redireciona PASSED                                                    [ 20%]
apps/dashboard/tests/test_views.py::TestDashboardPdfViews::test_pdf_processo_seletivo_staff_200 PASSED                                                               [ 20%]
apps/eventos/tests/test_admin.py::TestEventoAdminConfig::test_list_display PASSED                                                                                    [ 20%]
apps/eventos/tests/test_admin.py::TestEventoAdminConfig::test_list_filter PASSED                                                                                     [ 20%]
apps/eventos/tests/test_admin.py::TestEventoAdminConfig::test_search_fields PASSED                                                                                   [ 20%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_changelist_carrega PASSED                                                                          [ 20%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_busca_por_nome PASSED                                                                              [ 21%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_filtrar_por_status PASSED                                                                          [ 21%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_paginacao PASSED                                                                                   [ 21%]
apps/eventos/tests/test_admin.py::TestEventoAdminChangeList::test_busca_vazia PASSED                                                                                 [ 21%]
apps/eventos/tests/test_admin.py::TestStatusAdminChangeList::test_changelist_carrega PASSED                                                                          [ 21%]
apps/eventos/tests/test_admin.py::TestStatusAdminChangeList::test_busca_por_nome PASSED                                                                              [ 21%]
apps/eventos/tests/test_admin.py::TestTurmaAdminChangeList::test_changelist_carrega PASSED                                                                           [ 21%]
apps/eventos/tests/test_admin.py::TestTurmaAdminChangeList::test_busca_por_nome PASSED                                                                               [ 21%]
apps/eventos/tests/test_admin.py::TestEventoAdminViews::test_add_view PASSED                                                                                         [ 22%]
apps/eventos/tests/test_admin.py::TestEventoAdminViews::test_change_view PASSED                                                                                      [ 22%]
apps/eventos/tests/test_admin.py::TestEventoAdminViews::test_delete_view PASSED                                                                                      [ 22%]
apps/eventos/tests/test_admin.py::TestStatusAdminViews::test_add_view PASSED                                                                                         [ 22%]
apps/eventos/tests/test_admin.py::TestStatusAdminViews::test_change_view PASSED                                                                                      [ 22%]
apps/eventos/tests/test_admin.py::TestStatusAdminViews::test_delete_view PASSED                                                                                      [ 22%]
apps/eventos/tests/test_admin.py::TestTurmaAdminViews::test_add_view PASSED                                                                                          [ 22%]
apps/eventos/tests/test_admin.py::TestTurmaAdminViews::test_change_view PASSED                                                                                       [ 22%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_status_colorido PASSED                                                                                [ 22%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_vagas_inscritos_sem_inscricoes PASSED                                                                 [ 23%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_vagas_inscritos_com_inscricoes PASSED                                                                 [ 23%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_data_inicio_inscricao_formatada PASSED                                                                [ 23%]
apps/eventos/tests/test_admin.py::TestEventoAdminMethods::test_data_fim_inscricao_formatada PASSED                                                                   [ 23%]
apps/eventos/tests/test_admin.py::TestEventoAdminInlines::test_exibe_inline_criterios PASSED                                                                         [ 23%]
apps/eventos/tests/test_admin.py::TestEventoAdminInlines::test_exibe_inline_turmas PASSED                                                                            [ 23%]
apps/eventos/tests/test_admin.py::TestEventoAdminInlines::test_change_view_carrega_com_inlines PASSED                                                                [ 23%]
apps/eventos/tests/test_admin.py::TestHorarioAdminChangeList::test_changelist_carrega PASSED                                                                         [ 23%]
apps/eventos/tests/test_admin.py::TestHorarioAdminChangeList::test_filtro_dia_semana PASSED                                                                          [ 24%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_classificar_inscricoes_action_existe PASSED                                                         [ 24%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_cor_visual_retorna_html_com_cor PASSED                                                              [ 24%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_data_fim_evento_formatada PASSED                                                                    [ 24%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_data_fim_inscricao_formatada PASSED                                                                 [ 24%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_data_inicio_evento_formatada PASSED                                                                 [ 24%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_data_inicio_inscricao_formatada PASSED                                                              [ 24%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_desfazer_classificacao_action_existe PASSED                                                         [ 24%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_exportar_classificacao_excel_action_existe PASSED                                                   [ 25%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_status_admin_list_display PASSED                                                                    [ 25%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_vagas_inscritos_cor_laranja PASSED                                                                  [ 25%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_vagas_inscritos_cor_verde PASSED                                                                    [ 25%]
apps/eventos/tests/test_admin_actions.py::TestAdminActions::test_vagas_inscritos_cor_vermelho PASSED                                                                 [ 25%]
apps/eventos/tests/test_admin_config.py::TestCriterioAdminConfig::test_list_display PASSED                                                                           [ 25%]
apps/eventos/tests/test_admin_config.py::TestCriterioAdminConfig::test_list_filter PASSED                                                                            [ 25%]
apps/eventos/tests/test_admin_config.py::TestCriterioAdminConfig::test_search_fields PASSED                                                                          [ 25%]
apps/eventos/tests/test_admin_config.py::TestCriterioAdminConfig::test_list_editable PASSED                                                                          [ 25%]
apps/eventos/tests/test_admin_config.py::TestCriterioAdminConfig::test_readonly_fields PASSED                                                                        [ 26%]
apps/eventos/tests/test_admin_config.py::TestCriterioAdminConfig::test_fieldsets PASSED                                                                              [ 26%]
apps/eventos/tests/test_admin_config.py::TestCriterioAdminConfig::test_has_delete_permission_retorna_false PASSED                                                    [ 26%]
apps/eventos/tests/test_admin_config.py::TestTurmaAdminConfig::test_list_display PASSED                                                                              [ 26%]
apps/eventos/tests/test_admin_config.py::TestTurmaAdminConfig::test_list_filter PASSED                                                                               [ 26%]
apps/eventos/tests/test_admin_config.py::TestTurmaAdminConfig::test_search_fields PASSED                                                                             [ 26%]
apps/eventos/tests/test_admin_config.py::TestHorarioAdminConfig::test_list_display PASSED                                                                            [ 26%]
apps/eventos/tests/test_admin_config.py::TestHorarioAdminConfig::test_list_filter PASSED                                                                             [ 26%]
apps/eventos/tests/test_admin_config.py::TestHorarioAdminMethods::test_dia_semana_display PASSED                                                                     [ 27%]
apps/eventos/tests/test_admin_config.py::TestStatusAdminConfig::test_list_editable PASSED                                                                            [ 27%]
apps/eventos/tests/test_admin_config.py::TestStatusAdminConfig::test_ordering PASSED                                                                                 [ 27%]
apps/eventos/tests/test_admin_config.py::TestStatusAdminConfig::test_fieldsets PASSED                                                                                [ 27%]
apps/eventos/tests/test_admin_config.py::TestEventoAdminConfigExtra::test_fieldsets PASSED                                                                           [ 27%]
apps/eventos/tests/test_admin_config.py::TestEventoAdminConfigExtra::test_actions_list PASSED                                                                        [ 27%]
apps/eventos/tests/test_admin_config.py::TestStatusForm::test_widget_color PASSED                                                                                    [ 27%]
apps/eventos/tests/test_admin_config.py::TestEventoCriterioInlineMethods::test_pontos_display_com_pontos PASSED                                                      [ 27%]
apps/eventos/tests/test_admin_config.py::TestEventoCriterioInlineMethods::test_pontos_display_ordenacao PASSED                                                       [ 28%]
apps/eventos/tests/test_admin_config.py::TestEventoCriterioInlineMethods::test_get_queryset_usar_select_related PASSED                                               [ 28%]
apps/eventos/tests/test_admin_config.py::TestEventoCriterioInlineMethods::test_formfield_for_foreignkey_filtra_ativos PASSED                                         [ 28%]
apps/eventos/tests/test_admin_config.py::TestEdgeCases::test_status_colorido_sem_status PASSED                                                                       [ 28%]
apps/eventos/tests/test_admin_config.py::TestEdgeCases::test_data_inicio_inscricao_sem_data PASSED                                                                   [ 28%]
apps/eventos/tests/test_admin_config.py::TestEdgeCases::test_data_fim_inscricao_sem_data PASSED                                                                      [ 28%]
apps/eventos/tests/test_admin_config.py::TestEdgeCases::test_data_inicio_evento_sem_data PASSED                                                                      [ 28%]
apps/eventos/tests/test_admin_config.py::TestEdgeCases::test_data_fim_evento_sem_data PASSED                                                                         [ 28%]
apps/eventos/tests/test_admin_config.py::TestEdgeCases::test_vagas_inscritos_zero_vagas PASSED                                                                       [ 29%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_usuario_anonimo_retorna_lista_vazia PASSED                                              [ 29%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_usuario_nao_staff_retorna_lista_vazia PASSED                                            [ 29%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_sem_eventos_retorna_lista_vazia PASSED                                                  [ 29%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao1_status_correto_sem_alerta PASSED                                           [ 29%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao1_status_errado_gera_alerta PASSED                                           [ 29%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao2_status_valido_sem_alerta PASSED                                            [ 29%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao2_status_invalido_gera_alerta PASSED                                         [ 29%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao3_status_correto_sem_alerta PASSED                                           [ 29%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao3_status_errado_gera_alerta PASSED                                           [ 30%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao4_status_valido_sem_alerta PASSED                                            [ 30%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao4_status_invalido_gera_alerta PASSED                                         [ 30%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_verificacao4_cancelado_sem_alerta PASSED                                                [ 30%]
apps/eventos/tests/test_context_processors.py::TestNotificacoesEventos::test_multiplos_eventos_com_alerta PASSED                                                     [ 30%]
apps/eventos/tests/test_models.py::TestStatusModel::test_create_status PASSED                                                                                        [ 30%]
apps/eventos/tests/test_models.py::TestStatusModel::test_status_str PASSED                                                                                           [ 30%]
apps/eventos/tests/test_models.py::TestStatusModel::test_status_ordem_unique PASSED                                                                                  [ 30%]
apps/eventos/tests/test_models.py::TestStatusModel::test_status_cor_valid_hex PASSED                                                                                 [ 31%]
apps/eventos/tests/test_models.py::TestEventoModel::test_create_evento PASSED                                                                                        [ 31%]
apps/eventos/tests/test_models.py::TestEventoModel::test_evento_str PASSED                                                                                           [ 31%]
apps/eventos/tests/test_models.py::TestEventoModel::test_evento_foreign_key_status PASSED                                                                            [ 31%]
apps/eventos/tests/test_models.py::TestEventoModel::test_evento_total_vagas_positive PASSED                                                                          [ 31%]
apps/eventos/tests/test_models.py::TestEventoModel::test_evento_data_inicio_inscricao_before_fim PASSED                                                              [ 31%]
apps/eventos/tests/test_models.py::TestEventoModel::test_evento_data_inicio_evento_before_fim PASSED                                                                 [ 31%]
apps/eventos/tests/test_models.py::TestEventoModel::test_evento_datas_evento_validas PASSED                                                                          [ 31%]
apps/eventos/tests/test_models.py::TestCriterioModel::test_create_criterio PASSED                                                                                    [ 32%]
apps/eventos/tests/test_models.py::TestCriterioModel::test_criterio_str PASSED                                                                                       [ 32%]
apps/eventos/tests/test_models.py::TestCriterioModel::test_criterio_codigo_unique PASSED                                                                             [ 32%]
apps/eventos/tests/test_models.py::TestCriterioModel::test_criterio_pontos_non_negative PASSED                                                                       [ 32%]
apps/eventos/tests/test_models.py::TestCriterioModel::test_criterio_categoria_choices PASSED                                                                         [ 32%]
apps/eventos/tests/test_models.py::TestTurmaModel::test_create_turma PASSED                                                                                          [ 32%]
apps/eventos/tests/test_models.py::TestTurmaModel::test_turma_str PASSED                                                                                             [ 32%]
apps/eventos/tests/test_models.py::TestTurmaModel::test_turma_foreign_key_evento PASSED                                                                              [ 32%]
apps/eventos/tests/test_models.py::TestTurmaModel::test_turma_capacidade_positive PASSED                                                                             [ 32%]
apps/eventos/tests/test_models.py::TestHorarioModel::test_create_horario PASSED                                                                                      [ 33%]
apps/eventos/tests/test_models.py::TestHorarioModel::test_horario_foreign_key_turma PASSED                                                                           [ 33%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_criar_criterio_valido PASSED                                                                     [ 33%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_ler_criterio PASSED                                                                              [ 33%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_atualizar_criterio PASSED                                                                        [ 33%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_deletar_criterio PASSED                                                                          [ 33%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_codigo_unico PASSED                                                                              [ 33%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_codigo_valido PASSED                                                                             [ 33%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_pontos_positivo PASSED                                                                           [ 34%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_pontos_zero_permitido PASSED                                                                     [ 34%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_criterio_ativo_padrao PASSED                                                                     [ 34%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_criterio_inativo PASSED                                                                          [ 34%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_criterio_com_eventos PASSED                                                                      [ 34%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_criterio_sem_eventos PASSED                                                                      [ 34%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_str_representation PASSED                                                                        [ 34%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_filtro_por_ativo PASSED                                                                          [ 34%]
apps/eventos/tests/test_models_criterio.py::TestCriterioModel::test_queryset_count PASSED                                                                            [ 35%]
apps/eventos/tests/test_models_evento.py::TestEventoCRUD::test_criar_evento_valido PASSED                                                                            [ 35%]
apps/eventos/tests/test_models_evento.py::TestEventoCRUD::test_ler_evento PASSED                                                                                     [ 35%]
apps/eventos/tests/test_models_evento.py::TestEventoCRUD::test_atualizar_evento PASSED                                                                               [ 35%]
apps/eventos/tests/test_models_evento.py::TestEventoCRUD::test_deletar_evento PASSED                                                                                 [ 35%]
apps/eventos/tests/test_models_evento.py::TestEventoCRUD::test_multiplos_eventos PASSED                                                                              [ 35%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_data_inicio_inscricao_antes_fim_inscricao PASSED                                                [ 35%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_data_fim_inscricao_antes_inicio_evento PASSED                                                   [ 35%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_data_inicio_evento_antes_fim_evento PASSED                                                      [ 35%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_datas_validas_factory PASSED                                                                    [ 36%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_clean_valida_datas PASSED                                                                       [ 36%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_total_vagas_positivo PASSED                                                                     [ 36%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_total_vagas_grande_numero PASSED                                                                [ 36%]
apps/eventos/tests/test_models_evento.py::TestEventoValidacoes::test_total_vagas_zero_permitido PASSED                                                               [ 36%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_com_status PASSED                                                                            [ 36%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_sem_status_invalido PASSED                                                                   [ 36%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_com_turmas PASSED                                                                            [ 36%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_multiplas_turmas PASSED                                                                      [ 37%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_com_criterios PASSED                                                                         [ 37%]
apps/eventos/tests/test_models_evento.py::TestEventoStatus::test_evento_multiplos_criterios PASSED                                                                   [ 37%]
apps/eventos/tests/test_models_evento.py::TestEventoTimestamps::test_evento_sem_criterios PASSED                                                                     [ 37%]
apps/eventos/tests/test_models_evento.py::TestEventoTimestamps::test_deletar_evento_deleta_turmas PASSED                                                             [ 37%]
apps/eventos/tests/test_models_evento.py::TestEventoTimestamps::test_criado_em_existe PASSED                                                                         [ 37%]
apps/eventos/tests/test_models_evento.py::TestEventoTimestamps::test_atualizado_em_existe PASSED                                                                     [ 37%]
apps/eventos/tests/test_models_evento.py::TestEventoTimestamps::test_atualizado_em_atualiza PASSED                                                                   [ 37%]
apps/eventos/tests/test_models_evento.py::TestEventoMetodos::test_inscricoes_abertas PASSED                                                                          [ 38%]
apps/eventos/tests/test_models_evento.py::TestEventoMetodos::test_inscricoes_fechadas PASSED                                                                         [ 38%]
apps/eventos/tests/test_models_evento.py::TestEventoMetodos::test_validacao_datas_inscricao PASSED                                                                   [ 38%]
apps/eventos/tests/test_models_evento.py::TestEventoMetodos::test_validacao_datas_evento PASSED                                                                      [ 38%]
apps/eventos/tests/test_models_evento.py::TestEventoMetodos::test_formatacao_datas PASSED                                                                            [ 38%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_filtro_por_status PASSED                                                                          [ 38%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_filtro_por_ativo PASSED                                                                           [ 38%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_queryset_count PASSED                                                                             [ 38%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_queryset_exists PASSED                                                                            [ 38%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_nome_obrigatorio PASSED                                                                           [ 39%]
apps/eventos/tests/test_models_evento.py::TestEventoQueryset::test_str_representation PASSED                                                                         [ 39%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoCreation::test_criar_evento PASSED                                                                      [ 39%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoCreation::test_str_evento PASSED                                                                        [ 39%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoCreation::test_defaults_evento PASSED                                                                   [ 39%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoCreation::test_status_evento PASSED                                                                     [ 39%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoCreation::test_multiplos_eventos PASSED                                                                 [ 39%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoDatas::test_fim_inscricao_antes_inicio PASSED                                                  [ 39%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoDatas::test_fim_evento_antes_inicio PASSED                                                     [ 40%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoDatas::test_datas_validas PASSED                                                               [ 40%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoDatas::test_datas_iguais PASSED                                                                [ 40%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoVagas::test_vagas_negativas PASSED                                                             [ 40%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoValidacaoVagas::test_vagas_altas PASSED                                                                 [ 40%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoRelacionamentos::test_has_status PASSED                                                                 [ 40%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoRelacionamentos::test_status_has_eventos PASSED                                                         [ 40%]
apps/eventos/tests/test_models_evento_expanded.py::TestEventoRelacionamentos::test_protect_status PASSED                                                             [ 40%]
apps/eventos/tests/test_models_evento_expanded.py::TestTurmaHorario::test_turma_horario_relation PASSED                                                              [ 41%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_criar_horario_valido PASSED                                                                        [ 41%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_ler_horario PASSED                                                                                 [ 41%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_atualizar_horario PASSED                                                                           [ 41%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_deletar_horario PASSED                                                                             [ 41%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_dia_semana_valido PASSED                                                                           [ 41%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_multiplos_horarios_mesma_turma PASSED                                                              [ 41%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_hora_inicio_antes_fim PASSED                                                                       [ 41%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_hora_inicio_igual_fim_permitido PASSED                                                             [ 41%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_horario_com_turma PASSED                                                                           [ 42%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_horario_sem_turma_invalido PASSED                                                                  [ 42%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_turma_tem_multiplos_horarios PASSED                                                                [ 42%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_str_representation PASSED                                                                          [ 42%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_filtro_por_turma PASSED                                                                            [ 42%]
apps/eventos/tests/test_models_horario.py::TestHorarioModel::test_queryset_count PASSED                                                                              [ 42%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_criar_turma_valida PASSED                                                                              [ 42%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_ler_turma PASSED                                                                                       [ 42%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_atualizar_turma PASSED                                                                                 [ 43%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_deletar_turma PASSED                                                                                   [ 43%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_multiplas_turmas PASSED                                                                                [ 43%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_datas_validas_factory PASSED                                                                           [ 43%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_capacidade_positiva PASSED                                                                             [ 43%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_capacidade_grande_numero PASSED                                                                        [ 43%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_capacidade_zero_permitido PASSED                                                                       [ 43%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_turma_com_evento PASSED                                                                                [ 43%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_turma_sem_evento_invalido PASSED                                                                       [ 44%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_turma_com_horarios PASSED                                                                              [ 44%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_turma_multiplos_horarios PASSED                                                                        [ 44%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_deletar_turma_deleta_horarios PASSED                                                                   [ 44%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_criado_em_existe PASSED                                                                                [ 44%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_atualizado_em_atualiza PASSED                                                                          [ 44%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_str_representation PASSED                                                                              [ 44%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_nome_obrigatorio PASSED                                                                                [ 44%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_filtro_por_evento PASSED                                                                               [ 45%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_filtro_por_turno PASSED                                                                                [ 45%]
apps/eventos/tests/test_models_turma.py::TestTurmaModel::test_queryset_count PASSED                                                                                  [ 45%]
apps/interessados/tests/test_admin.py::TestSexoAdmin::test_list_display PASSED                                                                                       [ 45%]
apps/interessados/tests/test_admin.py::TestSexoAdmin::test_search_fields PASSED                                                                                      [ 45%]
apps/interessados/tests/test_admin.py::TestFototipoAdmin::test_list_display PASSED                                                                                   [ 45%]
apps/interessados/tests/test_admin.py::TestFototipoAdmin::test_search_fields PASSED                                                                                  [ 45%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_data_nascimento_formatada_com_data PASSED                                                   [ 45%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_data_nascimento_formatada_sem_data PASSED                                                   [ 45%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_sexo_display_com_sexo PASSED                                                                [ 46%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_sexo_display_sem_sexo PASSED                                                                [ 46%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_fototipo_display_com_fototipo PASSED                                                        [ 46%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_fototipo_display_sem_fototipo PASSED                                                        [ 46%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_programa_social_display_true PASSED                                                         [ 46%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_programa_social_display_false PASSED                                                        [ 46%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_necessidades_especiais_display_true PASSED                                                  [ 46%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_necessidades_especiais_display_false PASSED                                                 [ 46%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_celular_formatado_11_digitos PASSED                                                         [ 47%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_celular_formatado_vazio PASSED                                                              [ 47%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_telefone_formatado_10_digitos PASSED                                                        [ 47%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_telefone_formatado_vazio PASSED                                                             [ 47%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_is_active_display_ativo PASSED                                                              [ 47%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_is_active_display_inativo PASSED                                                            [ 47%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminMetodos::test_short_descriptions PASSED                                                                   [ 47%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminSaveModel::test_save_model_com_senha_nova_aplica_set_password PASSED                                      [ 47%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminActions::test_ativar_interessados PASSED                                                                  [ 48%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminActions::test_desativar_interessados PASSED                                                               [ 48%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminActions::test_gerar_senha_provisoria_rejeita_multiplos PASSED                                             [ 48%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminActions::test_gerar_senha_provisoria_um_interessado PASSED                                                [ 48%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminActions::test_exportar_interessados_retorna_csv PASSED                                                    [ 48%]
apps/interessados/tests/test_admin.py::TestInteressadoAdminActions::test_exportar_interessados_conteudo_tem_cabecalho PASSED                                         [ 48%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_get_interessado_retorna_nome PASSED                                                         [ 48%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_get_status_valido PASSED                                                                    [ 48%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_get_status_expirado PASSED                                                                  [ 48%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_get_status_usado PASSED                                                                     [ 49%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_limpar_tokens_expirados PASSED                                                              [ 49%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_limpar_tokens_usados PASSED                                                                 [ 49%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_limpar_todos_invalidos PASSED                                                               [ 49%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_has_add_permission_false PASSED                                                             [ 49%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_has_change_permission_false PASSED                                                          [ 49%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_has_delete_permission_superuser_true PASSED                                                 [ 49%]
apps/interessados/tests/test_admin.py::TestPasswordResetTokenAdmin::test_has_delete_permission_normal_user_false PASSED                                              [ 49%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendAuthenticate::test_autentica_com_cpf_e_senha_validos PASSED                                    [ 50%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendAuthenticate::test_autentica_com_senha_errada_retorna_none PASSED                              [ 50%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendAuthenticate::test_autentica_com_cpf_inexistente_retorna_none PASSED                           [ 50%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendAuthenticate::test_autentica_com_cpf_none_retorna_none PASSED                                  [ 50%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendAuthenticate::test_autentica_com_senha_none_retorna_none PASSED                                [ 50%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendAuthenticate::test_autentica_interessado_inativo_retorna_none PASSED                           [ 50%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendAuthenticate::test_autentica_sem_request_mas_com_cpf_valido PASSED                             [ 50%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendGetUser::test_get_user_com_id_valido_retorna_interessado PASSED                                [ 50%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendGetUser::test_get_user_com_id_inexistente_retorna_none PASSED                                  [ 51%]
apps/interessados/tests/test_authentication.py::TestInteressadoBackendGetUser::test_get_user_interessado_inativo_retorna_none PASSED                                 [ 51%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_valido_dados_minimos PASSED                                                        [ 51%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_cpf_duplicado PASSED                                                               [ 51%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_email_duplicado PASSED                                                             [ 51%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_senhas_nao_conferem PASSED                                                         [ 51%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_cpf_invalido_todos_iguais PASSED                                                   [ 51%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cpf_valido_com_pontuacao PASSED                                                             [ 51%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cpf_invalido_digito_verificador PASSED                                                      [ 51%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cpf_muito_curto PASSED                                                                      [ 52%]
apps/interessados/tests/test_forms.py::TestCadastroInteressadoForm::test_cadastro_sem_consentimento_lgpd PASSED                                                      [ 52%]
apps/interessados/tests/test_forms.py::TestLoginInteressadoForm::test_login_valido PASSED                                                                            [ 52%]
apps/interessados/tests/test_forms.py::TestLoginInteressadoForm::test_login_cpf_nao_cadastrado PASSED                                                                [ 52%]
apps/interessados/tests/test_forms.py::TestLoginInteressadoForm::test_login_senha_incorreta PASSED                                                                   [ 52%]
apps/interessados/tests/test_forms.py::TestLoginInteressadoForm::test_login_interessado_inativo PASSED                                                               [ 52%]
apps/interessados/tests/test_forms.py::TestLoginInteressadoForm::test_login_cpf_formatado_com_pontuacao PASSED                                                       [ 52%]
apps/interessados/tests/test_forms.py::TestEdicaoInteressadoForm::test_edicao_valida_dados_minimos PASSED                                                            [ 52%]
apps/interessados/tests/test_forms.py::TestEdicaoInteressadoForm::test_cpf_nao_aparece_na_edicao PASSED                                                              [ 53%]
apps/interessados/tests/test_forms.py::TestEdicaoInteressadoForm::test_tentativa_alterar_cpf_ignorada PASSED                                                         [ 53%]
apps/interessados/tests/test_forms.py::TestEdicaoInteressadoForm::test_edicao_sem_nome_rejeita PASSED                                                                [ 53%]
apps/interessados/tests/test_forms.py::TestEdicaoInteressadoForm::test_edicao_email_invalido_rejeita PASSED                                                          [ 53%]
apps/interessados/tests/test_models.py::TestHashCPF::test_mesmo_cpf_mesmo_hash PASSED                                                                                [ 53%]
apps/interessados/tests/test_models.py::TestHashCPF::test_cpfs_diferentes_hashes_diferentes PASSED                                                                   [ 53%]
apps/interessados/tests/test_models.py::TestHashCPF::test_hash_tem_64_caracteres PASSED                                                                              [ 53%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_senha_nao_e_texto_puro PASSED                                                                     [ 53%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_check_password_ok PASSED                                                                          [ 54%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_check_password_errado PASSED                                                                      [ 54%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_is_authenticated PASSED                                                                           [ 54%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_is_anonymous PASSED                                                                               [ 54%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_str_contem_nome PASSED                                                                            [ 54%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_cpf_criptografado_no_banco PASSED                                                                 [ 54%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_cpf_hash_unico PASSED                                                                             [ 54%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_cpf_hash_busca_eficiente PASSED                                                                   [ 54%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_nis_criptografado_no_banco PASSED                                                                 [ 54%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_factory_cria_interessado_valido PASSED                                                            [ 55%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_cpf_11_digitos_valido PASSED                                                                      [ 55%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_cpf_formatado_aceito_pelo_model PASSED                                                            [ 55%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_nis_valido PASSED                                                                                 [ 55%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_nis_muito_curto_rejeita PASSED                                                                    [ 55%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_cep_valido PASSED                                                                                 [ 55%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_cep_muito_curto_rejeita PASSED                                                                    [ 55%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_relacionamento_sexo PASSED                                                                        [ 55%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_relacionamento_fototipo PASSED                                                                    [ 56%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_relacionamentos_simultaneos PASSED                                                                [ 56%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_multiplas_deficiencias PASSED                                                                     [ 56%]
apps/interessados/tests/test_models.py::TestInteressadoModel::test_tem_deficiencia_property PASSED                                                                   [ 56%]
apps/interessados/tests/test_models.py::TestSolicitacaoExclusao::test_criada_com_status_pendente PASSED                                                              [ 56%]
apps/interessados/tests/test_models.py::TestSolicitacaoExclusao::test_todos_os_status_sao_validos PASSED                                                             [ 56%]
apps/interessados/tests/test_models.py::TestSolicitacaoExclusao::test_nome_solicitante_obrigatorio PASSED                                                            [ 56%]
apps/interessados/tests/test_models.py::TestSolicitacaoExclusao::test_email_solicitante_opcional PASSED                                                              [ 56%]
apps/interessados/tests/test_models.py::TestSolicitacaoExclusao::test_str_contem_status_e_nome PASSED                                                                [ 57%]
apps/interessados/tests/test_models.py::TestSexoModel::test_factory_cria_valido PASSED                                                                               [ 57%]
apps/interessados/tests/test_models.py::TestSexoModel::test_str_retorna_nome PASSED                                                                                  [ 57%]
apps/interessados/tests/test_models.py::TestSexoModel::test_unique_constraint_violado PASSED                                                                         [ 57%]
apps/interessados/tests/test_models.py::TestFototipoModel::test_factory_cria_valido PASSED                                                                           [ 57%]
apps/interessados/tests/test_models.py::TestFototipoModel::test_descricao_pode_ser_vazia PASSED                                                                      [ 57%]
apps/interessados/tests/test_models.py::TestPasswordResetTokenModel::test_factory_cria_token_valido PASSED                                                           [ 57%]
apps/interessados/tests/test_models.py::TestPasswordResetTokenModel::test_expiracao_futura PASSED                                                                    [ 57%]
apps/interessados/tests/test_models.py::TestPasswordResetTokenModel::test_marca_como_usado PASSED                                                                    [ 58%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_cadastro_url PASSED                                                                                     [ 58%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_login_url PASSED                                                                                        [ 58%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_logout_url PASSED                                                                                       [ 58%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_meus_dados_url PASSED                                                                                   [ 58%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_dashboard_url PASSED                                                                                    [ 58%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_detalhes_url PASSED                                                                                     [ 58%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_inscrever_evento_url PASSED                                                                             [ 58%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_senha_recuperar_url PASSED                                                                              [ 58%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_senha_recuperar_enviado_url PASSED                                                                      [ 59%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_senha_redefinir_url PASSED                                                                              [ 59%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_senha_redefinir_concluido_url PASSED                                                                    [ 59%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_senha_sem_email_url PASSED                                                                              [ 59%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_solicitar_exclusao_url PASSED                                                                           [ 59%]
apps/interessados/tests/test_urls.py::TestUrlsResolvem::test_exclusao_solicitada_url PASSED                                                                          [ 59%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_cadastro_path PASSED                                                                                        [ 59%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_login_path PASSED                                                                                           [ 59%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_logout_path PASSED                                                                                          [ 60%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_meus_dados_path PASSED                                                                                      [ 60%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_dashboard_path PASSED                                                                                       [ 60%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_detalhes_path PASSED                                                                                        [ 60%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_inscrever_evento_path PASSED                                                                                [ 60%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_senha_recuperar_path PASSED                                                                                 [ 60%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_senha_recuperar_enviado_path PASSED                                                                         [ 60%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_senha_redefinir_path PASSED                                                                                 [ 60%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_senha_redefinir_concluido_path PASSED                                                                       [ 61%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_senha_sem_email_path PASSED                                                                                 [ 61%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_solicitar_exclusao_path PASSED                                                                              [ 61%]
apps/interessados/tests/test_urls.py::TestUrlsPath::test_exclusao_solicitada_path PASSED                                                                             [ 61%]
apps/interessados/tests/test_utils.py::TestCustomEmailBackendSSLContext::test_sem_certificate_desabilita_verificacao PASSED                                          [ 61%]
apps/interessados/tests/test_utils.py::TestCustomEmailBackendSSLContext::test_com_ssl_certfile_mantem_verificacao PASSED                                             [ 61%]
apps/interessados/tests/test_utils.py::TestCustomEmailBackendSSLContext::test_context_e_cached_property PASSED                                                       [ 61%]
apps/interessados/tests/test_utils.py::TestCustomEmailBackendSSLContext::test_ssl_context_sem_cert_e_sem_keyfile PASSED                                              [ 61%]
apps/interessados/tests/test_utils.py::TestCustomEmailBackendHeranca::test_herda_de_emailbackend PASSED                                                              [ 61%]
apps/interessados/tests/test_utils.py::TestCustomEmailBackend::test_timeout_padrao_nao_definido PASSED                                                               [ 62%]
apps/interessados/tests/test_utils.py::TestCustomEmailBackend::test_timeout_personalizado PASSED                                                                     [ 62%]
apps/interessados/tests/test_views.py::TestCadastroView::test_get_retorna_200 PASSED                                                                                 [ 62%]
apps/interessados/tests/test_views.py::TestCadastroView::test_post_valido_redirect_login PASSED                                                                      [ 62%]
apps/interessados/tests/test_views.py::TestCadastroView::test_post_com_dados_completos PASSED                                                                        [ 62%]
apps/interessados/tests/test_views.py::TestCadastroView::test_post_invalido_mostra_erro PASSED                                                                       [ 62%]
apps/interessados/tests/test_views.py::TestCadastroView::test_rejeita_senha_fraca PASSED                                                                             [ 62%]
apps/interessados/tests/test_views.py::TestLoginView::test_get_retorna_200 PASSED                                                                                    [ 62%]
apps/interessados/tests/test_views.py::TestLoginView::test_post_valido_redirect_dashboard PASSED                                                                     [ 63%]
apps/interessados/tests/test_views.py::TestLoginView::test_post_inativo_mostra_erro PASSED                                                                           [ 63%]
apps/interessados/tests/test_views.py::TestLoginView::test_post_senha_errada_mostra_erro PASSED                                                                      [ 63%]
apps/interessados/tests/test_views.py::TestLoginView::test_sql_injection PASSED                                                                                      [ 63%]
apps/interessados/tests/test_views.py::TestLoginView::test_nao_expoe_mensagem_diferenciada PASSED                                                                    [ 63%]
apps/interessados/tests/test_views.py::TestLogoutView::test_logout_limpa_sessao PASSED                                                                               [ 63%]
apps/interessados/tests/test_views.py::TestLogoutView::test_logout_redirect_login PASSED                                                                             [ 63%]
apps/interessados/tests/test_views.py::TestDashboardView::test_sem_login_redirect PASSED                                                                             [ 63%]
apps/interessados/tests/test_views.py::TestDashboardView::test_inativo_redirect PASSED                                                                               [ 64%]
apps/interessados/tests/test_views.py::TestDashboardView::test_valido_retorna_200 PASSED                                                                             [ 64%]
apps/interessados/tests/test_views.py::TestDashboardView::test_context_tem_chaves_esperadas PASSED                                                                   [ 64%]
apps/interessados/tests/test_views.py::TestMeusDadosView::test_sem_login_redirect PASSED                                                                             [ 64%]
apps/interessados/tests/test_views.py::TestMeusDadosView::test_get_valido_retorna_200 PASSED                                                                         [ 64%]
apps/interessados/tests/test_views.py::TestMeusDadosView::test_edicao_valida_redirect PASSED                                                                         [ 64%]
apps/interessados/tests/test_views.py::TestMeusDadosView::test_edicao_sem_nome_rejeita PASSED                                                                        [ 64%]
apps/interessados/tests/test_views.py::TestDetalhesView::test_sem_login_redirect PASSED                                                                              [ 64%]
apps/interessados/tests/test_views.py::TestDetalhesView::test_valido_retorna_200 PASSED                                                                              [ 64%]
apps/interessados/tests/test_views.py::TestDetalhesView::test_inscricao_alheia_404 PASSED                                                                            [ 65%]
apps/interessados/tests/test_views.py::TestInscreverEventoView::test_sem_login_redirect PASSED                                                                       [ 65%]
apps/interessados/tests/test_views.py::TestInscreverEventoView::test_evento_inexistente_redirect_com_erro PASSED                                                     [ 65%]
apps/interessados/tests/test_views.py::TestInscreverEventoView::test_inscricao_valida_redirect PASSED                                                                [ 65%]
apps/interessados/tests/test_views.py::TestInscreverEventoView::test_duplicata_mostra_aviso PASSED                                                                   [ 65%]
apps/interessados/tests/test_views.py::TestSenhaRecuperarView::test_get_retorna_200 PASSED                                                                           [ 65%]
apps/interessados/tests/test_views.py::TestSenhaRecuperarView::test_post_cpf_com_email_redirect_envio PASSED                                                         [ 65%]
apps/interessados/tests/test_views.py::TestSenhaRecuperarView::test_post_cpf_sem_email_redirect_sem_email PASSED                                                     [ 65%]
apps/interessados/tests/test_views.py::TestSenhaRecuperarView::test_post_cpf_inexistente_mostra_erro PASSED                                                          [ 66%]
apps/interessados/tests/test_views.py::TestSenhaRecuperarView::test_falha_envio_email_mostra_erro PASSED                                                             [ 66%]
apps/interessados/tests/test_views.py::TestSenhaRecuperarEnviadoView::test_get_retorna_200 PASSED                                                                    [ 66%]
apps/interessados/tests/test_views.py::TestSenhaRedefinirView::test_token_valido_retorna_200 PASSED                                                                  [ 66%]
apps/interessados/tests/test_views.py::TestSenhaRedefinirView::test_post_valido_redirect_concluido PASSED                                                            [ 66%]
apps/interessados/tests/test_views.py::TestSenhaRedefinirView::test_token_expirado_mostra_tela_erro PASSED                                                           [ 66%]
apps/interessados/tests/test_views.py::TestSenhaRedefinirView::test_token_ja_usado_mostra_tela_erro PASSED                                                           [ 66%]
apps/interessados/tests/test_views.py::TestSenhaRedefinirView::test_post_senha_curta_mostra_erro PASSED                                                              [ 66%]
apps/interessados/tests/test_views.py::TestSenhaRedefinirView::test_post_senhas_diferentes_mostra_erro PASSED                                                        [ 67%]
apps/interessados/tests/test_views.py::TestSenhaRedefinirConcluidoView::test_get_retorna_200 PASSED                                                                  [ 67%]
apps/interessados/tests/test_views.py::TestSenhaSemEmailView::test_get_retorna_200 PASSED                                                                            [ 67%]
apps/interessados/tests/test_views.py::TestTrocarSenhaObrigatorioView::test_sem_login_redirect PASSED                                                                [ 67%]
apps/interessados/tests/test_views.py::TestTrocarSenhaObrigatorioView::test_sem_must_change_redirect_dashboard PASSED                                                [ 67%]
apps/interessados/tests/test_views.py::TestTrocarSenhaObrigatorioView::test_com_must_change_retorna_200 PASSED                                                       [ 67%]
apps/interessados/tests/test_views.py::TestTrocarSenhaObrigatorioView::test_post_valido_redirect_dashboard PASSED                                                    [ 67%]
apps/interessados/tests/test_views.py::TestTrocarSenhaObrigatorioView::test_post_senha_curta_mostra_erro PASSED                                                      [ 67%]
apps/interessados/tests/test_views.py::TestTrocarSenhaObrigatorioView::test_post_senhas_diferentes_mostra_erro PASSED                                                [ 67%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_sem_login_redirect_para_login PASSED                                                 [ 68%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_post_sem_login_redirect_para_login PASSED                                            [ 68%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_interessado_inativo_logout_e_redirect PASSED                                         [ 68%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_get_sem_pendente_retorna_200 PASSED                                                  [ 68%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_get_com_pendente_redirect_dashboard PASSED                                           [ 68%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_post_confirmacao_valida_cria_solicitacao PASSED                                      [ 68%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_post_confirmacao_valida_sem_motivo PASSED                                            [ 68%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_post_confirmacao_invalida_mostra_erro PASSED                                         [ 68%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_post_confirmacao_vazia_mostra_erro PASSED                                            [ 69%]
apps/interessados/tests/test_views_exclusao.py::TestSolicitarExclusaoView::test_post_com_pendente_nao_cria_nova PASSED                                               [ 69%]
apps/interessados/tests/test_views_exclusao.py::TestExclusaoSolicitadaView::test_sem_login_redirect_para_login PASSED                                                [ 69%]
apps/interessados/tests/test_views_exclusao.py::TestExclusaoSolicitadaView::test_get_com_login_retorna_200 PASSED                                                    [ 69%]
apps/interessados/tests/tests.py::TestHashCPF::test_hash_gerado_corretamente PASSED                                                                                  [ 69%]
apps/interessados/tests/tests.py::TestHashCPF::test_hash_tem_64_caracteres PASSED                                                                                    [ 69%]
apps/interessados/tests/tests.py::TestHashCPF::test_hashes_diferentes_para_cpfs_diferentes PASSED                                                                    [ 69%]
apps/interessados/tests/tests.py::TestInteressadoModel::test_check_password_correto PASSED                                                                           [ 69%]
apps/interessados/tests/tests.py::TestInteressadoModel::test_check_password_incorreto PASSED                                                                         [ 70%]
apps/interessados/tests/tests.py::TestInteressadoModel::test_is_anonymous_false PASSED                                                                               [ 70%]
apps/interessados/tests/tests.py::TestInteressadoModel::test_is_authenticated PASSED                                                                                 [ 70%]
apps/interessados/tests/tests.py::TestInteressadoModel::test_senha_criptografada PASSED                                                                              [ 70%]
apps/interessados/tests/tests.py::TestInteressadoModel::test_str PASSED                                                                                              [ 70%]
apps/interessados/tests/tests.py::TestValidacaoCPF::test_cpf_digito_verificador_errado PASSED                                                                        [ 70%]
apps/interessados/tests/tests.py::TestValidacaoCPF::test_cpf_duplicado_rejeitado PASSED                                                                              [ 70%]
apps/interessados/tests/tests.py::TestValidacaoCPF::test_cpf_formatado_aceito PASSED                                                                                 [ 70%]
apps/interessados/tests/tests.py::TestValidacaoCPF::test_cpf_sem_formatacao_aceito PASSED                                                                            [ 70%]
apps/interessados/tests/tests.py::TestValidacaoCPF::test_cpf_todos_digitos_iguais_rejeitado PASSED                                                                   [ 71%]
apps/interessados/tests/tests.py::TestValidacaoCPF::test_cpf_valido_aceito PASSED                                                                                    [ 71%]
apps/interessados/tests/tests.py::TestLoginForm::test_login_conta_inativa PASSED                                                                                     [ 71%]
apps/interessados/tests/tests.py::TestLoginForm::test_login_correto PASSED                                                                                           [ 71%]
apps/interessados/tests/tests.py::TestLoginForm::test_login_cpf_nao_cadastrado PASSED                                                                                [ 71%]
apps/interessados/tests/tests.py::TestLoginForm::test_login_senha_errada PASSED                                                                                      [ 71%]
apps/interessados/tests/tests.py::TestViews::test_dashboard_com_login_acessivel PASSED                                                                               [ 71%]
apps/interessados/tests/tests.py::TestViews::test_dashboard_sem_login_redireciona PASSED                                                                             [ 71%]
apps/interessados/tests/tests.py::TestViews::test_meus_dados_sem_login_redireciona PASSED                                                                            [ 72%]
apps/interessados/tests/tests.py::TestViews::test_pagina_cadastro_acessivel PASSED                                                                                   [ 72%]
apps/interessados/tests/tests.py::TestViews::test_pagina_login_acessivel PASSED                                                                                      [ 72%]
apps/interessados/tests/tests.py::TestViews::test_solicitar_exclusao_sem_login_redireciona PASSED                                                                    [ 72%]
apps/interessados/tests/tests.py::TestSolicitacaoExclusao::test_segunda_solicitacao_bloqueada PASSED                                                                 [ 72%]
apps/interessados/tests/tests.py::TestSolicitacaoExclusao::test_solicitacao_criada_com_confirmacao PASSED                                                            [ 72%]
apps/interessados/tests/tests.py::TestSolicitacaoExclusao::test_solicitacao_nao_criada_sem_confirmacao PASSED                                                        [ 72%]
apps/portal/tests/test_forms.py::TestLoginInteressadoForm::test_form_valido_com_cpf_e_senha_corretos PASSED                                                          [ 72%]
apps/portal/tests/test_forms.py::TestLoginInteressadoForm::test_form_valido_com_cpf_formatado PASSED                                                                 [ 73%]
apps/portal/tests/test_forms.py::TestLoginInteressadoForm::test_form_invalido_com_cpf_incorreto PASSED                                                               [ 73%]
apps/portal/tests/test_forms.py::TestLoginInteressadoForm::test_form_invalido_com_senha_incorreta PASSED                                                             [ 73%]
apps/portal/tests/test_forms.py::TestLoginInteressadoForm::test_form_invalido_interessado_inativo PASSED                                                             [ 73%]
apps/portal/tests/test_forms.py::TestLoginInteressadoForm::test_form_invalido_cpf_com_menos_de_11_digitos PASSED                                                     [ 73%]
apps/portal/tests/test_forms.py::TestLoginInteressadoForm::test_form_invalido_com_campos_vazios PASSED                                                               [ 73%]
apps/portal/tests/test_forms.py::TestConsultaPublicaForm::test_cpf_valido_sem_formatacao PASSED                                                                      [ 73%]
apps/portal/tests/test_forms.py::TestConsultaPublicaForm::test_cpf_valido_com_formatacao PASSED                                                                      [ 73%]
apps/portal/tests/test_forms.py::TestConsultaPublicaForm::test_cpf_invalido_com_menos_de_11_digitos PASSED                                                           [ 74%]
apps/portal/tests/test_forms.py::TestConsultaPublicaForm::test_cpf_invalido_vazio PASSED                                                                             [ 74%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_index_url PASSED                                                                                              [ 74%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_login_url PASSED                                                                                              [ 74%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_logout_url PASSED                                                                                             [ 74%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_dashboard_url PASSED                                                                                          [ 74%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_consulta_publica_url PASSED                                                                                   [ 74%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_resultado_evento_url PASSED                                                                                   [ 74%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_detalhes_evento_url PASSED                                                                                    [ 74%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_contato_url PASSED                                                                                            [ 75%]
apps/portal/tests/test_urls.py::TestUrlsResolvem::test_privacidade_url PASSED                                                                                        [ 75%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_index_path PASSED                                                                                                 [ 75%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_login_path PASSED                                                                                                 [ 75%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_logout_path PASSED                                                                                                [ 75%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_dashboard_path PASSED                                                                                             [ 75%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_consulta_publica_path PASSED                                                                                      [ 75%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_resultado_evento_path PASSED                                                                                      [ 75%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_detalhes_evento_path PASSED                                                                                       [ 76%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_contato_path PASSED                                                                                               [ 76%]
apps/portal/tests/test_urls.py::TestUrlsPath::test_privacidade_path PASSED                                                                                           [ 76%]
apps/portal/tests/test_views.py::TestIndexView::test_index_get_200 PASSED                                                                                            [ 76%]
apps/portal/tests/test_views.py::TestIndexView::test_index_context_eventos PASSED                                                                                    [ 76%]
apps/portal/tests/test_views.py::TestIndexView::test_index_total_eventos_int PASSED                                                                                  [ 76%]
apps/portal/tests/test_views.py::TestLoginInteressadoView::test_login_post_valido_redirect_302 PASSED                                                                [ 76%]
apps/portal/tests/test_views.py::TestLoginInteressadoView::test_login_post_valido_cria_sessao_id PASSED                                                              [ 76%]
apps/portal/tests/test_views.py::TestLoginInteressadoView::test_login_post_valido_sessao_nome PASSED                                                                 [ 77%]
apps/portal/tests/test_views.py::TestLoginInteressadoView::test_login_post_valido_sessao_cpf_mascarado PASSED                                                        [ 77%]
apps/portal/tests/test_views.py::TestLoginInteressadoView::test_login_com_sessao_redirect_302 PASSED                                                                 [ 77%]
apps/portal/tests/test_views.py::TestLogoutInteressadoView::test_logout_limpa_sessao PASSED                                                                          [ 77%]
apps/portal/tests/test_views.py::TestLogoutInteressadoView::test_logout_redirect_302 PASSED                                                                          [ 77%]
apps/portal/tests/test_views.py::TestDashboardView::test_dashboard_sem_sessao_redirect_302 PASSED                                                                    [ 77%]
apps/portal/tests/test_views.py::TestDashboardView::test_dashboard_sessao_invalida_redirect_302 PASSED                                                               [ 77%]
apps/portal/tests/test_views.py::TestDashboardView::test_dashboard_sessao_valida_nao_302 PASSED                                                                      [ 77%]
apps/portal/tests/test_views.py::TestDashboardView::test_dashboard_sessao_valida_status_ok PASSED                                                                    [ 77%]
apps/portal/tests/test_views.py::TestConsultaPublicaView::test_consulta_get_200 PASSED                                                                               [ 78%]
apps/portal/tests/test_views.py::TestConsultaPublicaView::test_consulta_post_cpf_valido_context PASSED                                                               [ 78%]
apps/portal/tests/test_views.py::TestConsultaPublicaView::test_consulta_post_cpf_invalido_mensagem PASSED                                                            [ 78%]
apps/portal/tests/test_views.py::TestConsultaPublicaView::test_consulta_post_vazio_form PASSED                                                                       [ 78%]
apps/portal/tests/test_views.py::TestResultadoEventoView::test_resultado_get_status_valido PASSED                                                                    [ 78%]
apps/portal/tests/test_views.py::TestResultadoEventoView::test_resultado_get_nao_erro_500 PASSED                                                                     [ 78%]
apps/portal/tests/test_views.py::TestDetalhesEventoView::test_detalhes_sem_sessao_redirect PASSED                                                                    [ 78%]
apps/portal/tests/test_views.py::TestDetalhesEventoView::test_detalhes_com_sessao_status_valido PASSED                                                               [ 78%]
apps/portal/tests/test_views.py::TestContatoView::test_contato_get_200 PASSED                                                                                        [ 79%]
apps/portal/tests/test_views.py::TestContatoView::test_contato_context PASSED                                                                                        [ 79%]
apps/portal/tests/test_views.py::TestPoliticaPrivacidadeView::test_politica_get_200 PASSED                                                                           [ 79%]
apps/portal/tests/test_views.py::TestPoliticaPrivacidadeView::test_politica_content_existe PASSED                                                                    [ 79%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoEventoNaoEncontrado::test_evento_inexistente_exibe_erro PASSED         [ 79%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoSemInscricoes::test_sem_inscricoes_confirmadas_exibe_aviso PASSED      [ 79%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoSemInscricoes::test_sem_inscricoes_nao_cria_classificacao PASSED       [ 79%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoSemCriterios::test_sem_criterios_exibe_aviso PASSED                    [ 79%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_pcd_atribuido PASSED                          [ 80%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_pcd_nao_atribuido_quando_sem_deficiencia PASSED [ 80%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_nis_atribuido PASSED                          [ 80%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_nis_nao_atribuido_sem_nis PASSED              [ 80%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_jovem_atribuido_16_anos PASSED                [ 80%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_jovem_atribuido_24_anos PASSED                [ 80%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_jovem_nao_atribuido_para_adulto PASSED        [ 80%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_idoso_atribuido_50_anos PASSED                [ 80%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_idoso_nao_atribuido_para_49_anos PASSED       [ 80%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_cota_racial_preta PASSED                      [ 81%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_cota_racial_parda PASSED                      [ 81%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_cota_racial_indigena PASSED                   [ 81%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_cota_racial_nao_atribuido_para_branca PASSED  [ 81%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_cota_racial_sem_fototipo PASSED               [ 81%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_escolaridade_fundamental_incompleto PASSED    [ 81%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_criterio_escolaridade_medio_completo PASSED            [ 81%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPontuacao::test_multiplos_criterios_somam_pontos PASSED                [ 81%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoCriterioOrdenacao::test_criterio_ordenacao_nao_soma_pontos PASSED      [ 82%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPosicao::test_primeiro_colocado_esta_classificado PASSED               [ 82%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPosicao::test_fora_das_vagas_esta_em_lista_espera PASSED               [ 82%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPosicao::test_total_de_classificacoes_igual_ao_total_de_inscricoes PASSED [ 82%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoPosicao::test_posicoes_sao_unicas PASSED                               [ 82%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoDesempatePorIdade::test_desempate_jovem_prioriza_mais_novo PASSED      [ 82%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoDesempatePorIdade::test_desempate_idoso_prioriza_mais_velho PASSED     [ 82%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoIdempotencia::test_segunda_execucao_nao_duplica_classificacao PASSED   [ 82%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoIdempotencia::test_segunda_execucao_nao_duplica_criterios_atendidos PASSED [ 83%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoStatusInscricao::test_inscricao_pendente_e_ignorada PASSED             [ 83%]
apps/scripts_admin/management/commands/tests/test_classificar_evento.py::TestClassificarEventoStatusInscricao::test_inscricao_confirmada_e_processada PASSED         [ 83%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisComando::test_comando_executa_sem_erro PASSED                   [ 83%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisComando::test_comando_retorna_string PASSED                     [ 83%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisComando::test_comando_nao_vazio PASSED                          [ 83%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_planejamento PASSED                  [ 83%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_inscricoes_abertas PASSED            [ 83%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_inscricoes_encerradas PASSED         [ 83%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_em_classificacao PASSED              [ 84%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_resultado_divulgado PASSED           [ 84%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_em_andamento PASSED                  [ 84%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_finalizado PASSED                    [ 84%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_status_cancelado PASSED                     [ 84%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusEventos::test_total_status_eventos PASSED                 [ 84%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_pendente PASSED                   [ 84%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_classificado PASSED               [ 84%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_confirmada PASSED                 [ 85%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_lista_espera PASSED               [ 85%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_cancelada PASSED                  [ 85%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_expirada PASSED                   [ 85%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_desistente PASSED                 [ 85%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_status_nao_localizado PASSED             [ 85%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusInscricoes::test_total_status_inscricoes PASSED           [ 85%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusMatriculas::test_status_pendente PASSED                   [ 85%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusMatriculas::test_status_ativa PASSED                      [ 86%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusMatriculas::test_status_concluida PASSED                  [ 86%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusMatriculas::test_status_trancada PASSED                   [ 86%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusMatriculas::test_status_cancelada PASSED                  [ 86%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisStatusMatriculas::test_total_status_matriculas PASSED           [ 86%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisCriterios::test_criterio_pcd PASSED                             [ 86%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisCriterios::test_criterio_programa_social PASSED                 [ 86%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisCriterios::test_criterio_jovem PASSED                           [ 86%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisCriterios::test_criterio_idoso PASSED                           [ 87%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisCriterios::test_criterio_ensino_fundamental PASSED              [ 87%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisCriterios::test_criterio_renda_baixa PASSED                     [ 87%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisCriterios::test_criterio_cota_racial PASSED                     [ 87%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSexo::test_sexo_masculino PASSED                                [ 87%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSexo::test_sexo_feminino PASSED                                 [ 87%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSexo::test_sexo_outro PASSED                                    [ 87%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSexo::test_sexo_nao_informar PASSED                             [ 87%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSexo::test_total_sexo PASSED                                    [ 87%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisFototipes::test_fototipo_branca PASSED                          [ 88%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisFototipes::test_fototipo_preta PASSED                           [ 88%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisFototipes::test_fototipo_parda PASSED                           [ 88%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisFototipes::test_fototipo_amarela PASSED                         [ 88%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisFototipes::test_fototipo_indigena PASSED                        [ 88%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisFototipes::test_total_fototipos PASSED                          [ 88%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisIntegracao::test_todos_modelos_populados PASSED                 [ 88%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisIntegracao::test_contagem_total_registros PASSED                [ 88%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisIntegracao::test_integridade_dados PASSED                       [ 89%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisIdempotencia::test_execucao_dupla_nao_duplica_dados PASSED      [ 89%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisIdempotencia::test_execucao_tripla_nao_duplica_dados PASSED     [ 89%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSaida::test_saida_contem_sucesso PASSED                         [ 89%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSaida::test_saida_contem_nome_comando PASSED                    [ 89%]
apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py::TestPopularDadosIniciaisSaida::test_saida_nao_contem_ansi PASSED                        [ 89%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionCapacity::test_matricular_alunos_capacidade_ultrapassada PASSED                                          [ 89%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionCapacity::test_matricular_alunos_capacidade_exata PASSED                                                 [ 89%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionValidation::test_validacao_evento_unico PASSED                                                           [ 90%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionValidation::test_validacao_turma_inexistente_para_evento PASSED                                          [ 90%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionValidation::test_protecao_duplicidade_matricula PASSED                                                   [ 90%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionValidation::test_validacao_turma_nao_pertence_ao_evento PASSED                                           [ 90%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionSuccess::test_sucesso_matricula_dentro_capacidade PASSED                                                 [ 90%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionSuccess::test_nenhuma_classificacao_selecionada PASSED                                                   [ 90%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionErrorHandling::test_transacao_atomica_rollback_on_matricula_save_error PASSED                            [ 90%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionErrorHandling::test_status_ativa_nao_encontrado PASSED                                                   [ 90%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionErrorHandling::test_status_confirmada_nao_encontrado PASSED                                              [ 90%]
apps/selecao/tests/test_admin.py::TestMatricularAlunosActionErrorHandling::test_classificacoes_sem_evento_associado PASSED                                           [ 91%]
apps/selecao/tests/test_models.py::TestStatusInscricaoModel::test_create_status_inscricao PASSED                                                                     [ 91%]
apps/selecao/tests/test_models.py::TestStatusInscricaoModel::test_status_inscricao_str PASSED                                                                        [ 91%]
apps/selecao/tests/test_models.py::TestStatusInscricaoModel::test_status_inscricao_unique_name PASSED                                                                [ 91%]
apps/selecao/tests/test_models.py::TestInscricaoModel::test_create_inscricao PASSED                                                                                  [ 91%]
apps/selecao/tests/test_models.py::TestInscricaoModel::test_inscricao_str PASSED                                                                                     [ 91%]
apps/selecao/tests/test_models.py::TestInscricaoModel::test_inscricao_unique_together PASSED                                                                         [ 91%]
apps/selecao/tests/test_models.py::TestInscricaoModel::test_inscricao_relacionamentos PASSED                                                                         [ 91%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_create_classificacao PASSED                                                                          [ 92%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_classificacao_str PASSED                                                                             [ 92%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_classificacao_posicao_null_default PASSED                                                            [ 92%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_classificacao_unique_inscricao PASSED                                                                [ 92%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_pontuacao_total_validacao_range PASSED                                                               [ 92%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_flags_classificacao_mutuamente_exclusivas PASSED                                                     [ 92%]
apps/selecao/tests/test_models.py::TestClassificacaoModel::test_desempate_por_data_inscricao PASSED                                                                  [ 92%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_valido PASSED                                                                   [ 92%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_none PASSED                                                                     [ 93%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_vazio PASSED                                                                    [ 93%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_ja_formatado PASSED                                                             [ 93%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_menos_de_11 PASSED                                                              [ 93%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_mascarado_valido PASSED                                                         [ 93%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_mascarado_none PASSED                                                           [ 93%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_cpf_mascarado_vazio PASSED                                                          [ 93%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_telefone_celular PASSED                                                             [ 93%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_telefone_fixo PASSED                                                                [ 93%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_telefone_none PASSED                                                                [ 94%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_telefone_vazio PASSED                                                               [ 94%]
apps/selecao/tests/test_reports.py::TestRelatorioAprovadosService::test_formatar_telefone_ja_formatado PASSED                                                        [ 94%]
apps/selecao/tests/test_reports.py::TestGerarRelatorioStaff::test_retorna_http_response PASSED                                                                       [ 94%]
apps/selecao/tests/test_reports.py::TestGerarRelatorioStaff::test_content_type_pdf PASSED                                                                            [ 94%]
apps/selecao/tests/test_reports.py::TestGerarRelatorioStaff::test_content_disposition_inline PASSED                                                                  [ 94%]
apps/selecao/tests/test_reports.py::TestGerarRelatorioStaff::test_conteudo_nao_vazio PASSED                                                                          [ 94%]
apps/selecao/tests/test_reports.py::TestGerarRelatorioStaff::test_filename_contem_staff PASSED                                                                       [ 94%]
apps/selecao/tests/test_reports.py::TestGerarRelatorioStaff::test_ordem_nome_altera_filename PASSED                                                                  [ 95%]
apps/selecao/tests/test_reports.py::TestGerarRelatorioMural::test_retorna_http_response PASSED                                                                       [ 95%]
apps/selecao/tests/test_reports.py::TestGerarRelatorioMural::test_content_type_pdf PASSED                                                                            [ 95%]
apps/selecao/tests/test_reports.py::TestGerarRelatorioMural::test_content_disposition_inline PASSED                                                                  [ 95%]
apps/selecao/tests/test_reports.py::TestGerarRelatorioMural::test_filename_contem_mural PASSED                                                                       [ 95%]
apps/selecao/tests/test_reports.py::TestGerarExcelStaff::test_retorna_http_response PASSED                                                                           [ 95%]
apps/selecao/tests/test_reports.py::TestGerarExcelStaff::test_content_type_excel PASSED                                                                              [ 95%]
apps/selecao/tests/test_reports.py::TestGerarExcelStaff::test_content_disposition_attachment PASSED                                                                  [ 95%]
apps/selecao/tests/test_reports.py::TestGerarExcelStaff::test_filename_contem_staff PASSED                                                                           [ 96%]
apps/selecao/tests/test_reports.py::TestGerarExcelStaff::test_conteudo_nao_vazio PASSED                                                                              [ 96%]
apps/selecao/tests/test_reports.py::TestGerarExcelMural::test_retorna_http_response PASSED                                                                           [ 96%]
apps/selecao/tests/test_reports.py::TestGerarExcelMural::test_content_type_excel PASSED                                                                              [ 96%]
apps/selecao/tests/test_reports.py::TestGerarExcelMural::test_filename_contem_mural PASSED                                                                           [ 96%]
apps/selecao/tests/test_services.py::TestClassificadorServicePontuacao::test_calcular_pontuacao_inscricao_com_criterios PASSED                                       [ 96%]
apps/selecao/tests/test_services.py::TestClassificadorServicePontuacao::test_calcular_pontuacao_inscricao_zero PASSED                                                [ 96%]
apps/selecao/tests/test_services.py::TestClassificadorServicePontuacao::test_calcular_pontuacao_multiplos_criterios PASSED                                           [ 96%]
apps/selecao/tests/test_services.py::TestClassificadorServicePontuacao::test_classificar_sem_eventocriterio_vinculado PASSED                                         [ 96%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_atribui_posicoes PASSED                                          [ 97%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_classifica_dentro_vagas PASSED                                   [ 97%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_lista_espera PASSED                                              [ 97%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_atualiza_status_inscricao PASSED                                 [ 97%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_com_criterios PASSED                                             [ 97%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_zero_inscricoes PASSED                                           [ 97%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_chamada_repetida PASSED                                          [ 97%]
apps/selecao/tests/test_services.py::TestClassificadorServiceClassificacao::test_classificar_evento_exatamente_1_vaga PASSED                                         [ 97%]
apps/selecao/tests/test_services.py::TestClassificadorServiceDesempate::test_desempate_por_data_inscricao_igual_pontuacao PASSED                                     [ 98%]
apps/selecao/tests/test_services.py::TestClassificadorServiceDesempate::test_desempate_com_lista_espera PASSED                                                       [ 98%]
apps/selecao/tests/test_services.py::TestClassificadorServiceDesempate::test_desempate_misto_pontuacoes_diferentes_e_iguais PASSED                                   [ 98%]
apps/selecao/tests/test_services.py::TestClassificadorServiceProcessamento::test_processar_inscricao_cria_classificacao PASSED                                       [ 98%]
apps/selecao/tests/test_validators.py::TestValidarEvento::test_evento_sem_vagas_falha PASSED                                                                         [ 98%]
apps/selecao/tests/test_validators.py::TestValidarEvento::test_evento_sem_inscricoes_falha PASSED                                                                    [ 98%]
apps/selecao/tests/test_validators.py::TestValidarEvento::test_evento_datas_invalidas_falha PASSED                                                                   [ 98%]
apps/selecao/tests/test_validators.py::TestValidarEvento::test_evento_sem_criterios_falha PASSED                                                                     [ 98%]
apps/selecao/tests/test_validators.py::TestValidarEvento::test_evento_com_criterios_passa PASSED                                                                     [ 99%]
apps/selecao/tests/test_validators.py::TestValidarInteressado::test_interessado_valido_passa PASSED                                                                  [ 99%]
apps/selecao/tests/test_validators.py::TestValidarInteressado::test_interessado_sem_nome_falha PASSED                                                                [ 99%]
apps/selecao/tests/test_validators.py::TestValidarInteressado::test_interessado_data_nascimento_futura_falha PASSED                                                  [ 99%]
apps/selecao/tests/test_validators.py::TestValidarInteressado::test_interessado_sem_sexo_gera_aviso PASSED                                                           [ 99%]
apps/selecao/tests/test_validators.py::TestValidarInscricao::test_inscricao_valida_passa PASSED                                                                      [ 99%]
apps/selecao/tests/test_validators.py::TestValidarInscricao::test_inscricao_sem_evento_falha PASSED                                                                  [ 99%]
apps/selecao/tests/test_validators.py::TestValidarInscricao::test_inscricao_sem_interessado_falha PASSED                                                             [ 99%]
apps/selecao/tests/test_validators.py::TestValidarInscricao::test_inscricao_com_data_futura_falha PASSED                                                             [100%]

---------- coverage: platform win32, python 3.13.2-final-0 -----------
Name                                                                    Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------------------
apps\__init__.py                                                            0      0   100%
apps\academico\__init__.py                                                  0      0   100%
apps\academico\admin.py                                                   320    199    38%   245-264, 270-276, 284-440, 450-613, 641-642, 666-667, 678, 681
apps\academico\apps.py                                                      5      0   100%
apps\academico\certificado.py                                             136      3    98%   103-104, 193
apps\academico\models.py                                                  110     22    80%   45, 122, 133, 142, 168, 204-206, 300-316, 339-342
apps\academico\services.py                                                136     72    47%   65-106, 121-144, 165-232, 255-283
apps\academico\urls.py                                                      5      0   100%
apps\academico\views.py                                                    63      0   100%
apps\accounts\__init__.py                                                   0      0   100%
apps\accounts\admin.py                                                     52      0   100%
apps\accounts\apps.py                                                       5      0   100%
apps\accounts\forms.py                                                      5      0   100%
apps\accounts\middleware.py                                                20      0   100%
apps\accounts\models.py                                                    22      1    95%   105
apps\accounts\urls.py                                                       5      0   100%
apps\accounts\views.py                                                     47     20    57%   27, 83-114
apps\accounts\views_exclusao.py                                            77      2    97%   44-45
apps\dashboard\__init__.py                                                  0      0   100%
apps\dashboard\admin.py                                                     0      0   100%
apps\dashboard\apps.py                                                      4      0   100%
apps\dashboard\models.py                                                    1      0   100%
apps\dashboard\services.py                                                157      0   100%
apps\dashboard\utils_pdf.py                                               373     90    76%   86-87, 90-91, 94-99, 102-107, 227-231, 235-239, 243-247, 250-252, 259-263, 267-271, 275-279, 282-284, 288-293, 416-435, 439-459, 583-603, 726-746
apps\dashboard\views.py                                                    71      0   100%
apps\eventos\__init__.py                                                    0      0   100%
apps\eventos\admin.py                                                     212     78    63%   67, 114, 196, 269-358, 371-415, 430-519
apps\eventos\apps.py                                                        5      0   100%
apps\eventos\context_processors.py                                         51      3    94%   39, 111-112
apps\eventos\management\__init__.py                                         0      0   100%
apps\eventos\management\commands\__init__.py                                0      0   100%
apps\eventos\models.py                                                    122      7    94%   106, 137, 142, 147, 152, 201, 206
apps\eventos\views.py                                                       1      1     0%   1
apps\interessados\__init__.py                                               0      0   100%
apps\interessados\admin.py                                                218     20    91%   235-238, 251, 255, 367, 380, 413-421, 480-481, 509, 514
apps\interessados\apps.py                                                   5      0   100%
apps\interessados\authentication.py                                        25      1    96%   52
apps\interessados\forms.py                                                157      8    95%   203, 227, 242, 395-396, 409, 447, 452
apps\interessados\management\__init__.py                                    0      0   100%
apps\interessados\management\commands\__init__.py                           0      0   100%
apps\interessados\management\commands\criptografar_cpfs.py                 22     22     0%   11-47
apps\interessados\management\commands\limpar_tokens.py                     59     59     0%   13-155
apps\interessados\management\commands\popular_cpf_hash.py                  22     22     0%   9-40
apps\interessados\models.py                                               139      9    94%   41, 138, 141, 144, 147, 162, 188, 191-192
apps\interessados\urls.py                                                   5      0   100%
apps\interessados\utils.py                                                 14      0   100%
apps\interessados\views.py                                                202     25    88%   60-61, 88-92, 132-134, 197-199, 209-210, 233-235, 247-248, 269-271, 282-286, 290-295
apps\interessados\views_exclusao.py                                        29      3    90%   25-27
apps\portal\__init__.py                                                     1      0   100%
apps\portal\admin.py                                                        1      0   100%
apps\portal\apps.py                                                         5      0   100%
apps\portal\forms.py                                                       34      0   100%
apps\portal\models.py                                                       1      0   100%
apps\portal\urls.py                                                         4      0   100%
apps\portal\views.py                                                       99     11    89%   72-74, 174-189, 202-220
apps\scripts_admin\__init__.py                                              0      0   100%
apps\scripts_admin\management\__init__.py                                   0      0   100%
apps\scripts_admin\management\commands\__init__.py                          0      0   100%
apps\scripts_admin\management\commands\classificar_evento.py              134      9    93%   82, 100-101, 182-184, 188-190
apps\scripts_admin\management\commands\configurar_criterios_evento.py      57     57     0%   5-91
apps\scripts_admin\management\commands\popular_criterios.py                21     21     0%   4-117
apps\scripts_admin\management\commands\popular_dados_iniciais.py           66      0   100%
apps\selecao\__init__.py                                                    0      0   100%
apps\selecao\admin.py                                                     275     88    68%   71-72, 87, 110-115, 152, 223, 233, 240-241, 247, 254-255, 266-275, 306-307, 338-343, 445, 466-503, 507-544, 552, 558, 564, 570, 580, 586, 592, 598, 661, 667
apps\selecao\apps.py                                                        5      0   100%
apps\selecao\management\__init__.py                                         0      0   100%
apps\selecao\management\commands\__init__.py                                0      0   100%
apps\selecao\models.py                                                     71      1    99%   188
apps\selecao\reports.py                                                   301     13    96%   54-55, 63-64, 95, 146, 163, 223, 346, 475, 513, 615, 653
apps\selecao\services.py                                                  125     26    79%   82-85, 89-92, 102, 106, 110, 114, 383-392, 414-432
apps\selecao\validators.py                                                105     35    67%   38-39, 47, 74, 101, 105, 116, 123, 126, 130, 149-175, 193-194, 199, 204, 213-215, 222-223
apps\selecao\views.py                                                       0      0   100%
-----------------------------------------------------------------------------------------------------
TOTAL                                                                    4207    928    78%
Coverage HTML written to dir htmlcov


===================================================================== 831 passed in 456.46s (0:07:36) =============================================================



