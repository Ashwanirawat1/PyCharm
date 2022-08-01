from excel_lib import read_locators
from homepage import HomePage


class LoginPage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = read_locators("loginpage")

    def login_enter_email(self, email):
        element = LoginPage.locators['txt_email']
        self.enter_element(element, value=email)

    def login_enter_password(self, password):
        element = LoginPage.locators['txt_password']
        self.enter_element(element, value=password)

    def login_click_login(self):
        element = LoginPage.locators['btn_login']
        self.click_element(element)

# class LoginPage(SeleniumWrapper):
#     def __init__(self, driver):
#         super().__init__(driver)

#     _txt_email = ("id","Email")
#     _txt_password = ("id", "Password")
#     _btn_login = ("xpath", "//input[@value='Log in']")

#     def enter_email(self, email):
#         self.enter_text(LoginPage._txt_email, value=email)

#     def enter_password(self, password):
#         self.enter_text(LoginPage._txt_password, value=password)

#     def click_login(self):
#         self.click_element(LoginPage._btn_login)
