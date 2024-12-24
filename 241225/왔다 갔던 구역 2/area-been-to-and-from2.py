n = int(input())

arr = [0] * 201
start = 0

T2 = ''
for i in range(n):
    x, T1 = input().split()
    x = int(x)
    if T1 == T2:
        if T1 == 'R':
            for j in range(start+1, start + x + 1):
                arr[j] += 1
            start = start + x
        else:
            for j in range(start-1, start - x - 1, -1):
                arr[j] += 1
            start = start - x
    else:
        if T1 == 'R':
            for j in range(start, start + x + 1):
                arr[j] += 1
            start = start + x
        else:
            for j in range(start, start - x - 1, -1):
                arr[j] += 1
            start = start - x
    T2 = T1

count = 0
c = 0

for i in arr:
    if i >= 2:
        c += 1
    else:
        if c > 0:
            c -= 1
            count += c
            c = 0

print(count)