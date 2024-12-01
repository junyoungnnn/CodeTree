n = int(input())

sum = 0

for i in range(n):
    sum += int(input())

sum = str(sum)

s = sum[0]
sum = sum.replace(s, '', 1)
sum += s

print(sum)