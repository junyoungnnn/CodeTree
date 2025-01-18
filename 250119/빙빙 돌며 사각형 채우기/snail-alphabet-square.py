n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

d = 1

x, y = 0, 0

alpha = 'A'

arr[x][y] = alpha

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

for i in range(1, n * m + 1):
    nx, ny = x + dxs[d], y + dys[d]
    if i > 25:
        i = i % 26

    if in_range(nx, ny) and arr[nx][ny] == 0:
        arr[nx][ny] = chr(ord(alpha) + i)
    else:
        d = (d + 1) % 4
        nx, ny = x + dxs[d], y + dys[d]
        if in_range(nx, ny) and arr[nx][ny] == 0:
            arr[nx][ny] = chr(ord(alpha) + i)

    x, y = nx, ny

for k in range(n):
    for h in range(m):
        print(arr[k][h], end=' ')
    print()