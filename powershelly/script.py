import textwrap
import os
import subprocess, sys
randList = []
for i in range(264 + 1):
    y = ((((i+1) * 327) % 681 ) + 344) % 313
    randList.append(y)


seedList = []
for i in range(264+1):
    seedList.append(((i+1) * 127) % 500)
# print(seedList)

f = open("outputOriginal.txt", "r")
blocks = []
result = 0
for k,stringOfOutput in enumerate(f):
    var = int(stringOfOutput)
    blockCount = 5
    # var = 879059547225600221
    seed=seedList[k]
    a = randList[k]^var
    funReturn = a^result # k=0 879059547225600240
    binStr = str(bin(funReturn))
    bn = []
    for i,char in enumerate(binStr):
        if i%2==0:
            bn.append(binStr[i:i+2])
    bn.pop(0)
    # print(bn)
    raw = ['C' for i in range(blockCount*6)]
    xAssigned = []
    for i in range(len(raw)):
        x = (i*seed)%(blockCount*6)
        while bn[x] == "10":
            x = (x + 1)%len(raw)#try both
        
        if bn[x] == "11":    
            raw[i] = "1"
        else:
            raw[i] = "0"
        bn[x] = "10"
    rawBlock = ''.join(raw)
    blocks.append(textwrap.wrap(rawBlock, 6))
    result = var
print(len(blocks))

inputFile = open("input.txt", "w")
f2 = open("C:/Users/krisu/input.txt", "w")
for i in range(len(blocks[0])):
    line = ""
    for x in blocks:
        line += x[i]+" "
    line = line[:-1] + '\n'
    inputFile.write(line)
    f2.write(line)
if os.path.exists("output.txt"):
    os.remove("output.txt")
# p = subprocess.Popen(["powershell.exe", 
#               "C:\\Users\\krisu\\Documents\\pico\\rev_PS.ps1"], 
#               stdout=sys.stdout)
# p.communicate()