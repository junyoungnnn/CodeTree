n, b = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
s.sort(key = lambda x: (x[0]//2 + x[1]))

maxCount = 0

for i in range(n):
    flag = True
    count = 0
    value = s[i][0] // 2 + s[i][1]

    for j in range(n):
        if i == j:
            continue
        
        count += 1
        
        if value >= b:
            break
        value += s[j][0] + s[j][1]

    maxCount = max(maxCount, count)

print(maxCount)




        