n = int(input())

A = []
B = []
C = []
arr = [0] * 4
index = 0
maxCount = 0

for i in range(n):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

for i in range(1, n+1):
    arr[i] = 1
    count = 0
    for j in range(n):
        arr[A[j]], arr[B[j]] = arr[B[j]], arr[A[j]]
        if arr[C[j]] == 1:
            count += 1
    if maxCount < count:
        maxCount = count
        index = i

print(index)




