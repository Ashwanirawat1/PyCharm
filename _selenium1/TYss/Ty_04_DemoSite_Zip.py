from selenium.webdriver import Chrome
from time import sleep

driver = Chrome('../chromedriver.exe')
driver.get('file:///C:/Users/dell/Downloads/demo-html/demo.html')
driver.maximize_window()
sleep(2)

boxes = driver.find_elements_by_xpath('//input[@name="fname"]')
words = ['hello', 'world', 'apple', 'google', 'microsoft', 'walmart', 'bestbuy', 'whatsapp', 'instagram']

for box,word in zip(boxes, words):
    box.send_keys(word)
    sleep(0.5)

driver.close()