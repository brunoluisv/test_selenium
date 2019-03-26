from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

email = "suporte@iafox.com"
senha = "4321"

browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
browser.maximize_window()
browser.get('https://demo1.test.iafox.com/')

if "Login no IAFOX" == browser.title:
	print("TITULO VALIDO = " +browser.title)
else:
	print("TITULO INVALIDO = "+browser.title)
	browser.close()

user = browser.find_element_by_name("j_username")
user.clear()
user.send_keys(email)
passwd = browser.find_element_by_name("j_password")
passwd.clear()
passwd.send_keys(senha)
login = browser.find_element_by_id("ctlForm")
login.click()
print("TESTE DE LOGIN OK")

if "IAFOX" == browser.title:
	print("TITULO VALIDO = "+browser.title)
else:
	print("TITULO INVALIDO = " +browser.title)
	browser.close()

browser.get_screenshot_as_file("test.png")
#os.system('display test.png')

elements = browser.find_elements_by_class_name('mblListItemLabel')
for e in elements:
	print(e.text)


email_layout = browser.find_element_by_xpath("/html/body/div/ul/li[6]").text
if email == email_layout:
	print("LAYOUT OK!!")
else:
	print("LAYOUT NAO CONFERE!!")
	browser.close()

logout = browser.find_element_by_xpath("/html/body/div/ul/li[6]")
logout.click()
logout = browser.find_element_by_xpath("/html/body/div/button")
logout.click()
browser.get_screenshot_as_file("logout.png")
#os.system('display logout.png')
return_link = browser.find_element_by_xpath('/html/body/a')
return_link.click()
print("TESTE DE LOGOUT OK")
browser.get_screenshot_as_file("login.png")
#os.system('display login.png')

browser.close()
