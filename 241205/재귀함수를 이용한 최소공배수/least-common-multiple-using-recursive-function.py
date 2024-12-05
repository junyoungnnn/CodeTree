def gcd(a, b):
    while(b != 0):
        temp = a % b
        a = b
        b = temp
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def cel(n):
    if n == 1:
        return arr[0]
    return lcm(cel(n-1), arr[n-1])

n = int(input())

arr = list(map(int, input().split()))

print(cel(n))