A, B, C = map(int, input().split())

maxValue = 0

for i in range(1001):
    value = 0
    a = A
    a *= i
    if a > C:
        break
    if a == C:
        value = a
    for j in range(1001):
        b = B
        b *= j
        if a + b > C:
            break
        value = a + b
        maxValue = max(maxValue, value)

print(maxValue)