n, b = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
s.sort(key = lambda x: [(x[0]//2 + x[1])])
t = s[:]
t.sort(key = lambda x: [(x[0] + x[1])])
maxCount = 0

for i in range(n):
    count = 1
    value = s[i][0] // 2 + s[i][1]
    left = s[i][0]
    right = s[i][1]

    for j in range(n):
        if left == t[j][0] and right == t[j][1]:
            continue
        else:
            value += t[j][0] + t[j][1]

        if value <= b:
            count += 1
        else:
            break

    maxCount = max(maxCount, count)

print(maxCount)