from time import sleep
from _pytest.fixtures import fixture
from selenium.webdriver import Chrome
from _selenium1.POM.config import Config


@fixture
def setup():
    driver = Chrome(Config.DRIVER_PATH)
    driver.get(Config.URL)
    driver.maximize_window()
    sleep(2)
    yield driver
    driver.close()




