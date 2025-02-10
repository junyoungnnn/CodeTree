N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

arr = [0] * 102

for u, h in zip(candy, pos):
    arr[h] += u

max_candy = 0

for i in range(101):
    value = 0
    for j in range(i-K, i+K+1):
        if j < 0 or j > 101:
            continue

        value += arr[j]
    max_candy = max(max_candy, value)

print(max_candy)



57
83
82
7
39
23
97
44
68
82
27
0
36
69
95
80
23
92
84
89