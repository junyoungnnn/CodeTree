def trans1(binary, A):
    num = 0
    for i in binary:
        num = num * A + i
    return num

def trans2(n, B):
    arr = []
    while True:
        if n < B:
            arr.append(n)
            break
        arr.append(n % B)
        n //= B
    return arr

a, b = map(int, input().split())
n = list(map(int, input()))

num = trans1(n, a)
result = trans2(num, b)

for i in result[::-1]:
    print(i, end='')