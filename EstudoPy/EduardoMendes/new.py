from selenium.webdriver import Firefox
from pdb import set_trace
from time import sleep

url1 = "https://www.webmotors.com.br/carros-usados/estoque/bmw/320i/de.2015/ate.2019?tipoveiculo=carros-usados&anoate=2019&anode=2015&marca1=BMW&media=com%20fotos&modelo1=320i&o=6"

#url = "https://curso-python-selenium.netlify.app/aula_03.html"

navegador = Firefox()
navegador.get(url1)

sleep(1)
# pdb.set_trace()


elementos = navegador.find_elements_by_tag_name("strong")

for elemento in elementos:
    print(elemento.text)

sleep(5)


navegador.quit()


# p = navegador.find_element_by_tag_name("p")

# print(f"texto de a:{a.text}") #print(f"texto de p:{p.text}")


# for x in range(100):
#    sleep(0.25)
#    print(f"texto de p:{a.text}")
#    a.click()

# mais um comentario
# navegador.quit()
