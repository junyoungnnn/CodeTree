def callendar(Y, M, D):

    M30 = [4, 6, 9, 11]

    if M == 2 and D == 29:
        if Y % 4 == 0:
            if Y % 400 == 0:
                return 'Winter'
            elif Y % 100 == 0:
                return -1
            else:
                return 'Winter'
        else:
            return -1
    elif M == 2 and D > 29:
        return -1
    elif M in M30 and D > 30:
        return -1
    elif M in [3, 4, 5]:
        return 'Spring'
    elif M in [6, 7, 8]:
        return 'Summer'
    elif M in [9, 10, 11]:
        return 'Fall'
    elif M in [12, 1, 2]:
        return 'Winter'


Y, M, D = map(int, input().split())

season = callendar(Y, M, D)
print(season)


