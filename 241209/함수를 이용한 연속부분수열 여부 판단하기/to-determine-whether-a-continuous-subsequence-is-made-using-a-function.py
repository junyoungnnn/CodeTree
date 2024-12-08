def cal(n1, n2, a, b):
    for i in range(n2):
        for j in range(n1):
            if b[i] == a[j]:
                if b[i + n2 - 1] == a[j + n2 - 1]:
                    return True
                else:
                    return False

n1, n2 = map(int, input().split())

a = input().split()
b = input().split()

if cal(n1, n2, a, b):
    print('Yes')
else:
    print('No')