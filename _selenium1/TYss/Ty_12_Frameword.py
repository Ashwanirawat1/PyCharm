from selenium.webdriver import Chrome
# from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.common.by import By

driver = Chrome(r'../chromedriver.exe')
driver.get('http://demowebshop.tricentis.com/')
driver.maximize_window()
driver.implicitly_wait(5)


# def click_element(loctype, locvalue):
#     driver.find_element(loctype, locvalue).click()
#
#
# def enter_text(loctype, locvalue, *, value):
#     driver.find_element(loctype, locvalue).clear()
#     driver.find_element(loctype, locvalue).send_keys(value)
#
#
# def select_item(loctype, locvalue, *, item):
#     element = driver.find_element(loctype, locvalue)
#     s = Select(element)
#     if isinstance(item, str):
#         s.select_by_index(item)
#     elif isinstance(item, int):
#         s.select_by_index(item)
#     else:
#         raise Exception


# click_element("link text", "Register")
#
# click_element("id", "gender-male")
#
# enter_text("name", "FirstName", value="hello")
#
# enter_text("xpath", "//input[@name = 'LastName']", value="world")
#
# enter_text("css selector", "input[name='Email']", value="hello.world@company.com")
#
# enter_text("id", "Password", value="Password123")
#
# enter_text("id", "ConfirmPassword", value="Password123")
#
# click_element("id", "register-button")

# driver.close()







# def click_element(locator):
#     driver.find_element(*locator).click()               # find_element('id', 'fname')
 
 
# def enter_text(locator, *, value):
#     loctype, locvalue = locator
#     driver.find_element(loctype, locvalue).clear()
#     driver.find_element(loctype, locvalue).send_keys(value)


# def select_item(locator, *, item):
#     loctype, locvalue = locator
#     element = driver.find_element(loctype, locvalue)
#     s = Select(element)
#     if isinstance(item, str):
#         s.select_by_index(item)
#     elif isinstance(item, int):
#         s.select_by_index(item)
#     else:
#         raise Exception


# click_element(("link text", "Register"))

# click_element(("id", "gender-male"))

# enter_text(("name", "FirstName"), value="hello")

# enter_text(("xpath", "//input[@name = 'LastName']"), value="world")

# enter_text(("css selector", "input[name='Email']"), value="hello.world@company.com")

# enter_text(("id", "Password"), value="Password123")

# enter_text(("id", "ConfirmPassword"), value="Password123")

# click_element(("id", "register-button"))

# driver.close()





def _visibility_of_element_loacted(visibility_of_element_located):
    def __init__(self,locator):
        super().__init__(locator)


    def __call__(self, driver):
        result = super().__call__(driver)
        if isinstance(result, WebElement):
            return result.is_enabled()
        else:
            return False



def _wait(func):
    def wrapper(*args, **kwargs):
        # add webdriver wait code
        locator = args[0]
        w = WebDriverWait(driver, 20)
        v = _visibility_of_element_loacted(locator)
        w.until(v, message="Progress bar was not loaded even after 20 seconds")
        return func(*args, **kwargs)
    return wrapper


@_wait        # click_element = _wait(click_element)
def click_element(locator):
    driver.find_element(*locator).click()


@_wait
def enter_text(locator, *, value):
    driver.find_element(*locator).clear()
    driver.find_element(*locator).send_keys(value)


@_wait
def select_item(locator, *, item):
    element = driver.find_element(*locator)
    s = Select(element)
    if isinstance(item, str):
        s.select_by_index(item)
    elif isinstance(item, int):
        s.select_by_index(item)
    else:
        raise Exception


click_element((By.LINK_TEXT, "Register"))

click_element((By.ID, "gender-male"))

enter_text((By.NAME, "FirstName"), value="hello")

enter_text((By.XPATH, "//input[@name = 'LastName']"), value="world")

enter_text((By.CSS_SELECTOR, "input[name='Email']"), value="hello.world@company.com")

enter_text((By.ID, "Password"), value="Password123")

enter_text((By.ID, "ConfirmPassword"), value="Password123")

click_element((By.ID, "register-button"))

driver.close()


