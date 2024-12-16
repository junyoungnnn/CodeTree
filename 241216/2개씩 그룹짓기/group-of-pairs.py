n = int(input())

arr = list(map(int, input().split()))

arr.sort()

arr2 = []

for i in range(n):
    arr2.append(arr[i] + arr[-i-1])

print(max(arr2))