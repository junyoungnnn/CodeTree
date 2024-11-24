n = int(input())

data = [1] * n
arr = []

for i in range(n):
    arr.append(data.copy())

for i in range(1, n):
    for j in range(1, n):
        arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j] + arr[i][j - 1]

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()