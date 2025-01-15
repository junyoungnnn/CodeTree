n = int(input())
moves = [input().split() for _ in range(n)]
direction = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]
 
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
 
d = {
    'N' : 0,
    'E' : 1,
    'S' : 2,
    'W' : 3
}
 
x, y = 0, 0
count = 0

for i in range(n):
    for j in range(dist[i]):
        nx, ny = x + dxs[d[direction[i]]], y + dys[d[direction[i]]]
        x, y = nx, ny
        count += 1
        if x == 0 and y == 0:
            break
    if x == 0 and y == 0:
        print(count)
        break
else:
    print(-1)

