x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

offset = 1000
x1, y1, x2, y2 = x1+offset, y1+offset, x2+offset, y2+offset
x3, y3, x4, y4 = x3+offset, y3+offset, x4+offset, y4+offset

arr = [[0] * 2001 for _ in range(2001)]

for i in range(x1, x2):
    for j in range(y1, y2):
        arr[i][j] = 1

for i in range(x3, x4):
    for j in range(y3, y4):
        arr[i][j] = 0

count = 0
for i in range(x1, x2):
    for j in range(y1, y2):
        if arr[i][j] == 1:
            count += 1

max_width = 0
max_height = 0

# y축 길이 찾기
for i in [x1, x2-1]:
    count = 0
    for j in range(y1, y2):
        if arr[i][y1] == 1 and arr[i][y2-1] == 1:
            max_height = y2 - y1
        else:
            if arr[i][j] == 1:
                count += 1
                if count > max_height:
                    max_height = count

# x축 길이 찾기
for i in [y1, y2-1]:
    count = 0
    for j in range(x1, x2):
        if arr[x1][i] == 1 and arr[x2-1][i] == 1:
            max_width = x2 - x1
        else:
            if arr[j][i] == 1:
                count += 1
                if count > max_width:
                    max_width = count

print(max_height * max_width)
