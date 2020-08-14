from pwn import *
from Crypto.Util.number import *
import string
from hashlib import sha256

#context.log_level = 'debug'from pwn import *
from Crypto.Util.number import *
import re
import string
import hashlib
import random


ADDRESS = '68.79.17.14'
PORT = 10003

sh = remote(ADDRESS, PORT)


def proof_of_work():

    rec = sh.recvuntil('Give me XXXX: ').strip().decode()
    suffix = re.findall(r'\(XXXX\+(.*?)\)', rec)[0]
    digest = re.findall(r'== (.*?)\n', rec)[0]

    print(suffix, digest)

    def f(x):
        return hashlib.sha256((x + suffix).encode()).hexdigest() == digest

    prefix = util.iters.mbruteforce(
        f, string.ascii_letters + string.digits, 4, 'fixed')
    return prefix


prefix = proof_of_work()
sh.sendline(prefix)

sh.interactive()
