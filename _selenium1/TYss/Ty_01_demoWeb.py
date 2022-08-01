# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome("../chromedriver.exe")
# driver.get('http://demowebshop.tricentis.com/login')
# driver.find_element_by_class_name('ico-register').click()
# driver.find_element_by_id('gender-male').click()
# driver.find_element_by_id('FirstName').send_keys('Ashwani')
# driver.find_element_by_id('LastName').send_keys('Rawat')
# driver.find_element_by_id('Email').send_keys('ashwinrawat354@gmail.com')
# driver.find_element_by_id('Password').send_keys('ashwani')
# sleep(2)
# driver.find_element_by_id('ConfirmPassword').send_keys('ashwani')
# driver.find_element_by_id('register-button').click()

# def deco(func):
#     def wrapper():
#         print("python is proramin language")
#         func()
#         print("prorgaming is fun")
#         return func
#     return wrapper
#
#
# @deco
# def what_is_python():
#     print("I'm learning")
#
# what_is_python()


def pos(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return abs(result)
    return inner

@pos
def add(a, b):
    return a+b

print(add(5, -6))