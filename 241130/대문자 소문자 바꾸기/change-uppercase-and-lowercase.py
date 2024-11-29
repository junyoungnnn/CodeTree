s = input()

s2 = ''

for i in range(len(s)):
    if ord(s[i]) < 97:
        s2 += chr(ord(s[i])+32)
    else:
        s2 += chr(ord(s[i])-32)

print(s2)