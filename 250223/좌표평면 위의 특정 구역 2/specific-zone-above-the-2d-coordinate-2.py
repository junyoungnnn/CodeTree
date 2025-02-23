import sys

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

minSize = sys.maxsize

for i in range(n):
    minX, maxX, minY, maxY = sys.maxsize, 0, sys.maxsize, 0

    for j in range(n):
        if i == j:
            continue
        
        minX = min(minX, x[j])
        maxX = max(maxX, x[j])
        minY = min(minY, y[j])
        maxY = max(maxY, y[j])

    size = (maxX - minX) * (maxY - minY)
    minSize = min(minSize, size)

print(minSize)

