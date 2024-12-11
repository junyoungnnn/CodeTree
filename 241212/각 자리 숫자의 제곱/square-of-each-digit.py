def f(n):
    if n == 0:
        return 0
    return (n % 10) ** 2 + f(n//10)

n = int(input())

print(f(n))