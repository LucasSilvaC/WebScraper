import requests
from bs4 import BeautifulSoup
import pandas as pd
#pip install openpyxl

response = requests.get('https://lucassilvac.github.io/ValShop/')

if response.status_code == 200:
    html = response.text  
    soup = BeautifulSoup(html, 'html.parser') 

    title = soup.title.string

    h1_tags = soup.find_all('h1')
    paragrafos = soup.find_all('p')

    nomes_produtos = [h1.text for h1 in h1_tags]
    precos_produtos = [paragrafo.text for paragrafo in paragrafos]

    max_length = max(len(nomes_produtos), len(precos_produtos))

    nomes_produtos += [''] * (max_length - len(nomes_produtos))
    precos_produtos += [''] * (max_length - len(precos_produtos))

    data = {
        'Produto': nomes_produtos,
        'Preço': precos_produtos,
    }

    df = pd.DataFrame(data)

    df.to_excel('produtos_valshop.xlsx', index=False)

    print("Arquivo Excel 'produtos_valshop.xlsx' criado com sucesso!")

else:
    print(f"Erro ao acessar a página: {response.status_code}")