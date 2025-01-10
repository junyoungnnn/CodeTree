N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Write your code here!
result = [0] * N
count = [K] * N
handshakes.sort()

result[P-1] = 1

for t, x, y in handshakes:
    if (count[x-1] > 0 and result[x-1] == 1) or (count[y-1] > 0 and result[y-1] == 1):
        result[x-1] = 1
        result[y-1] = 1
        count[x-1] -= 1
        count[y-1] -= 1

for i in result:
    print(i, end='')