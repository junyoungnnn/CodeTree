n = int(input())
numbers = list(map(int, input().split()))

max_num = 0

for i in range(n):
    for j in range(n):
        num = numbers[i]
        if i == j or i == j-1 or i == j + 1:
            continue
        else:
            num += numbers[j]
        max_num = max(max_num, num)

print(max_num)

