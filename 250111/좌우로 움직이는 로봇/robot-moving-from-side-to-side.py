n, m = map(int, input().split())

t_a = []
d_a = []

for _ in range(n):
    time, direction = input().split()
    t_a.append(int(time))
    d_a.append(direction)

t_b = []
d_b = []

for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

A = []
B = []

sum1 = 0
sum2 = 0
for i in range(n):
    for j in range(t_a[i]):
        if d_a[i] == 'L':
            sum1 -= 1
            A.append(sum1)
        else:
            sum1 += 1
            A.append(sum1)

for i in range(m):
    for j in range(t_b[i]):
        if d_b[i] == 'L':
            sum2 -= 1
            B.append(sum2)
        else:
            sum2 += 1
            B.append(sum2)

count = 0
for i in range(1, min(len(A), len(B))):
    if A[i] == B[i] and A[i-1] != B[i-1]:
        count += 1
end = min(len(A), len(B))

if end > len(A) - 1:
    for k in range(end, max(len(A), len(B))):
        if A[end - 1] == B[k] and A[end - 2] != B[k-1]:
            count += 1
elif end < len(A) - 1:
    for k in range(end, max(len(A), len(B))):
        if B[end - 1] == A[k] and B[end - 2] != A[k-1]:
            count += 1
        
print(count)