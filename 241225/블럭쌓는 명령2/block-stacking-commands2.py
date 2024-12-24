n, k = map(int, input().split())

for i in range(k):
    arr = [0] * n
    count = 0
    maxValue = 0
    a, b = map(int, input().split())
    for j in range(a, b + 1):
        arr[j] = 1
    for i in arr:
        if i == 1:
            count += 1
    if count > maxValue:
        maxValue = count
    
print(maxValue)

