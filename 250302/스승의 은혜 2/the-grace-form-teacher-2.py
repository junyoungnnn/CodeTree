n, b = tuple(map(int, input().split()))
p = [int(input()) for _ in range(n)]

maxCount = 0

for i in range(n):
    count = 0
    sumValue = p[i] // 2
    for j in range(n):
        if i == j:
            continue
        if sumValue <= b:
            count += 1
        else:
            break
        sumValue += p[j]
    maxCount = max(maxCount, count)

print(maxCount)

        
