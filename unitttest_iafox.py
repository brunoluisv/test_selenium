from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import unittest

class LoginLogoutTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(30)
		self.browser.maximize_window()
		self.browser.get('https://demo1.test.iafox.com/')

	def test_login(self):
		browser = self.browser
		if "Login no IAFOX" == browser.title:
			print("TITULO VALIDO = " +browser.title)
		else:
			print("TITULO INVALIDO = "+browser.title)
			browser.close()	
		email = "suporte@iafox.com"
		senha = "4321"
		user = browser.find_element_by_name("j_username")
		user.clear()
		user.send_keys(email)
		passwd = browser.find_element_by_name("j_password")
		passwd.clear()
		passwd.send_keys(senha)
		login = browser.find_element_by_id("ctlForm")
		login.click()

	def title_test(self):
		browser = self.browser

		if "IAFOX" == browser.title:
			print("TITULO VALIDO = "+browser.title)
		else:
			print("TITULO INVALIDO = " +browser.title)
			browser.close()


	def logout_test(self):
		browser = self.browser
		browser.get_screenshot_as_file("test.png")
		#os.system('display test.png')

		elements = browser.find_elements_by_class_name('mblListItemLabel')
		for e in elements:
			print(e.text)

		logout = browser.find_element_by_xpath("//div[contains(text(), 'suporte@iafox.com')]")
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

	def tearDown(self):
		self.browser.close()
'''
if __name__ == '__main__':
    unittest.main()'''
    