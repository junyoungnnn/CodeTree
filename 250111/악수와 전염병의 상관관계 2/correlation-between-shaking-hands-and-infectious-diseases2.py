N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Write your code here!
result = [0] * N
handshakes.sort()

for t, x, y in handshakes:
    if K == 0:
        break
    if x == P or y == P:
        result[x-1] = 1
        result[y-1] = 1
        K -= 1

for i in result:
    print(i, end='')