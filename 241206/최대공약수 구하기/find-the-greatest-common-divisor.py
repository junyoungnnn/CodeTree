def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

a, b = map(int, input().split())

print(gcd(a, b))
