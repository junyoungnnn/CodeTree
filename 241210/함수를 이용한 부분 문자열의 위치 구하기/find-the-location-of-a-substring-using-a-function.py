s = input()

s2 = input()

def findS():
    if s.find(s2):
        idx = s.find(s2)
    else:
        idx = -1
    return idx

print(findS())
