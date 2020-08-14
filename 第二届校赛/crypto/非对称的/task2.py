# !/usr/bin/env python3
import socketserver
import os, sys, signal
import string, random
from gmpy2 import invert
from Crypto.Util.number import *



from secret import flag

BANNER = br"""
         _              _    __
        | |            | |  / _|
 _______| |_ _   _  ___| |_| |_
|_  / __| __| | | |/ __| __|  _|
 / /\__ \ |_| |_| | (__| |_| |
/___|___/\__|\__,_|\___|\__|_|

"""


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



    def handle(self):
        signal.alarm(1200)
        self.send(BANNER)
        e=0x1001
        p, q = getPrime(100), getPrime(100)
        N = p * q
        c=pow(bytes_to_long(flag),e,N)
        self.send(f"n={N}\ne={e}\nc={c}\nGood Luck!\n".encode())




class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 10000
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()