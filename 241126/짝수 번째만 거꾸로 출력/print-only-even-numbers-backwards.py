s = input()
arr = []

for i in range(len(s)):
    if i % 2 == 1:
        arr.append(s[i])

arr.reverse()

for i in arr:
    print(i, end='')
