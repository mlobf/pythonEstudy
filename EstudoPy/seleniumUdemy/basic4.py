
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")
url = f"https://www.yellowpages.ae/categories-by-alphabet/a.html"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
ddd = driver.find_elements_by_xpath("//a")

for d in ddd:

    print(d.get_attribute("href"))


#if driver.find_element_by_xpath("//a[@id='ContentPlaceHolder1_lnkNext']"):
#    print('ok')

print('nao ok')







driver.close()
