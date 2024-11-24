n, m = map(int, input().split())

data = [0] * n
arr = []

for i in range(n):
    arr.append(data.copy())

for i in range(m):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = x * y

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()