from selenium import webdriver
from time import sleep
driver = webdriver.Chrome("../chromedriver.exe")
driver.get('file:///C:/Users/dell/Downloads/demo-html/demo.html')
driver.maximize_window()
sleep(2)
links = driver.find_elements_by_xpath("//a")
images = driver.find_elements_by_xpath("//img")
inputs = driver.find_elements_by_xpath("//input[@type = 'text']")
radios = driver.find_elements_by_xpath("//input[@type = 'radio']")
checkboxes = driver.find_elements_by_xpath("//input[@type = 'checkbox']")
tables = driver.find_elements_by_xpath("//table")

# print(links)
print(f"no of links {len(links)}")
print(f"no of images {len(images)}")
print(f"no of inputs {len(inputs)}")
print(f"no of radios {len(radios)}")
print(f"no of checkboxes {len(checkboxes)}")
print(f"no of tables {len(tables)}")

driver.close()