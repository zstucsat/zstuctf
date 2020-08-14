import struct
data = [0x7dc4fa113cd6ffe9, 0x75b89ba7d812e894, 0x5df8545d6858a5b6, 0xd73978b81896b9da, 0xc9d8447f947f9d43]

def Z(a): 
    return a & 18446744073709551615

def S(str_):
    return struct.unpack('<Q', str_.encode())[0]

def T(a):
    for i in range(64):
        a = a * 2
        if a > 0xFFFFFFFFFFFFFFFF:
            a = Z(a)     
            a = Z(a ^ 0xA2014C7079FA24A3)
            continue
    return a

def U():
    print("This is ZSTU CTF 2020")
    print("And This is a easy python")
    print("You should pay a attention to odd and even\n")
    input_ = input('input your flag:')
    if len(input_) % 8 != 0:
        for i in range(8 - len(input_) % 8):
            input_ += '\x00'
        
    arr = []
    for i in range(len(input_) // 8):
        value = T(S(input_[i * 8:i * 8 + 8]))
        arr.append(value)
    
    for i in range(5):
        if arr[i] != data[i]:
            print('fail')
            exit()
            continue
    print('success！')
    exit()

U()