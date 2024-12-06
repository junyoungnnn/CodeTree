def yoonyear(n):
    if n % 4 != 0:
        return False
    elif n % 400 == 0:
        return True
    elif n % 100 == 0:
        return False
    else:
        return True

y = int(input())

if yoonyear(y):
    print('true')
else:
    print('false')