# flag = "picoCTF{"
# output = ''.join(
#     [chr((ord(flag[i]) << 8) + 
#     ord(flag[i + 1])) 
#     for i in range(0, len(flag), 2)
#     ])
# print((ord(output[0]) - ord(output[1]))>> 8)
# print(chr(12))
# print(chr((ord(output[0]) - ord(output[1]))>> 8) + chr(ord(output[1])))

test = u"灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽"
print(test.encode("utf-16"))