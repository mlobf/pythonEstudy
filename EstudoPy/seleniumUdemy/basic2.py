# test 1234
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

# Objetivo e usar a lista de letras e com elas realizar uma busca em cada
# _pagina de cada letra.
# -----------------------------------------------------------------------

letras = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "x",
    "z",
]
# letras= ['a','b','c']
lista = []
driver = webdriver.Chrome(options=chrome_options)
# -----------------------------------------------------------------------
for letra in letras:
#    url = f"https://www.yellowpages.ae/categories-by-alphabet/{letra}.html"
    url = f"https://www.yellowpages.ae/categories-by-alphabet/{letra}.html"
    driver.get(url)
    

    xs = driver.find_elements_by_tag_name("h2")
    for x in xs:
        lista.append(x.text)
        print(x.text)




from selenium import webdriver

f1 = open("/home/italia/Área de trabalho/pythonEstudy/EstudoPy/scrapy/relatorio.txt", "w")

for l in lista:
    print(l, file=f1)

driver.close()

