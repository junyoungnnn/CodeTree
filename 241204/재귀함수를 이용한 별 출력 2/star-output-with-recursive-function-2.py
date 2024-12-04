n = int(input())

def recur(n):
    if n == 0:
        return 0
    print((n + 1 - 1) * '* ')
    recur(n-1)
    print((n + 1 - 1) * '* ')
   

recur(n)