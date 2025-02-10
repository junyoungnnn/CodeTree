N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

arr = [0] * 101

for u, h in zip(candy, pos):
    arr[h] = u

max_candy = 0

for i in range(K, 101-K):
    value = 0
    for j in range(i-K, i+K+1):
        value += arr[j]
    max_candy = max(max_candy, value)

print(max_candy)



