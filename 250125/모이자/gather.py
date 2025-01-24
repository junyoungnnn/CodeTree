import sys

max_dist = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

max_sum = 0

for i in range(n):
    sum_value = 0
    for j in range(n):
        sum_value += abs(i - j) * arr[j]
    if max_dist > sum_value:
        max_dist = sum_value
print(max_dist)

