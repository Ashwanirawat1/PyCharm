from seleniumwrapper import SeleniumWrapper
from excel_lib import read_locators
class LoginPage(SeleniumWrapper):
    def __int__(self, driver):
        super().__int__(driver)

    locators = read_locators("loginpage")

    def enter_email(self, email):
        element = LoginPage.locators['txt_email']
        self.enter_element(element, value=email)

    def enter_password(self, password):
        element = LoginPage.locators['txt_password']
        self.enter_element(element, value = password)

    def click_login(self):
        element = LoginPage.locators['btn_login']
        self.click_element(element)
