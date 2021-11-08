key = ['f1','a7','f0','07','ed']
flag = ['9d','6e','93','c8','b2','b9','41','8b','c1','c5','dc','61','c6','97','94','8c','66','91','91','c1','89','33','94','9e','c9','dd','61','91','c4','c8','dd','62','c0','92','c1','8c','37','95','93','c8','90','00','00']
output = ''
for i,char in enumerate(flag):
    keyIndex = 4 - (i % 5)
    keyVal = int(key[keyIndex],16)
    flagVal = int(char, 16)
    print(flagVal)
    output += chr(((keyVal<<24)>>24)^flagVal)
print(output)