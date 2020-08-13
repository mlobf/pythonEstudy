"""
Este script tem por objetivo criar um buscador no site inquisiçao.
Nele devera ser usado criterios para buscar os i

Objetivo, buscar o judeus brasileiros que foram persequidos pela inquisicao.
    Gerar informaçoes com estes dados, tais como sobrenomes.
    Salvar estas infos em um banco de dados.
    
Ferramentas:
    ->Selenium
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
url = "https://inquisicao.info/search?key=Juda%C3%ADsmo&cat=2&page=1"
driver.get(url)

# Definir a ultima pagina no footer, o elemento e o nome do penuntimo campo
# disponivel.
x = driver.find_elements_by_tag_name("li")
total_paginas = x[-2].text
#total_de_paginas = 10
#    O total de paginas e o numero maximo iteravel no range paginas
for p in range(int(total_paginas)):
    url1 = f"https://inquisicao.info/search?key=Juda%C3%ADsmo&cat=2&page={p}"
    driver.get(url1)
# Buscar a lista dos Processos por nomes.----------------------------------
    x = driver.find_elements_by_class_name('card-title')
    for n in x:
        print(n.text)
# --------------------------------------------------------------------------
"""
for n in x:
    print(n.text)

if x:
    print("ok, I got  It")
else:
    print("Houston we have a problem")

print(x[-2].text)
"""
