n = int(input())
arr = [int(input()) for _ in range(n)]

count = 1
max_count = 1
for i in range(n):
    if i == 0 or arr[i] != arr[i - 1]:
        if count > max_count:
            max_count = count
        count = 1
    else:
        count += 1
else:
    if count > max_count:
            max_count = count

print(max_count)
