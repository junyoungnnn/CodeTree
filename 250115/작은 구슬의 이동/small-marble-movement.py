n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

arr = [[0] * n for _ in range(n)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

directrion = {}
directrion['U'] = 0
directrion['R'] = 1
directrion['D'] = 2
directrion['L'] = 3

def in_range(x, y):
    return 1 <= x and x < n and 1 <= y and y < n

for i in range(t):
    r += dy[directrion[d]]
    c += dx[directrion[d]]
    if not in_range(r, c):
        directrion[d] = (2 + directrion[d]) % 4
        r += dy[directrion[d]]
        c += dx[directrion[d]]
    
print(r, c)


