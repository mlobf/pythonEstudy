from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options =  Options()
chrome_options.add_argument('--headless')

# Objetivo 
#   Criar uma lista com os nomes das empresas da pagina e seus respectivos links. 
#   Se houver na pag o botao de next page, entao coletar os ultimos dados e 
#   gerar o relatoriorio. 

#letras= ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','x','z']
letras= ['a']
lista = []
driver = webdriver.Chrome(options= chrome_options)

#-----------------------------------------------------------------------

for letra in letras:
    url = f"https://www.yellowpages.ae/companies-by-alphabet/{letra}.html"
    driver.get(url)
    #xs = driver.find_elements_by_xpath('//h2/a/@href')
    xs = driver.find_elements_by_name("a")
# 
# 
# 
# 
# 
    for x in xs:
        lista.append(x.text)

f1 = open("/home/italia/github/pythonEstudy/EstudoPy/seleniumUdemy/relatorio.txt", "w")

for l in lista:
    print(l, file =f1)

driver.close()

