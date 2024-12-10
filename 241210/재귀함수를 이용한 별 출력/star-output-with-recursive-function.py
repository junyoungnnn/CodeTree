def printStar(n):
    if n == 0:
        return
    printStar(n-1)
    print('*' * n)

n = int(input())

printStar(n)
