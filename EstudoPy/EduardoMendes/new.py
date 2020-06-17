from selenium.webdriver import Firefox
from time import sleep

lista_noticias = []
firefox = Firefox()


url ='https://www.uol.com.br'


firefox.get(url)

elementos = firefox.find_elements_by_tag_name("a")

for elemento in elementos:
    lista_noticias.append(elemento.text)
sleep(1)

print(lista_noticias)


firefox.quit()






# p = navegador.find_element_by_tag_name("p")
