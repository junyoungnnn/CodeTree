X, Y = map(int, input().split())

count = 0

for i in range(X, Y+1):
    arr = (list(map(int, str(i))))
    arr.sort()
    change = 0
    for j in range(len(arr) - 1):
        if arr[j] != arr[j+1]:
            change += 1
        
    if change == 1:
        flag = 0
        if arr[0] == arr[1]:
            flag += 1
        if arr[-1] == arr[-2]:
            flag += 1
        if flag == 1:
            count += 1

print(count)
