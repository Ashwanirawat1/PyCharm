from selenium import webdriver
from time import sleep
driver = webdriver.Chrome("../chromedriver.exe")
driver.get('file:///C:/Users/dell/Downloads/demo-html/demo.html')
driver.maximize_window()
sleep(2)
elements = driver.find_elements_by_xpath("//input[@name='download']")
for element in elements:
    element.click()
    sleep(1)

for element in elements[::-1]:
    element.click()
    sleep(1)

for element in reversed(elements):
    element.click()
    sleep(1)

# for i in range(len(elements), -1, -1):
#     elements[i].click()
#     sleep(1)