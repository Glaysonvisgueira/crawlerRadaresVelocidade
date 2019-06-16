import requests
from bs4 import BeautifulSoup
import webbrowser

'''
Posicionamento dos radares de velocidade na cidade de Teresina PI.
Dados coletados no site da prefeitura:
https://pmt.pi.gov.br
'''

url = 'https://pmt.pi.gov.br/localizacao-de-radares/'      #Página onde são dispostos os arquivos PDFs com as localizações dos radares 
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

buscarLink = soup.find_all(id='core')        #Buscando a div com a class: core
links = buscarLink[0].find_all('h4')         #Buscando dentro da div com a classe core, todos os elementos com a tag: h4  

radaresFixos = links[0].find('a')
radaresEstaticos =  links[1].find('a')

print("FIXOS     " + radaresFixos.get('href'))     #Coletando o link dentro da tag: a
print("ESTÁTICOS " + radaresEstaticos.get('href')) #Coletando o link dentro da tag: a


#Utilizando a lib webbrowser para abrir o link direto na aba do navegador padrão do usuário
webbrowser.open_new_tab(radaresFixos.get('href'))
webbrowser.open_new_tab(radaresEstaticos.get('href'))



'''--------------------------------
imprimir todos os links presentes na página

for link in soup.find_all('a'):
    a = link.get('href')
    print(a)
'''    
   

   
