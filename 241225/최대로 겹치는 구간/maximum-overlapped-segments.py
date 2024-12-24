n = int(input())

arr = [0] * 201

for i in range(n):
    a, b = map(int, input().split())
    for i in range(a+101, b+101):
        arr[i] += 1

print(max(arr))

