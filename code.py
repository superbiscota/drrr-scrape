import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

session = requests.session()

login_info = {
    "language":"jp-JP",
    "icon":"setton",
    "name":"nyaharo",
    "login":"login",
    "token":"35cb62b76541bdb25b7c8976a52e97d2"
}

url_login = "http://drrrkari.com/#"
res = session.post(url_login, data=login_info)
res.raise_for_status()

print(res.text)