n, m = map(int, input().split())

arr1 = []
arr2 = []

for i in range(n):
    data = list(map(int, input().split()))
    arr1.append(data)
for i in range(n):
    data = list(map(int, input().split()))
    arr2.append(data)

r = [1] * m
result = []

for h in range(n):
    result.append(r.copy())

for k in range(n):
    for j in range(m):
        if arr1[k][j] == arr2[k][j]:
            result[k][j] = 0

for q in range(n):
    for w in range(m):
        print(result[q][w], end=' ')
    print()