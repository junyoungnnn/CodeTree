n = int(input())

data = [0] * n
arr = []

for i in range(n):
    arr.append(data.copy())

count = 0

for i in range(n-1, -1, -1):
    if i % 2 == 1:
        for j in range(n-1, -1, -1):
            count = count + 1
            arr[j][i] = count
    else:
        for j in range(n):
            count = count + 1
            arr[j][i] = count

for k in range(n):
    for h in range(n):
        print(arr[k][h], end=' ')
    print()

