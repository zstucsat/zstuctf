# !/usr/bin/env python3
import socketserver
import os, sys, signal
import string, random
from hashlib import sha256
from random import  getrandbits,randrange
from Crypto.Util.number import getPrime

from secret import flag

BANNER = br"""
         _              _    __
        | |            | |  / _|
 _______| |_ _   _  ___| |_| |_
|_  / __| __| | | |/ __| __|  _|
 / /\__ \ |_| |_| | (__| |_| |
/___|___/\__|\__,_|\___|\__|_|

"""
LOGGER=br"""
[++++++++++++++++] Log Here [++++++++++++++++]
class LCG(object):
    def __init__(self, seed):
        self.N = getPrime(256)
        self.a = randrange(self.N)
        self.b = randrange(self.N)
        self.seed = seed % self.N
        self.state = self.seed

    def next(self):
        self.state = (self.a * self.state + self.b) % self.N
        return self.state
[++++++++++++++++] Have fun [++++++++++++++++]
"""
class LCG(object):
    def __init__(self, seed):
        self.N = getPrime(256)
        self.a = randrange(self.N)
        self.b = randrange(self.N)
        self.seed = seed % self.N
        self.state = self.seed

    def next(self):
        self.state = (self.a * self.state + self.b) % self.N
        return self.state
class Task(socketserver.BaseRequestHandler):
    def _recvall(self):
        BUFF_SIZE = 2048
        data = b''
        while True:
            part = self.request.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                break
        return data.strip()

    def send(self, msg, newline=True):
        try:
            if newline:
                msg += b'\n'
            self.request.sendall(msg)
        except:
            pass

    def recv(self, prompt=b'> '):
        self.send(prompt, newline=False)
        return self._recvall()
    def challenge(self):
        self.send(f'[++++++++++++++++] Generating challenge  [++++++++++++++++]'.encode())
        init_seed = getrandbits(256)
        lcg = LCG(init_seed)
        self.send(f'[+] init_seed = getrandbits(256)'.encode())
        self.send(f'[+] lcg = LCG(init_seed)'.encode())
        self.send(f'[+] lcg.N = {lcg.N}'.encode())
        self.send(f'[+] lcg.a = {lcg.a}'.encode())
        self.send(f'[+] lcg.b = {lcg.b}'.encode())
        self.send(f'[+] lcg.next() = {lcg.next()}'.encode())
        # print lcg.seed
        try:
            guess = int(self.recv(prompt=b'[-] lcg.seed = '))
        except:
            self.send(f'[!] Sorry, you are wrong, exit...'.encode())
            exit(0)
        if guess != lcg.seed:
            self.send(f'[!] Sorry, you are wrong, exit...'.encode())
            exit(0)
        self.send(f'[++++++++++++++++] Challenge  completed [++++++++++++++++]\n\n'.encode())



    def handle(self):
        signal.alarm(1200)
        self.send(BANNER)
        self.send(LOGGER)
        self.challenge()
        self.send('[+] Good job! Here is your flag: '.encode()+flag)



class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 10000
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()