def f(n):
    if n == 0:
        return 0
    return n % 10 + f(n//10)

a, b, c = map(int, input().split())

print(f(a * b * c))