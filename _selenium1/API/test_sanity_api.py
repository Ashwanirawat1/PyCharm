from pytest import mark
from requests import request

headers = "page"
# pages = ['login', 'register', 'cart', 'iphone', 'electronics',
#          'wishlist', 'books', 'computers', 'desktops', 'notebooks',
#          'accessories', 'hello', 'electronics','camera-photo',
#          'cell-phones', 'apparel-shoes', 'digital-downloads',
#          'jewelry', 'gift-cards', 'iphone'
#          ]
#
# def test_api_sanity():
#     for page in pages:
#         url = f"http://demowebshop.tricentis.com/{page}"
#         response = request("GET", url)
#         if response.status_code == 200:
#             print("PASS")
#         else:
#             print(f"FAIL: {page}")









pages = [('login',), ('register', ), ('cart',), ('iphone', ), ('electronics',),
        ('wishlist',), ('books', ), ('computers', ), ('desktops', ),
        ('notebooks', ), ('accessories',), ('hello',),
        ('electronics,'),('camera-photo',),
        ('cell-phones',), ('apparel-shoes',),
        ('digital-downloads',), ('jewelry',),
        ('gift-cards',), ('iphone',)
         ]



# @mark.parametrize("page", pages)
# def test_api_sanity(page):
#     page = page[0]
#     url = f"http://demowebshop.tricentis.com/{page}"
#     response = request("GET", url)
#     if response.status_code == 200:
#         print(f"PASS: {url}")
#     else:
#         print(f"FAIL: {url}")




@mark.parametrize("page", pages)
def test_api_sanity(page):
    page = page[0]
    url = f"http://demowebshop.tricentis.com/{page}"
    response = request("GET", url)
    assert response.status_code == 200
#sanity.html






