from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import  ActionChains

driver = Chrome("../chromedriver.exe")
driver.maximize_window()
driver.get(r"https://www.myntra.com/")

act = ActionChains(driver)

driver.implicitly_wait(10)
ele = driver.find_element("xpath", "(//a[text()='Men'])[1]")
act.move_to_element(ele).perform()

driver.find_element("xpath", "(//a[text()='Casual Shoes'])[1]").click()