import sys
n = int(input())

arr = list(map(int, input().split()))

diff = sys.maxsize

for i in range(n):
    arr[i] *= 2

    for j in range(n):
        remain_arr = []
        for k in range(n):
            if j != k:
                remain_arr.append(arr[k])

        sum_diff = 0

        for h in range(len(remain_arr)-1):
            sum_diff += abs(remain_arr[h]-remain_arr[h+1])

        diff = min(diff, sum_diff)
    arr[i] //= 2

print(diff)

