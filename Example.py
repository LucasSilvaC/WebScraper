import requests
from bs4 import BeautifulSoup

response = requests.get('https://example.com')

if response.status_code == 200:
    html = response.text  
    soup = BeautifulSoup(html, 'html.parser') 

    title = soup.title.string
    print(f"Título da página: {title}")

    h1_tags = soup.find_all('h1')
    print("H1 encontrados:")
    for h1 in h1_tags:
        print(h1.text) 

    paragrafos = soup.find_all('p')
    for paragrafo in paragrafos:
        print(paragrafo.text)

else:
    print(f"Erro ao acessar a página: {response.status_code}")

