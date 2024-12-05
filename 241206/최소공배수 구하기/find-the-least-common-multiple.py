n, m = map(int, input().split())

if n > m:
    n, m = m, n

for i in range(1, n+1):
    if i * m % n == 0:
        print(i * m)
        break