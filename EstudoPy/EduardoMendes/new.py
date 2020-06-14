from selenium.webdriver import Firefox
from pdb import set_trace
from time import sleep


url = "https://curso-python-selenium.netlify.app/aula_03.html"
navegador = Firefox()

navegador.get(url)
sleep(1)
# pdb.set_trace()

a = navegador.find_element_by_tag_name("a")
p = navegador.find_element_by_tag_name("p")

print(f"texto de a:{a.text}")
print(f"texto de p:{p.text}")


for x in range(100):
    sleep(0.25)
    print(f"texto de p:{p.text}")
    a.click()

# navegador.quit()
