from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Test git 

from pdb import set_trace



chrome_options =  Options()
chrome_options.add_argument('--headless')

pdb.set_trace()

# Objetivo 
#   Criar uma lista com os nomes das empresas da pagina e seus respectivos links. 
#   Se houver na pag o botao de next page, entao coletar os ultimos dados e 
#   gerar o relatoriorio. 
pagina = []

for n in range(10):
    pagina.append(n)

print(pagina)

pdb.set_trace()


url = f"https://inquisicao.info/search?key=judaismo&cat=2&page={pagina}"


letras= ['a']
lista = []
driver = webdriver.Chrome(options= chrome_options)
is_novice = 0
#-----------------------------------------------------------------------

for letra in letras:
    if is_novice > 0:
        url = driver.find_element_by_xpath("//a[@id='ContentPlaceHolder1_lnkNext']/@href")
    else:
        url = f"https://www.yellowpages.ae/companies-by-alphabet/{letra}.html"
    driver.get(url)

    xs = driver.find_elements_by_xpath('//h2/a')
    #xs = driver.find_elements_by_name("a")
#    pdb.set_trace()
# 
    for x in xs:
        lista.append(x.text)

    if driver.find_element_by_xpath("//a[@id='ContentPlaceHolder1_lnkNext']"):

        print(driver.find_element_by_xpath('//a[@id='ContentPlaceHolder1_lnkNext']/@href))

        next_page = driver.find_element_by_xpath("//a[@id='ContentPlaceHolder1_lnkNext']/@href")
        next_page.click()
        is_novice +1

#------------------Relatorio----------------------------------------------------------

f1 = open("/home/italia/github/pythonEstudy/EstudoPy/seleniumUdemy/relatorio.txt", "w")

for l in lista:
    print(l, file =f1)

driver.close()

