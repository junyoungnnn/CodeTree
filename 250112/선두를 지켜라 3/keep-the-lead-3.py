N, M = map(int, input().split())

A_V = []
A_T = []
for i in range(N):
    v, t = map(int, input().split())
    A_V.append(v)
    A_T.append(t)

B_V = []
B_T = []
for i in range(M):
    v, t = map(int, input().split())
    B_V.append(v)
    B_T.append(t)

A = []
B = []
sum_A = 0
sum_B = 0

for i in range(N):
    for j in range(A_T[i]):
        sum_A += A_V[i]
        A.append(sum_A)

for i in range(M):
    for j in range(B_T[i]):
        sum_B += B_V[i]
        B.append(sum_B)

count = 1

for i in range(1, len(A)):
    if A[i] > B[i] and A[i-1] <= B[i-1]:
        count += 1
    elif  A[i] < B[i] and A[i-1] >= B[i-1]:
        count += 1
    elif A[i] == B[i] and A[i-1] != B[i-1]:
        count += 1

print(count)