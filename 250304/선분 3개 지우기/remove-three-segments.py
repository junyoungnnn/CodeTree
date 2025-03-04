n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
left = [i[0] for i in arr]
right = [i[1] for i in arr]

count = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if i == j or j == k or i == k:
                continue
            
            line = [0] * 101
            flag = False

            for l in range(n):
                if l == i or l == j or l == k:
                    continue
                           
                for g in range(left[l], right[l] + 1):
                    if line[g] == 1:
                        flag = True
                        break

                    line[g] = 1
                
            if flag == False:
                count += 1

print(count)

            