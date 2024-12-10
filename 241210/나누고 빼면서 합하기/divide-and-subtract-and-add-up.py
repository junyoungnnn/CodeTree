n, m = map(int, input().split())

a = list(map(int, input().split()))

score = 0

def minus():
    global n, m, a, score
    while m != 0:
        score += a[m-1]
        if m % 2 == 1:
            m -= 1
        else:
            m //= 2

minus()

print(score)