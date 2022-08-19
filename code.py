# coding: utf-8
import requests
from bs4 import BeautifulSoup
import time

session = requests.session()
url_login = "http://drrrkari.com/#"
res_1 = session.get(
        url=url_login
        )

cookies = res_1.cookies
bs = BeautifulSoup(res_1.text, 'html.parser')
token = bs.find(attrs={'name':'token'}).get('value')
time.sleep(1)

login_info = {
    "language":"jp-JP",
    "icon":"setton",
    "name":"nyaharo",
    "login":"login",
    "token":token
}
res = session.post(
                url_login,
                data=login_info
        )
res.raise_for_status()
res.encoding = res.apparent_encoding 
print(res.text)

f = open('myfile.txt', 'w', encoding='UTF8')
f.write(res.text)
f.close()
