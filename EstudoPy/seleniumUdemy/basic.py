from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--headless")


# Objetivo e usar a lista de letras e com elas realizar uma busca em cada
# _pagina de cada letra.


letras = ["a", "b", "c", "d", "e", "f", "g", "h"]
lista = []
url_a = "https://www.yellowpages.ae/categories-by-alphabet/a.html"
url_b = "https://www.yellowpages.ae/categories-by-alphabet/b.html"
url_c = "https://www.yellowpages.ae/categories-by-alphabet/c.html"
url_d = "https://www.yellowpages.ae/categories-by-alphabet/d.html"


driver = webdriver.Chrome(options=chrome_options)

# ------------------------------------------
# A
driver.get(url_a)
a_s = driver.find_elements_by_tag_name("h2")

for x in a_s:
    lista.append(x.text)

# B
driver.get(url_b)
b_s = driver.find_elements_by_tag_name("h2")

for x in b_s:
    lista.append(x.text)

# C
driver.get(url_c)
c_s = driver.find_elements_by_tag_name("h2")

for x in c_s:
    lista.append(x.text)
# D
driver.get(url_d)
d_s = driver.find_elements_by_tag_name("h2")

for x in d_s:
    lista.append(x.text)
# ----------------------------------------------


f1 = open("/home/italia/github/pythonEstudy/EstudoPy/seleniumUdemy/relatorio.txt", "w")
print(lista, file=f1)

driver.close()
