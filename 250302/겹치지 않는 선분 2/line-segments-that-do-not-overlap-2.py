n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [l[0] for l in lines]
x2 = [l[1] for l in lines]

count = 0

for i in range(n):
    flag = False
    for j in range(n):
        if i == j:
            continue
        if x1[i] <= x1[j] and x2[i] >= x2[j] or x1[j] <= x1[i] and x2[j] >= x2[i]:
            flag = True

    if flag == False:
        count += 1
    
print(count)
