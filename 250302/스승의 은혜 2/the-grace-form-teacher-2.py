n, b = tuple(map(int, input().split()))
p = [int(input()) for _ in range(n)]

maxCount = 0

p.sort()

for i in range(n):
    count = 0
    sumValue = 0
    for j in range(n):
        if i == j:
            sumValue += p[i] // 2
        else:
            sumValue += p[j]
        if sumValue <= b:
            count += 1
        else:
            break
        
    maxCount = max(maxCount, count)

print(maxCount)

        
