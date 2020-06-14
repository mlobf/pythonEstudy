from selenium.webdriver import Firefox
import pdb
import time

url = "https://curso-python-selenium.netlify.app/aula_03.html"
navegador = Firefox()

navegador.get(url)

pdb.set_trace()

a = navegador.find_element_by_tag_name("a")

for x in range(28):
    a.click()
    time.sleep(1)

# for x in range(10):
# a.click()

#    navegador.quit()
