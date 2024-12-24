binary = list(map(int, input()))

num = 0

for i in binary:
    num = num * 2 + i

num *= 17

arr = []

while True:
    if num < 2:
        arr.append(num)
        break
    arr.append(num % 2)
    num //= 2

for i in arr[::-1]:
    print(i, end='')