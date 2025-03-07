n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

maxCount = 0
maxValue = max(arr)

for i in range(1, maxValue):
    count = 1
    for j in range(n-1):
        if arr[j] > i and arr[j+1] <= i:
            count += 1
            
    maxCount = max(maxCount, count)

print(maxCount)

