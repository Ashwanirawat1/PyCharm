from time import sleep
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Ty_13_Confi import Confi
from Ty_15_SeleniumWrapper import SeleniumWrapper

driver = Chrome(Confi.DRIVER_PATH)
driver.get(Confi.URL)
driver.maximize_window()
sleep(3)

s = SeleniumWrapper(driver)
s.click_element((By.LINK_TEXT, "Register"))

s.click_element((By.ID, "gender-male"))

s.enter_text((By.NAME, "FirstName"), value="hello")

s.enter_text((By.XPATH, "//input[@name = 'LastName']"), value="world")

s.enter_text((By.CSS_SELECTOR, "input[name='Email']"), value="hello.world@company.com")

s.enter_text((By.ID, "Password"), value="Password123")

s.enter_text((By.ID, "ConfirmPassword"), value="Password123")

s.click_element((By.ID, "register-button"))

driver.close()