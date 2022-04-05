#!/usr/bin/python3
from pwn import *
conn = remote('scripting.ctf.shellmates.club',1402)
conn.recvuntil(b"g!!!\n")
while True:
    line = str(conn.recvline()).strip()
    if len(line)>10:
        if 'shellmates' not in line:
                L=eval(eval(line).decode())
                conn.sendline(("".join([i[1] for i in sorted(L)])).encode())
                try:
                    conn.recvuntil(b'_________________________________')
                except:
                    pass
        else:
            print(line[line.index('shellmates'):line.index('}')+1].strip())
            conn.close()
            break
