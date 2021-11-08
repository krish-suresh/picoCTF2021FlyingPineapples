from pwn import *

elf = ELF("./vuln")

local = True
if local:
    p = elf.process()
    libc = ELF('libc.so.6')
else:
    p = remote("mercury.picoctf.net", 1774)
raw_input()
print(p.recv)
p.sendline("Hi")
r = p.recvline()
print(r)
raw_input()