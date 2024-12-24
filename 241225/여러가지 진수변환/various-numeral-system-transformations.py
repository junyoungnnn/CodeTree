n, B = map(int, input().split())

arr = []

if B == 4:
    while True:
        if n < 4:
            arr.append(n)
            break

        arr.append(n%4)
        n //= 4
else:
    while True:
        if n < 8:
            arr.append(n)
            break

        arr.append(n % 8)
        n //= 8

for i in arr[::-1]:
    print(i, end='')
