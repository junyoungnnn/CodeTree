def alpha2(s):
    s = set(s)
    if len(s) > 1:
        return True
    return False

s = list(input())

if alpha2(s):
    print('Yes')
else:
    print('No')