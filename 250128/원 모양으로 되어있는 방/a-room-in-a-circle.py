import sys

n = int(input())
a = [int(input()) for _ in range(n)]

distance = sys.maxsize

for i in range(n):
    dist = 0
    for j in range(i, n + i):
        if i == j:
            continue
        else:
            dist += a[j %n] * (j-i)

    distance = min(distance, dist)

print(distance)