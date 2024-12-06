def print_min(a, b, c):
    return min(a, min(b, c))

a, b, c = map(int, input().split())

print(print_min(a, b, c))