n, t = map(int, input().split())
arr = list(map(int, input().split()))

count, ans = 0, 0
for i in range(n):
    if arr[i] > t:
        count += 1
    else:
        ans = max(count, ans)
        count = 0

print(ans) 
