s = input()

command = input()

for i in range(len(command)):
    if command[i] == 'L':
        temp = s[0]
        s = s.replace(temp, '', 1)
        s += temp
    else:
        temp = s[-1]
        s = s.replace(s[0], temp+s[0], 1)
        s = s[:-1]

print(s)