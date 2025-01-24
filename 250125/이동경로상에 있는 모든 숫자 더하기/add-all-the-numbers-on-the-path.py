N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

x, y = N // 2, N // 2

dxs, dys= [-1, 0, 1, 0], [0, 1, 0, -1]

d = 0

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N

sumValue = board[x][y]

for i in range(T):
    if str[i] == 'R':
        d = (d + 1) % 4
    elif str[i] == 'L':
        d = (d - 1) % 4
    elif str[i] == 'F':
        nx, ny = x + dxs[d], y + dys[d]
        if in_range(nx, ny):
            x, y = x + dxs[d], y + dys[d]
            sumValue += board[x][y]

print(sumValue)