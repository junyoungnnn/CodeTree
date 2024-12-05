def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

n, m = map(int, input().split())

print(lcm(n, m))