import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

min_dist = sys.maxsize

for i in range(1, n-1):
    distance = 0
    copyX = x.copy()
    copyX[i] = copyX[i-1]
    copyY = y.copy()
    copyY[i] = copyY[i-1]
    for j in range(0, n-1):
        distance += abs(copyX[j] - copyX[j+1]) + abs(copyY[j] - copyY[j+1])
    min_dist = min(min_dist, distance)
print(min_dist)