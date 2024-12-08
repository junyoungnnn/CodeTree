def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sumAll(n):
    sum = 0
    while(n != 0):
        sum += n % 10
        n //= 10
    if sum % 2 == 0:
        return True
    return False

a, b = map(int, input().split())

count = 0

for i in range(a, b+1):
    if isPrime(i) and sumAll(i):
        count += 1

print(count)