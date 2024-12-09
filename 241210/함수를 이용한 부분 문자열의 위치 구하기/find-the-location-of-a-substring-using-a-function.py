s = input()

s2 = input()

def findS():
    if s2 in s:
        idx = s.find(s2)
    else:
        idx = -1
    return idx

print(findS())
