s = input()

n = len(s)

count = 0

for i in range(n):
    for j in range(i + 1, n):
        if s[i] == '(':
            if s[j] == ')':
                count += 1
                
print(count)
