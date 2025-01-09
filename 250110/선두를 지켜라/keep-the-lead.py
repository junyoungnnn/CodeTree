N, M = map(int, input().split())

v1 = []
t1= []

v2 = []
t2 = []

for _ in range(N):
    v, t = map(int, input().split())
    v1.append(v)
    t1.append(t)

for _ in range(M):
    v, t = map(int, input().split())
    v2.append(v)
    t2.append(t)

A = []
B = []

sum1, sum2 = 0, 0

for i in range(N):
    for j in range(t1[i]):
        sum1 += v1[i]
        A.append(sum1)

for i in range(M):
    for j in range(t2[i]):
        sum2 += v2[i]
        B.append(sum2)

count = 0
first = 'A' if A[0] >= B[0] else 'B'
for i in range(len(A)):
    if first == 'A' and A[i] < B[i]:
        count += 1
        first = 'B'
    elif first == 'B' and A[i] > B[i]:
        count += 1
        first = 'A'

print(count)


