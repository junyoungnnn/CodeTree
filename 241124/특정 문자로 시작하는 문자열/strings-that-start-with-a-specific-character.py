n = int(input())

arr = []

for i in range(n):
    arr.append(input())

alpha = input()

count = 0
sum = 0

for i in range(n):
    if arr[i][0] == alpha:
        count += 1
        sum += len(arr[i])

print(f'{count} {sum/count:.2f}')