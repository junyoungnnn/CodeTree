n = int(input())

arr = list(map(int, input().split()))

count = 0

for i in range(1, 51):
    for j in range(n):
        for h in range(j+1, n):
            if arr[j] == arr[h]:
                continue
            if abs(arr[j]-i) == abs(arr[h]-i):
                count += 1

print(count)

