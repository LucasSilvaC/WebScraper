import requests
from bs4 import BeautifulSoup
import pandas as pd
# pip install openpyxl

#URL
response = requests.get('https://lucassilvac.github.io/WebScraper/')  

#Se o site estiver no ar e correspondeer
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser') #Faz a comunicação para pegar as informações

    table_rows = soup.select('table tbody tr')  #Define a tag "tr" da tabela para o web scraper pegar

    nomes = [] #Cria duas listas vazias para armazenar nome e nota
    notas = [] 

    for row in table_rows: #Faz um for retirando cada nome e cada nota e armazenando na lista
        columns = row.find_all('td')  
        if len(columns) >= 3:  
            nomes.append(columns[0].text.strip()) 
            notas.append(columns[2].text.strip())

    data = {
        'Nome': nomes,
        'Nota': notas,
    }
    df = pd.DataFrame(data) #Com o pandas define o data com as info para colocar no xlsx 

    df.to_excel('relatorio_notas.xlsx', index=False) #Gera o excel

    print("Arquivo Excel 'relatorio_notas.xlsx' criado com sucesso!") #Exibe se o arquivo foi criado com sucesso
else:
    print(f"Erro ao acessar a página: {response.status_code}") #Retorna erro de conexão
