def printNum(i, n):
    print(i, end=' ')
    if i == n:
        print()
        print(i, end=' ')
        return
    printNum(i + 1, n)
    print(i, end=' ')

n = int(input())
i = 1

printNum(i, n)