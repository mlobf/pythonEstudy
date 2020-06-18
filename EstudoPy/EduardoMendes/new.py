from selenium.webdriver import Chrome
from time import sleep


chrome = Chrome()


urls_letra = []
lista_noticias = []
letters = [
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
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "x",
]

for letter in letters:
    url2 = "https://www.yellowpages.ae/categories-by-alphabet/{}.html"


url = "https://www.yellowpages.ae/companies-by-alphabet/a.html"


elementos = chrome.find_elements_by_tag_name("a")

for elemento in elementos:
    lista_noticias.append(elemento.text)
sleep(1)

print(lista_noticias)


chrome.quit()
