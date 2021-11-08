# "\18j|a\118i7\1e_}[hK]=\02\18\14{e6E](\5c3E\099VDB};o@W\7f\0eY\00\00"
def bitshift(n, x):
    return ((n<<24)>>24) ^ x
# input = 'picoCTF{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}'
input = "\x18j|a\x118i7\x1e_}[hK]=\x02\x18\x14{e6E](\x5c3E\x099VDB};o@W\x7f\x0eY"
output = [ord(i) for i in input]
for i,char in enumerate(input):
    outputLen = len(output)
    if i >= outputLen:
        print("weird")
        break
    if i%2==0:
        if i+1<outputLen:
            output[i], output[i + 1] = output[i + 1], output[i]
for i in reversed(range(len(output))):
    char = output[i]
    if i%3 == 0:
        char = bitshift(char, 7)
    else:
        if i%3 == 1:
            char = bitshift(char, 6)
        else:
            char = bitshift(char, 5)
    if i%2 == 0:
        char = bitshift(char, 9)
    else: 
        char = bitshift(char, 8)
    char = bitshift(char, i%10)
    if i > 2:
        char = ((output[i-3]<<24)>>24)^((char<<24)>>24)
    if i > 0:
        char = ((output[i-1]<<24)>>24)^((char<<24)>>24)
    char = bitshift(char, 20)
    if (char<<24)>>24 == 0:
        break
    output[i] = char
# print(bytes(output))

print(bytes(output))
