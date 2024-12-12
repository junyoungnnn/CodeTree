def f(n, arr, maxValue):
    if n == 0:
        return max(arr[n], maxValue)
    return f(n-1, arr, max(arr[n-1], maxValue))



n = int(input())

arr = list(map(int, input().split()))

print(f(n, arr, arr[n-1]))