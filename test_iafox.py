from selenium import webdriver as wd
import time

def test_setup():
    global driver = wd.Firefox()
    driver.get('https://demo1.test.iafox.com')
    time.sleep(5)

def test_login():
    if "Login no IAFOX" == driver.title:
        print("TITULO VALIDO = " + driver.title)
    else:
        print("TITULO INVALIDO = " + driver.title)
        driver.close()

    user = driver.find_element_by_name("j_username")
    user.clear()
    user.send_keys("suporte@iafox.com")
    passwd = driver.find_element_by_name("j_password")
    passwd.clear()
    passwd.send_keys("4321")
    login = driver.find_element_by_id("ctlForm")
    login.click()
    print("TESTE DE LOGIN OK")

def test_logout():
    logout = driver.find_element_by_xpath("//div[contains(text(), 'suporte@iafox.com')]")
    logout.click()
    logout = driver.find_element_by_xpath("/html/body/div/button")
    logout.click()
    return_link = driver.find_element_by_xpath('/html/body/a')
    return_link.click()
    print("TESTE DE LOGOUT OK")

def test_teardown():
    driver.close()
    driver.quit()
    print("TESTE COMPLETED")

