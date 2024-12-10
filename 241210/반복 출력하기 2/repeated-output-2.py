def printHello(n):
    if n == 0:
        return
    print('HelloWorld')
    printHello(n - 1)
    

n = int(input())

printHello(n)