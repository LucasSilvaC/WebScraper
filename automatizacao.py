import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('https://lucassilvac.github.io/WebScraper/')

if response.status_code == 200:
    html = response.text  
    soup = BeautifulSoup(html, 'html.parser') 

    h2_tags = soup.find_all('h2')
    paragrafos = soup.find_all('p')

    nomes_produtos = [h2.text for h2 in h2_tags]
    precos_produtos = [paragrafo.text for paragrafo in paragrafos]

    max_length = max(len(nomes_produtos), len(precos_produtos))

    nomes_produtos += [''] * (max_length - len(nomes_produtos))
    precos_produtos += [''] * (max_length - len(precos_produtos))

    data = {
        'Produto': nomes_produtos,
        'Preço': precos_produtos,
    }

    df = pd.DataFrame(data)

    df.to_excel('produtos_cucas.xlsx', index=False)

    print("Arquivo Excel 'produtos_cucas.xlsx' criado com sucesso!")

else:
    print(f"Erro ao acessar a página: {response.status_code}")