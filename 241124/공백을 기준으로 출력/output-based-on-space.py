arr = []

for i in range(2):
    arr.append(input().split())

for i in range(2):
    for j in range(len(arr[i])):
        print(arr[i][j], end='')