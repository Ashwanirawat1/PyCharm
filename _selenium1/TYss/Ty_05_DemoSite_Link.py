from selenium.webdriver import Chrome
from time import sleep

driver = Chrome('../chromedriver.exe')
driver.get('https://www.python.org/')
driver.maximize_window()
sleep(2)

links = driver.find_elements_by_xpath("//a")

# for link in links:
#     link_text = link.text
#     if 'Python' in link_text:
#         print(link_text)
#         sleep(0.5)

# for link in links:
#     print(link.get_attribute("href"))
#     sleep(0.5)



for link in links:
    link_text = link.text
    if 'Python' in link_text:
        print(link_text, link.get_attribute("href"))
        sleep(0.5)

driver.close()