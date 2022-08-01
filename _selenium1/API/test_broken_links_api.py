from pytest import mark
from requests import request
from selenium.webdriver import Chrome

driver = Chrome('../chromedriver.exe')
driver.get("file:///C:/Users/dell/Downloads/demo-html/links.html")

links = driver.find_element("xpath", '//a')
urls = []

for link in links:
    urls.append((link.text, link.get_attribute("herf")))


# for url in urls:
#     print(f"Hitting url: {url} ")
#     response = request("GET", url)
#     if response.status_code == 200:
#         print("pass")
#     else:
#         print(f"FAIL: Broken link {url}")





@mark.parametrize()
def test_broken_link():
    for url in urls:
        print(f"Hitting url: {url} ")
        response = request("GET", url)
        if response.status_code == 200:
            print("pass")
        else:
            print(f"FAIL: Broken link {url}")



# @mark.parametrize("link_text, url", urls)
# def test_broken_links(link_text, url):
#     print(f"Hitting url: {url} link text {link_text}")
#     response = request("GET", url)
#     assert response.status_code == 200