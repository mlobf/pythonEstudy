from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--headless")

# Objetivo e usar a lista de letras e com elas realizar uma busca em cada
# _pagina de cada letra.

letras = ["a", "b", "c", "d", "e", "f", "g", "h"]
lista = []

url = "https://www.yellowpages.ae/categories-by-alphabet/a.html"

driver = webdriver.Chrome(options=chrome_options)

driver.get(url)
xs = driver.find_elements_by_tag_name("h2")

for x in xs:
    lista.append(x.text)

f1 = open("/home/italia/github/pythonEstudy/EstudoPy/seleniumUdemy/relatorio.txt", "w")
print(lista, file=f1)

driver.close()
