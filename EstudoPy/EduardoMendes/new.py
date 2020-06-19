from selenium.webdriver import Chrome
from time import sleep


chr = Chrome()
lista = []


g1 = chr.get('https://g1.globo.com/')
g1.find_element_by_tag_name('a')






print(g1)

sleep(3)
chr.quit()
