n = int(input())

arr = list(map(int, input().split()))

for i in range(1, n+1):
    if i % 2 == 1:
        arr2 = arr[0:i]
        arr2 = sorted(arr2)
        print(arr2[i//2], end=' ')