n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]

arr[0][0] = 1

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

x, y = 0, 0

d = 2

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

for i in range(2, n * m + 1):
    nx, ny = x + dxs[d], y+dys[d]
    if in_range(nx, ny) and arr[nx][ny] == 0:
        arr[nx][ny] = i
    else:
        d = (d - 1) % 4
        nx, ny = x + dxs[d], y+dys[d]
        arr[nx][ny] = i
    x, y = nx, ny


for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()
    
