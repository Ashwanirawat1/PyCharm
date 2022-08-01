from _selenium1.POM.homepage import HomePage
from _selenium1.POM.loginpage import LoginPage


def test_login(setup):
    hp = HomePage(setup)
    hp.click_login()
    lp = LoginPage(setup)
    lp.enter_email("hello.world@company.com")
    lp.enter_password("Password123")
    lp.click_login()
