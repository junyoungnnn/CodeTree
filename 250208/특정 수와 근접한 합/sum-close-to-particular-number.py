N, S = map(int, input().split())
arr = list(map(int, input().split()))

min_diff = 10000
for i in range(N-1):
    for j in range(i+1, N):
        sum_value = sum(arr)
        sum_value += -arr[i] -arr[j]
        min_diff = min(min_diff, abs(S - sum_value))

print(min_diff)

