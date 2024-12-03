a, b = map(int, input().split())

def cel(a, b):
    if a > b : a, b = b, a
    a += 10
    b *= 2
    return a, b

A, B = cel(a, b)

print(A, B)