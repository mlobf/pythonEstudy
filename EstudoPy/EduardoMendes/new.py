elementos = navegador.find_elements_by_tag_name("src")

for elemento in elementos:
    print(elemento.text)

sleep(9)



navegador.quit()

# p = navegador.find_element_by_tag_name("p")

