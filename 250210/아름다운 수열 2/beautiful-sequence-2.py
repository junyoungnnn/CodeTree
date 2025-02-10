N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0

for i in range(N - M + 1):
    B_arr = B.copy()
    for j in range(i, i + M):
        if A[j] in B_arr:
            
            B_arr.remove(A[j])
        
        if len(B_arr) == 0:
            count += 1
print(count)