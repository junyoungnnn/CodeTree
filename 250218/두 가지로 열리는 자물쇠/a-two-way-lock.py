N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

count = 0

def correct(n, a, b, c, i, j, k):
    if (abs(a-i) <= 2 or abs(a-i) >= N - 2) and (abs(b-j) <= 2 or abs(b-j) >= N - 2) and (abs(c-k) <= 2 or abs(c-k) >= N - 2):
        return True

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if correct(N, a1, b1, c1, i, j, k) or correct(N, a2, b2, c2, i, j, k):
                count += 1

print(count)

