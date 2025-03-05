X, Y = map(int, input().split())

maxValue = 0

for i in range(X, Y+1):
    value = 0
    while i > 0:
        value += i % 10
        i //= 10
    maxValue = max(maxValue, value)

print(maxValue) 