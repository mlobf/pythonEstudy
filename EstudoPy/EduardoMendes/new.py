from selenium.webdriver import Firefox

url = "https://curso-python-selenium.netlify.app/aula_03.html"

navegador = Firefox()

navegador.get(url)

a = navegador.find_element_by_tag_name('a')

a.click()


#for x in range(10):
#a.click()

#    navegador.quit()
