n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_value = 0

for i in range(n-k):
    value = 0
    for j in range(i, i+k):
        value += arr[j]
    max_value = max(value, max_value)

print(max_value)
