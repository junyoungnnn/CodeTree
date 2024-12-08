def cal():
    for j in range(n1):
        if b[0] == a[j]:
            if b[n2 - 1] == a[j + n2 - 1]:
                return True
    return False

n1, n2 = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

if cal():
    print('Yes')
else:
    print('No')