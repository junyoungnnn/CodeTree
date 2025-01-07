n = int(input())

offset = 100

arr = [[0 for _ in range(201)] for _ in range(201)]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1+offset, y1+offset, x2+offset, y2+offset

    if i % 2 == 0:
        for k in range(x1, x2):
            for h in range(y1, y2):
                arr[k][h] = 0
    else:
        for k in range(x1, x2):
            for h in range(y1, y2):
                arr[k][h] = 1

count = 0
for k in range(201):
    for h in range(201):
        if arr[k][h] == 1:
            count += 1

print(count)