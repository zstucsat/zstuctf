#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from Crypto.Util.number import *
from gmpy2 import invert
from hashlib import sha256
import string
import os
import random
from secret import flag, e


assert e.bit_length() == 477
BITS = 512

def proof_of_work():
    random.seed(os.urandom(8))
    proof = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(20)])
    digest = sha256(proof.encode()).hexdigest()
    print("sha256(XXX+%s) == %s" % (proof[3:], digest))
    print('Give me XXX:', end = '')
    x = input().replace('\n', '')
    if len(x) != 3 or sha256((x + proof[3:]).encode()).hexdigest() != digest: 
        return True
    return False

def eat_cake():
    p, q = getPrime(BITS), getPrime(BITS)
    ph = (p - 1) * (q + 1)
    N = p * q
    d = invert(e, ph)
    
    cake = getPrime(BITS >> 1 | BITS)
    q = getPrime(BITS << 1 | BITS)
    f = d
    g = getPrime(q.bit_length() - f.bit_length() - 1)
    f_inv_q = invert(f, q)
    h = f_inv_q * g % q
    r = getPrime(BITS)
    c = (r * h + cake) % q
    print(q, h, c)
    print(N)
    print(pow(cake, 0x10001, N))
    
    answer = int(input("Give me your cake:"))
    print("This cake looks delicious!" if cake != answer else flag)
    return

def make_cake():
    p, q = getPrime(BITS), getPrime(BITS)
    N = p * q
    ph = (p - 1) * (q + 1)
    d = invert(e, ph)
    
    cake = getPrime(BITS >> 1)
    q = getPrime(BITS << 1 | BITS)
    f = d
    g = getPrime(q.bit_length() - f.bit_length() - 1)
    f_inv_q = invert(f, q)
    h = f_inv_q * g % q
    r = getPrime(BITS)
    c = (r * h + cake) % q
    print(q, h, c)
    print(N)
    print(pow(cake, d, N))
    
    return

if __name__ == '__main__':
    if(proof_of_work()):
        exit()
    print('''
                                                                                      
  _|_|_|    _|_|    _|    _|  _|_|_|_|        _|_|_|    _|_|    _|      _|  _|_|_|_|  
_|        _|    _|  _|  _|    _|            _|        _|    _|  _|_|  _|_|  _|        
_|        _|_|_|_|  _|_|      _|_|_|        _|  _|_|  _|_|_|_|  _|  _|  _|  _|_|_|    
_|        _|    _|  _|  _|    _|            _|    _|  _|    _|  _|      _|  _|        
  _|_|_|  _|    _|  _|    _|  _|_|_|_|        _|_|_|  _|    _|  _|      _|  _|_|_|_|  
                                                                                      
    ''')
    print("WELCOME TO MY CAKE GAME!")
    print("1.EAT MY CAKE\n2.MAKE A CAKE\n3.EXIT")
    op = int(input("What's your choice?\n"))
    if op == 1:
        print("Here is my cake:")
        eat_cake()
    elif op == 2:
        print("Let's make a big cake!")
        make_cake()
    elif op == 3:
        print("Bye~")
        exit()
    else:
        print("Your choice is so strange!")
        exit()