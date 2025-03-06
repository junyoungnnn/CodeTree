n, c, g, h = map(int, input().split())

ta, tb = [0] * n, [0] * n

for i in range(n):
    ta[i], tb[i] = map(int, input().split())


def temp(k, ta, tb):
    if k < ta:
        return c
    elif k >= ta and k <= tb:
        return g
    elif k > tb:
        return h

maxResult = 0

for k in range(0, 1001):
    result = 0
    for i in range(n):
        result += temp(k, ta[i], tb[i])
    maxResult = max(maxResult, result)

print(maxResult)



