N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Write your code here!
arr = [0] * N
for i in student:
    arr[i-1] += 1
    if arr[i-1] >= K:
        print(i)
        break
else:
    print(-1)
