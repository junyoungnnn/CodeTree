n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]



maxCount = 0

for i in range(n):
    work = [0] * 1001
    for j in range(n):
        if i == j:
            continue
        for k in range(a[j], b[j]):
            work[k] = 1

    count = 0
    for h in work:
        if h == 1:
            count += 1
    maxCount = max(maxCount, count)

print(maxCount)

