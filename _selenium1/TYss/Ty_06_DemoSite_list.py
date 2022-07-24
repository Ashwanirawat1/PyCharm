from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver = Chrome('../chromedriver.exe')
driver.maximize_window()
driver.get('file:///C:/Users/dell/Downloads/demo-html/demo.html')
box = driver.find_element_by_id('standard_cars')

s = Select(box)

# s.select_by_value('vol')
# sleep(2)
#
# s.select_by_index(5)
# sleep(2)
#
# s.select_by_visible_text('BMW')
# sleep(2)

current_selected_option = s.first_selected_option
print(current_selected_option)


# driver.close()

