n, b = tuple(map(int, input().split()))
p = [int(input()) for _ in range(n)]

maxCount = 0

for i in range(n):
    sumValue = p[i] // 2
    if sumValue <= b:
        count = 1
    else:
        count = 0
    for j in range(n):
        if i == j:
            continue

        sumValue += p[j]
        if sumValue <= b:
            count += 1
        else:
            break
        
    maxCount = max(maxCount, count)

print(maxCount)

        
