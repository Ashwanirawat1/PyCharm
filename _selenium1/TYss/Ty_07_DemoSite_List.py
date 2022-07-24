from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver = Chrome('../chromedriver.exe')
driver.maximize_window()
driver.get('file:///C:/Users/dell/Downloads/demo-html/demo.html')
box = driver.find_element_by_id('standard_cars')
s = Select(box)
all_options = s.options

# items = []
# for item in all_options:
#     items.append(item.text)
# print(items)


# using Comprehension

items = [ item.text for item in all_options]

# print(items)



car = 'Mercedes'

for index, item in enumerate(items):
    if item == car:
        s.select_by_visible_text(car)
        print(f"Index of {car} is {index}")



# for item in items:
#     s.select_by_visible_text(item)
#     sleep(0.5)
#
# for item in reversed(items):
#     s.select_by_visible_text(item)
#     sleep(0.5)
#
# for i in range(len(item)-1, -1, -1):
#     s.select_by_visible_text(items[i])
#     sleep(1)


driver.close()