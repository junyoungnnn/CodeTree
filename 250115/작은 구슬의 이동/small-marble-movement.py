n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

arr = [[0] * n for _ in range(n)]

dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]

directrion = {}
directrion['R'] = 0
directrion['U'] = 1
directrion['D'] = 2
directrion['L'] = 3

def in_range(x, y):
    return 0 < x and x <= n and 0 < y and y <= n

for i in range(t):
    nx, ny = r + dx[directrion[d]], c + dy[directrion[d]]

    if not in_range(nx, ny):
        directrion[d] = 3 - directrion[d]
    else:
        r += dx[directrion[d]]
        c += dy[directrion[d]]

print(r, c)


