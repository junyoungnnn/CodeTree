n, k, T = input().split()

n, k = int(n), int(k)

arr = []

for i in range(n):
    data = input()
    if data.find(T) == 0:
        arr.append(data)

arr = sorted(arr)

print(arr[k-1])