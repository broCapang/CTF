section .data
    filename db 'flag.txt', 0          ; File name (null-terminated)
    buffer   times 128 db 0            ; Buffer to hold the file content
    len      equ $ - buffer            ; Length of the buffer

section .bss

section .text
global _start

_start:
    ; Open the file (sys_open)
    mov rax, 0x2                       ; Syscall number for sys_open
    lea rdi, [rel filename]            ; Load the address of the filename into RDI
    xor rsi, rsi                       ; Flags (0 - read only)
    syscall                            ; Trigger syscall
    mov rdi, rax                       ; Save the file descriptor in RDI

    ; Read the file (sys_read)
    mov rax, 0x0                       ; Syscall number for sys_read
    mov rsi, buffer                    ; Load the address of the buffer into RSI
    mov rdx, 128                       ; Number of bytes to read
    syscall                            ; Trigger syscall

    ; Write to stdout (sys_write)
    mov rax, 0x1                       ; Syscall number for sys_write
    mov rdi, 1                         ; File descriptor (stdout)
    mov rsi, buffer                    ; Load the address of the buffer into RSI
    syscall                            ; Trigger syscall
