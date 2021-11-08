x = 0 # (sp+28)
k = 3297082261 # (sp+12)
# print(hex(int(str(hex(k))[6:], 16)*3))
z = 0 # (sp+24)
while x < k:
    z+=3
    x+=1
    if z%100000==0:
        print(z)
print(z)


print(hex(9891246783))

# 9891246783
0x24d9072bf