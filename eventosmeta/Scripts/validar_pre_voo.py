# Script de validação pré-voo para Django MetaReciclagem
# Executar: python validar_pre_voo.py
# Requisitos: pip install python-dotenv cryptography psycopg2-binary

import os
import sys
from dotenv import load_dotenv
from cryptography.fernet import Fernet
import psycopg2
import socket

# Raiz do projeto
project_root = r'C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta'
env_path = os.path.join(project_root, '.env')

# Cores ANSI para output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def print_status(ok, msg):
    """Imprime status com símbolo e cor"""
    symbol = Colors.GREEN + '✓' + Colors.END if ok else Colors.RED + '✗' + Colors.END
    print(f"{symbol} {msg}")

errors = []  # Lista de erros e recomendações

# 1. Verificar existência do .env
print(Colors.BLUE + "\n=== VALIDAÇÃO PRÉ-VOO ===" + Colors.END)
if not os.path.exists(env_path):
    print_status(False, "Arquivo .env não encontrado")
    errors.append(f"Baixar/colocar .env em: {env_path}")
    sys.exit(1)

# Carregar .env
load_dotenv(env_path)
print_status(True, ".env carregado")

# 2. Validar chaves críticas no .env
required_keys = {
    'SECRET_KEY': lambda v: bool(v and v.strip()),
    'FERNET_KEY': lambda v: bool(v and v.strip()),
    'DATABASE_ENGINE': lambda v: bool(v),
    'DATABASE_NAME': lambda v: bool(v),
    'DATABASE_USER': lambda v: bool(v),
    'DATABASE_PASSWORD': lambda v: bool(v),
    'DATABASE_HOST': lambda v: bool(v),
    'DATABASE_PORT': lambda v: bool(v),
    'EMAIL_HOST': lambda v: bool(v),
    'EMAIL_PORT': lambda v: bool(v),
    'EMAIL_USER': lambda v: bool(v),
    'EMAIL_PASSWORD': lambda v: bool(v),
    'EMAIL_FROM': lambda v: bool(v),
    'DEBUG': lambda v: v is not None,
    'ALLOWED_HOSTS': lambda v: bool(v),
    'LANGUAGE_CODE': lambda v: bool(v),
    'TIME_ZONE': lambda v: bool(v),
}

for key, validator in required_keys.items():
    val = os.getenv(key)
    if not validator(val):
        print_status(False, f"Chave '{key}' ausente ou inválida")
        errors.append(f"Corrigir no .env: {key}={val or ''}")
    else:
        print_status(True, f"Chave '{key}' OK")

# 3. Testes específicos

# 3.1 Teste FERNET_KEY (criptografar/decryptar)
fernet_key = os.getenv('FERNET_KEY')
try:
    f = Fernet(fernet_key)
    token = f.encrypt(b'teste_pre_voo')
    decrypted = f.decrypt(token)
    assert decrypted == b'teste_pre_voo'
    print_status(True, "FERNET_KEY válida (teste encrypt/decrypt)")
except Exception:
    print_status(False, "FERNET_KEY inválida")
    errors.append("Gerar nova FERNET_KEY: python -c \"from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())\"")

# 3.2 Conexão PostgreSQL
try:
    conn = psycopg2.connect(
        host=os.getenv('DATABASE_HOST'),
        port=os.getenv('DATABASE_PORT'),
        dbname=os.getenv('DATABASE_NAME'),
        user=os.getenv('DATABASE_USER'),
        password=os.getenv('DATABASE_PASSWORD')
    )
    conn.close()
    print_status(True, "Conexão PostgreSQL OK")
except Exception as e:
    print_status(False, f"Falha conexão DB: {str(e)[:100]}")
    errors.append("Verificar DATABASE_* no .env, usuário/senha e conectividade")

# 3.3 SMTP acessível (teste socket)
try:
    sock = socket.create_connection(('10.28.10.54', 587), timeout=10)
    sock.close()
    print_status(True, "Servidor SMTP (10.28.10.54:587) acessível")
except Exception as e:
    print_status(False, f"SMTP inacessível: {str(e)}")
    errors.append("Verificar rede/firewall para 10.28.10.54:587")

# 3.4 Diretórios obrigatórios
required_dirs = ['input', 'docs', 'scripts', 'staticfiles_collected']
for dname in required_dirs:
    dpath = os.path.join(project_root, dname)
    if os.path.isdir(dpath):
        print_status(True, f"Diretório '{dname}' OK")
    else:
        print_status(False, f"Diretório '{dname}' ausente")
        errors.append(f"Criar diretório: {dpath}")

# 3.5 manage.py existe
manage_path = os.path.join(project_root, 'manage.py')
if os.path.exists(manage_path):
    print_status(True, "manage.py OK")
else:
    print_status(False, "manage.py ausente")
    errors.append(f"Colocar manage.py em: {manage_path}")

# 4. Resumo final
print(Colors.BLUE + "\n" + "="*60 + Colors.END)
if not errors:
    print(Colors.GREEN + "\U0001f680 PRONTO PARA VOO! Todos os testes passaram com sucesso." + Colors.END)
else:
    print(Colors.RED + f"\u274c PROBLEMAS ENCONTRADOS ({len(errors)})" + Colors.END)
    print(Colors.YELLOW + "\nRECOMENDAÇÕES DE CORREÇÃO:" + Colors.END)
    for i, err in enumerate(errors, 1):
        print(f"  {i}. {err}")
    print(Colors.YELLOW + "\nCorrija os itens acima e execute novamente." + Colors.END)


    