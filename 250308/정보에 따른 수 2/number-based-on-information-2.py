T, a, b = map(int, input().split())

S = []
N = []
count = 0

for i in range(T):
    c, x = input().split()
    x = int(x)
    if c == 'S':
        S.append(x)
    else:
        N.append(x)

S.sort()
N.sort()

for i in range(a, b+1):
    min_S = 1000
    min_N = 1000
    for j in S:
        diff_S = abs(j-i)
        min_S = min(min_S, diff_S)

    for k in N:
        diff_N = abs(k-i)
        min_N = min(min_N, diff_N)

    if min_S <= min_N:
        count += 1

print(count)

    

