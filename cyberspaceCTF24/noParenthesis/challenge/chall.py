#!/usr/local/bin/python3 -u
import os
import os.path
import subprocess
import tempfile

template = """
int main() {
    %s
}
"""

banned = "{}()#%?"

print("Input your code (1 line)")
code = input("> ")

for c in banned:
    if c in code:
        print("Now that would make things too easy wouldn't it...")
        exit(1)

with tempfile.TemporaryDirectory() as td:
    src_path = os.path.join(td, "source.c")
    compiled_path = os.path.join(td, "compiled")
    with open(src_path, "w") as file:
        file.write(template % code)
    
    returncode = subprocess.call(["gcc", "-Werror", "-Wall", "-O0", "-o", compiled_path, src_path], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

    if returncode != 0:
        print("Oops, there were some compilation errors!")
        exit(1)

    print("Okay hopefully it does something now!")
    subprocess.call([compiled_path])



# char* args[] = {"./readflag", 0};void* fp = execve;args[2] = args[0];args[3] = args[1];((int(*)())*(long*)(&fp))(args[2], args + 2, 0);

# char** args; args* = "readflag" ; void fp* = execve; &fp = args*;


# char* args[2];args[0] = "readflag";args[1] = 0;void* exec;*exec = args[0], args, 0;

# char* args[2];args[0] = "readflag";args[1] = NULL;void* exec;*exec = args[0], args, 0; goto *exec;


# mov rax, 0x3b;lea rdi, [rip+path];xor esi,esi;xor edx,edx;syscall;path: .string "./readflag";