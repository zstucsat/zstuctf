# hint: 乘二是偶，异或是奇      异或是不进位加法，与末尾是3的数进行异或，结果必为奇数

import struct

def re_d(a):
    for _ in range(64):
        if (a%2 == 1):  # 若为奇数
            tmp = a ^ 0xA2014C7079FA24A3
            if( _ == 0):
                print(tmp)
            a = tmp + 0xFFFFFFFFFFFFFFFF + 1
        a = a//2
    return a
        


cmp_data = [
0x7dc4fa113cd6ffe9,
0x75b89ba7d812e894,
0x5df8545d6858a5b6,
0xd73978b81896b9da,
0xc9d8447f947f9d43]

flag = ""
for i in cmp_data:
    tmp = re_d(i)
    print(hex(tmp))
    flag += struct.pack('<Q',tmp).decode("utf-8")

    print("flag:",flag)


