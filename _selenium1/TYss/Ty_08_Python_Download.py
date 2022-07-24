from time import sleep

from selenium.webdriver import Chrome

driver = Chrome('../chromedriver.exe')
driver.maximize_window()
driver.get('https://www.python.org/downloads/')
sleep(5)

driver.find_element_by_xpath("(//input[@name='download'])[3]").click()
driver.find_element_by_xpath("//td[text()='Python']/..//input[@name='download']").click()