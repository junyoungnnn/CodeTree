n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

maxArea = 0

def line(a, b, c):
    linex, liney = 0, 0
    if x[a] == x[b]:
        liney = abs(y[a] - y[b])
    elif x[b] == x[c]:
        liney = abs(y[b] - y[c])
    elif x[a] == x[c]:
        liney = abs(y[a] - y[c])

    if y[a] == y[b]:
        linex = abs(x[a] - x[b])
    elif y[b] == y[c]:
        linex = abs(x[b] - x[c])
    elif y[a] == y[c]:
        linex = abs(x[a] - x[c])

    return linex, liney



for i in range(0, n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            lineX, lineY = 0, 0
            lineX, lineY = line(i,j,k)
            maxArea = max(maxArea, lineX *lineY)

print(maxArea)

