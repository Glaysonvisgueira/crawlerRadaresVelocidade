import requests
from bs4 import BeautifulSoup
import webbrowser

'''
Posicionamento dos radares de velocidade na cidade de Teresina PI.
Dados coletados no site da prefeitura:
https://pmt.pi.gov.br
'''

url = 'https://pmt.pi.gov.br/localizacao-de-radares/'   
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

buscarLink = soup.find_all(id='core')
links = buscarLink[0].find_all('h4')

radaresFixos = links[0].find('a')
radaresEstaticos =  links[1].find('a')

print("FIXOS     " + radaresFixos.get('href'))
print("ESTÁTICOS " + radaresEstaticos.get('href'))

webbrowser.open_new_tab(radaresFixos.get('href'))
webbrowser.open_new_tab(radaresEstaticos.get('href'))



'''--------------------------------
imprimir todos os links presentes na página

for link in soup.find_all('a'):
    a = link.get('href')
    print(a)
'''    
   
