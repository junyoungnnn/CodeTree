Y, M, D = map(int, input().split())

M30 = [4, 6, 9, 11]

if M == 2 and D == 29:
    if Y % 4 == 0:
        if Y % 400 == 0:
            print('Winter')
        elif Y % 100 == 0:
            print(-1)
        else:
            print('Winter')
    else:
        print(-1)
elif M == 2 and D > 29:
    print(-1)
elif M in M30 and D > 30:
    print(-1)
elif M in [3, 4, 5]:
    print('Spring')
elif M in [6, 7, 8]:
    print('Summer')
elif M in [9, 10, 11]:
    print('Fall')
elif M in [12, 1, 2]:
    print('Winter')
