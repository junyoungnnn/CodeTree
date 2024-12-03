n, m = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(m):
    sum = 0
    a, b = map(int, input().split())
    for j in range(a - 1, b):
        sum += arr[j]
    print(sum)