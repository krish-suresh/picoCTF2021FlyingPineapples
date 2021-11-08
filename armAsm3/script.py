sp28 = 4012702611
sp44 = 0
while sp28!=0:
    if (sp28 & 1) == 0:
        sp28 = sp28 >> 1 # .L3
    else:
        sp44 += 3 # func 2
        sp28 = sp28 >> 1 # .L3

print(hex(sp44))
