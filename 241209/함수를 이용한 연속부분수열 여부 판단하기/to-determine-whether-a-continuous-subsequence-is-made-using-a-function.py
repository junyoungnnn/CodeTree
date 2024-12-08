def cal():
    for i in b:
        if i not in a:
            return False
    return True

n1, n2 = map(int, input().split())

a = input().split()
b = input().split()

if cal():
    print('Yes')
else:
    print('No')