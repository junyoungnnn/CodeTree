def callendar(M, D):
    month30 = [4, 6, 9, 11]

    if D > 31:
        return False
    elif M == 2 and D > 28:
        return False
    elif D > 30 and M in month30:
        return False
    return True

M, D = map(int, input().split())

if callendar(M, D):
    print("Yes")
else:
    print("No")