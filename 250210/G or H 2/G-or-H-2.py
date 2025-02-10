n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

arr = [0] * 101

for i, j in zip(pos, alpha):
    arr[i] = j

max_dist = 0

for i in range(1, 101):
    if arr[i] != 0:
        count_H = 0
        count_G = 0
        for j in range(i, 101):
            if arr[j] != 0:
                
                dist = 0
                if arr[j] == 'H':
                    count_H += 1
                elif arr[j] == 'G':
                    count_G += 1

                if count_H != 0 and count_G == count_H:
                    dist = j - i
                elif count_H != 0 and count_G == 0:
                    dist = j - i
                elif count_G != 0 and count_H == 0:
                    dist = j - i
                max_dist = max(max_dist, dist)
            
if n == 1:
    max_dist = 0

print(max_dist)
