n = int(input())
arr = list(map(int, input().split()))

result = []

for i in range(n):
    for j in range(i, n):
        avg_arr = []
        for k in range(i, j + 1):
            avg_arr.append(k)
        
        avg_value = sum(avg_arr) / len(avg_arr)
        
        if avg_value in avg_arr:
            result.append(avg_value)

print(len(result))

