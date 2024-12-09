def absol(n, arr):
    for idx, i in enumerate(arr):
        if i < 0 :
            arr[idx] = abs(i)
    return arr

n = int(input())

arr = list(map(int, input().split()))

arr = absol(n, arr)

for i in arr:
    print(i, end=' ')
