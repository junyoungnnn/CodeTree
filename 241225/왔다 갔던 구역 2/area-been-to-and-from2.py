n = int(input())

arr = [0] * 201
start = 0

for i in range(n):
    x, T = input().split()
    x = int(x)
    if T == 'R':
        for j in range(start, start + x + 1):
            arr[j] += 1
        start = start + x
    else:
        for j in range(start, start - x - 1, -1):
            arr[j] += 1
        start = start - x
        
count = 0
c = 0
for i in arr:
    if i >= 2:
        c += 1
    else:
        if c != 0:
            c -= 1
            count += c
            c = 0

print(count)