n, m = map(int, input().split())

arr = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]

for i in range(m):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1
    cnt = 0
    for j in range(4):
        nx, ny = r - 1 + dxs[j], c - 1 + dys[j]
        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)