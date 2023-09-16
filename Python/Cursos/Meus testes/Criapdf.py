import urllib.request
from bs4 import BeautifulSoup

# Define a string com a busca no Google
query = "cybersecurity best practices"

# Abra um connection com o Google e busque a informação
result = urllib.request.urlopen("https://www.google.com.br/search?q=" + query)

# Crie um documento com a informação retornada
html_doc = result.read()

# Crie o BeautifulSoup e procuro a tags de PDF no resultado
soup = BeautifulSoup(html_doc, "lxml")

# Se houver match, crie uma lista
match = soup.findAll("a", href=True)
if match:
    links = [link["href"] for link in match]

# Imprima os links dos PDFs encontrados
for lin in links:
    print(lin)
