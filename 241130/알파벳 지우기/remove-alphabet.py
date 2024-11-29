s1 = input()
s2 = input()

l1 = ''
l2 = ''

for i in range(len(s1)):
    if ord(s1[i]) >= 48 and ord(s1[i]) <= 57:
        l1 += s1[i]

for i in range(len(s2)):
    if ord(s2[i]) >= 48 and ord(s2[i]) <= 57:
        l2 += s2[i]

print(int(l1) + int(l2))