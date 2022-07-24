from selenium.webdriver import Chrome
from Ty_13_Confi import Confi
from Ty_15_SeleniumWrapper import SeleniumWrapper
from selenium.webdriver.common.by import By

driver =  Chrome(Confi.DRIVER_PATH)
driver.get(Confi.URL)
driver.maximize_window()

s = SeleniumWrapper(driver)

s.click_element((By.LINK_TEXT, "Log in"))
s.enter_text((By.NAME, 'Email'), value = "hello.world@company.com")
s.enter_text((By.ID, 'Password'), value = "Password123")
s.click_element((By.CSS_SELECTOR, "input[value = 'Log in']"))