# Script para capturar conteúdo de várias URLs e gerar um PDF consolidado
# Dependências: selenium, pdfkit, webdriver-manager, wkhtmltopdf

# Passos para usar:
# 1. Instale as bibliotecas:
#    pip install selenium pdfkit webdriver-manager
# 2. Instale o wkhtmltopdf:
#    - Windows: https://wkhtmltopdf.org/downloads.html
#    - Linux: sudo apt-get install wkhtmltopdf
#    - Mac: brew install wkhtmltopdf

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pdfkit
import time

# Lista de URLs (adicione todas as abas aqui)
urls = [
    "https://claude.ai/chat/61daac55-3b19-4819-a3d5-7d929bbc580e",
    "https://claude.ai/chat/8001efac-67f5-4210-ae48-c6647b1ac705",
    "https://mermaid.live/edit#pako:eNqtWNtu8jgQfpUo11CVQwvlLstBG205qAEuVpWQSQz1KsmwtoO6bXmgfY59sR3HJJDE8PN3lwsk5uA5fTMe82n7EFC7Z1M-YGTLSfQaW_hxJ_Phy9DznMHU-vqq1-ETSV7_xe07U6tnvdob8vFqX5QdO3MUXTw7qWxEJGd-EpK6oJmS_h4uh5P5BQuc-nSdyxcl54uXsT57B0IkrCR1gHr968vy5s584aVikkbmk_SvFdrFIFxtORGk6GbOvaJEdiHzSQDWyVJZLY8v11w58-Fk4A70EXsSskAdsSO85MEpNeosjK3_7HieO0JSlq8tPSkVxW8wTSSNg1JxdJKNFfUhlv_8nQd6Yh69c5bOs5t7RlRgxdRUkfOpSerDYmm5gTX77UQSiKB4a02SqD8bWQsDByJaIXr0HU7EAIO0BkSSCRE-i2gsoaLRVwWgVwQWoyvMCfEZxLqKVW-GmGEENbxQwQIa-4yEpgAzsQrvF8I4N7gM0S6k18I5GTSEc4U5pyHdQFyNpE9D7GZejTAiLCzWcQQSJNuBNTqr2RogpCS2ZhzUyCEeXErGxPWqahOcDEKkoYmh2FFUZqIqNmICO7JKXzKRnFvL6E4SMMn2Bg03lpgKXxrVZmgFh1AphIw7TkIMPyTCiFhM_g5iQfY0vJj9azLHQlwTSWtyTWC6FpTviU-q8BE0fiPFBpIIfQvDkasQtiw2MPtc9fqKRgaeo1LIPs75B8N9cNMsGFDh47Vy7rYW9iSRiSgATtJ3maOtRJ6u_0Dn9lCRxsz_mSCGTH1F-Jb8CpxwQ9sMwMdmpKXB48YMh4Mbp04DFSX2iEUmnopoSbbERBqzmEUGYI0hqIygMxfG2W1c9eASSys6SQHGmVKJfHRCJwfMzGfwDe2eDb4S91ikKkj_F8Qdd4SbEKeBZZgAlEdM0mP9yoCc8sBoOd8Ofg7tGKykmNnqvMApW2Xmw60I8Uu5M3Tj6kZHNWm4VxdRofk0I3OtwppRYQ4Gh5aquQH5R05QbouzVJ8POEV1i_2gfUKSbiITg7wzw6wowvBg3tH-U6LUZcPxflML0zk3L5laYQxYM4C0iLfCxniLi7mRoh9430YktDwfOJ2DJKUbfwaCmftUOd7HeSDYBiV-kETDovp9n69AMAtnhistiOlasgAMPb487uZlNGrqDPjlWmkhc7h6x_65CTBPeBWxBjjl-64e3wYGTu9vDO4zViGW0yvglkKlUXwX_oaL6kfwPz1JbvEuN2DEyojjZlDamTPeBDvCMH53HPYF-GScobo6-pTLtCkyiYNds7ecBXZP8oTW7AivGKJ-2qn3-KB9w5X_1VbPq4BuCG6Z6mml1HYk_h0gyjQ5JNs3u7chocBfyU7l8fjUz0XU24_3IYml3XtIT7B7n_a73Ws379rtbvvhvtVtNDqPzVbN_svu1R8eu3eNduf-odF5arY6ncdDzf5IbTbvWs3GU6v91Oq2W_ed7mPNprhVAx_rvxnSfxsO_wJdkum-",
    "https://claude.ai/chat/46cad7f9-f7de-429f-a581-f49a1e30e778",
    "https://agent.adapta.one/agentic-chat/019a31c3-6827-7308-8384-cb9d56fe3a72",
    # Adicione outras URLs
]

# Configuração do Selenium com webdriver-manager
options = Options()
options.add_argument("--headless")  # Executa sem abrir janela
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Função para extrair texto
def extrair_texto(url):
    driver.get(url)
    time.sleep(3)  # Aguarda carregamento
    return driver.find_element("tag name", "body").text

# Monta HTML consolidado
conteudo_html = "<h1>Conversas Diversas</h1>"
for i, url in enumerate(urls, start=1):
    texto = extrair_texto(url)
    conteudo_html += f"<h2>Conversa {i}</h2><pre>{texto}</pre><hr>"

# Salva HTML e gera PDF
with open("conversas.html", "w", encoding="utf-8") as f:
    f.write(conteudo_html)

pdfkit.from_file("conversas.html", "conversas.pdf")
driver.quit()

print("✅ PDF gerado com sucesso: conversas.pdf")
