def sumNum(n):
    if n == 1:
        return 1

    return sumNum(n-1) + n

n = int(input())

print(sumNum(n))