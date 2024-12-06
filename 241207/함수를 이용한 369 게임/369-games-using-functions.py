def is3or6or9(n):
    while n != 0:
        if n % 10 == 3 or n % 10 == 6 or n % 10 == 9:
            return True
        n //= 10
    return False
        

def is3div(n):
    if n % 3 == 0:
        return True
    return False

def cal(a, b):
    count = 0
    for i in range(a, b+1):
        if is3or6or9(i) or is3div(i):
            count += 1
    return count

a, b = map(int, input().split())

print(cal(a, b))