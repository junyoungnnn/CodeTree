n , k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

maxValue = -1

for i in range(n):
    for j in range(i+1, i+k+1):
        if j < n and arr[i] == arr[j]:
            maxValue = max(maxValue, arr[j])

print(maxValue)