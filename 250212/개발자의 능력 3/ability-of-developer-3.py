import sys
abilities = list(map(int, input().split()))

min_diff = sys.maxsize
sum_value = sum(abilities)

for i in range(len(abilities)-2):
    for j in range(i+1, len(abilities)-1):
        for k in range(j + 1, len(abilities)):
            sum1 = abilities[i] + abilities[j] + abilities[k]
            sum2 = sum_value - sum1
            min_diff = min(min_diff, abs(sum1 - sum2))

print(min_diff)

