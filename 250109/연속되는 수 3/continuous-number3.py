N = int(input())
arr = [int(input()) for _ in range(N)]

count = 0
max_count = 0
for i in range(N):
    if i == 0 or arr[i] > 0 and arr[i-1] > 0 or arr[i] < 0 and arr[i-1] < 0:
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 1
else:
    if count > max_count:
        max_count = count
print(max_count)