x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

offset = 1000

x1, y1, x2, y2 = x1+offset, y1+offset, x2+offset, y2+offset
x3, y3, x4, y4 = x3+offset, y3+offset, x4+offset, y4+offset
x5, y5, x6, y6 = x5+offset, y5+offset, x6+offset, y6+offset

arr = [[0] * 2001 for _ in range(2001)]

for i in range(x1, x2):
    for j in range(y1, y2):
        arr[i][j] = 1

for i in range(x3, x4):
    for j in range(y3, y4):
        arr[i][j] = 1

for i in range(x5, x6):
    for j in range(y5, y6):
        arr[i][j] = 0

count = 0
for k in range(2001):
    for h in range(2001):
        if arr[k][h] == 1:
            count += 1

print(count)