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
b *0x000000000040093f
continue
'''.format(**locals())
# Set up pwntools for the correct architecture
exe = './ircman'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Change logging level to help with debugging (error/warning/info/debug)
context.log_level = 'debug'
# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================


rotated = [101, 101, 97, 76, 121, 95, 14, 77, 97, 121, 95, 111, 109, 101, 33]

io = start()

io.sendlineafter(b': ', hex(rotated))

io.interactive()
