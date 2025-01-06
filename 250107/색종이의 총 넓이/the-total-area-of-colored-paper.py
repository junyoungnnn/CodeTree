n = int(input())

arr = [[0] * 201 for _ in range(201)]

offset = 100

for i in range(n):
    x, y = map(int, input().split())
    x, y = x+offset, y+offset

    for k in range(x, x+8):
        for h in range(y, y+8):
            arr[k][h] = 1

count = 0
for j in range(201):
    for l in range(201):
        if arr[j][l] == 1:
            count += 1 

print(count)