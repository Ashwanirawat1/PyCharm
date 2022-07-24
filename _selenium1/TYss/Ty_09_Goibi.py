from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
driver = Chrome(r"../chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.co.in/")
driver.implicitly_wait(10)

driver.find_element("name", "q").send_keys("goibibo.com")
driver.find_element("xpath", "(//span[text()='goibibo'])[1]").click()
driver.find_element("xpath", "(//h3[contains(text(), 'Goibibo ')])[1]").click()
driver.find_element("xpath", "(//p[contains(text(), 'Enter city or airport')])[1]").click()
driver.find_element("xpath", "//input[@type='text']").send_keys("Bengaluru")
sleep(2)
driver.find_element("xpath", "(//span[contains(text(),'Bengaluru')])[1]").click()
sleep(4)
driver.find_element("xpath", "(//p[contains(text(), 'Enter city or airport')])[2]").click()
sleep(2)
driver.find_element("xpath", "//div[@class='sc-ciZhAO dOPsYm']/..//input").send_keys("Chennai")
# driver.switch_to().active_element().send_keys("chennai")
sleep(2)
driver.find_element("xpath", "(//p[contains(text(),'Chennai')])[1]").click()