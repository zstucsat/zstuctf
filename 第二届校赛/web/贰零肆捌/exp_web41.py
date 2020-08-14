# -*- coding: utf-8 -*-
# @Author : Hn13
# @Blog   : https://www.hn13.top
import requests
import pyotp
import re

url = "http://68.79.17.14:10010/verify.php"
totp = pyotp.TOTP("JBHDCMZSGIZFCTKN", 8, interval=5)
data = {
    "score": 600000,
    "totp": totp.now()
}
rule = re.compile(r'/\'Flag\'(.*?)}\'/')
r = requests.post(url, data=data)
print(r.headers)
