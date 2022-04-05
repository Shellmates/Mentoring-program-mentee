#!/usr/bin/python3

from pwn import *


def get_op(r):
    r.recvuntil(": ")
    return map(int, r.recvline().strip().split(b"+"))


def send_res(r, res):
    r.recvuntil("> ")
    r.sendline(res)


r = remote("scripting.ctf.shellmates.club", 1401)

for i in range(100):
    op1, op2 = get_op(r)
    print(op1, op2)
    res = str(op1 + op2)
    send_res(r, res)

r.interactive()
