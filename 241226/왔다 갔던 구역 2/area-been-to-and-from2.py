n = int(input())

arr = [0] * 2000
start = 0

dist = []

for i in range(n):
    x, T = input().split()
    x = int(x)

    if T == 'L':
        left = start - x
        right = start
        start = left
    else:
        left = start
        right = start + x
        start = right

    dist.append([left, right])

for x1, x2 in dist:
    
    for i in range(x1+1000, x2+1000):
        arr[i] += 1

count = 0

for i in arr:
    if i >= 2:
        count += 1

print(count)

    

    
