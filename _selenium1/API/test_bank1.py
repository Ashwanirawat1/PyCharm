from _csv import reader
from json import loads
from pytest import mark
from requests import request


def read_csv():
    with open("./bank.csv") as f:
        data = []
        rows = reader(f)
        headers = next(rows)
        for row in rows:
            data.append(tuple(row))
    return data


headers = "code, expected_branch"
data = read_csv()


@mark.parametrize(headers, data)
def test_bank(code, expected_branch):
    url = f"https://ifsc.razorpay.com/{code}"
    print(url)
    response = request("GET", url)
    response_text = response.text
    print(response_text)
    d = loads(response_text)
    actual_branch = d['BRANCH']
    assert actual_branch == expected_branch
