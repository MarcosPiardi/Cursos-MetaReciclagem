# Seguranca Docker

## Importante

1. Nunca commite .env com senhas
2. Use .env.example para template
3. Altere senhas reais no servidor

## Gerar chaves

SECRET_KEY:
  python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

FERNET_KEY:
  python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"

## Checklist

- [ ] .env.example no git
- [ ] .env no .gitignore
- [ ] Senhas alteradas no servidor
- [ ] DEBUG=False em producao
- [ ] SSL configurado
