from _selenium1.POM1.excel_lib import read_locators
from _selenium1.POM1.homepage import HomePage


class RegistrationPage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = read_locators("registrationpage")

    def reg_select_male(self):
        element = RegistrationPage.locators['rdo_male']
        self.click_element(element)

    def reg_select_female(self):
        element = RegistrationPage.locators['rdo_female']
        self.click_element(element)

    def reg_enter_fname(self, fname):
        element = RegistrationPage.locators['txt_fname']
        self.enter_element(element, value=fname)

    def reg_enter_lname(self, lname):
        element = RegistrationPage.locators['txt_lname']
        self.enter_element(element, value=lname)

    def reg_enter_email(self, email):
        element = RegistrationPage.locators['txt_email']
        self.enter_element(element, value=email)

    def reg_enter_password(self, password):
        element = RegistrationPage.locators['txt_password']
        self.enter_element(element, value=password)

    def reg_enter_confirm_password(self, password):
        element = RegistrationPage.locators['txt_confirm_password']
        self.enter_element(element, value=password)

    def reg_click_register(self):
        element = RegistrationPage.locators['btn_register']
        self.click_element(element)