def cal(n1, n2, a, b):
    for j in range(n1):
        if b[0] == a[j]:
            if b[n2 - 1] == a[j + n2 - 1]:
                return True
    return False

n1, n2 = map(int, input().split())

a = input().split()
b = input().split()

if cal(n1, n2, a, b):
    print('Yes')
else:
    print('No')