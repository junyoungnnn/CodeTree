n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

max_sum = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == k:
                for h in range(j+2, n):
                    if in_range(i, j+2) and in_range(k, h+2):
                        sum_value = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[k][h] + arr[k][h+1] + arr[k][h+2]
                        max_sum = max(max_sum, sum_value)
            else:
                for h in range(j, n):
                    if in_range(i, j+2) and in_range(k, h+2):
                        sum_value = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[k][h] + arr[k][h+1] + arr[k][h+2]
                        max_sum = max(max_sum, sum_value)

print(max_sum)
