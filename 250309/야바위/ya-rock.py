n = int(input())

A = []
B = []
C = []

maxCount = 0

for i in range(n):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

for i in range(1, 4):
    arr = [0] * 4
    arr[i] = 1
    count = 0
    for j in range(n):
        arr[A[j]], arr[B[j]] = arr[B[j]], arr[A[j]]
        if arr[C[j]] == 1:
            count += 1
    maxCount = max(maxCount, count)

print(maxCount)



