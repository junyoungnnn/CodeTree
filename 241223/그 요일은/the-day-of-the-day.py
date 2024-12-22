m1, d1, m2, d2 = map(int, input().split())

input_day = input()

month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

elapsed_days1 = 0
elapsed_days2 = 0

for i in range(1, m1):
    elapsed_days1 += month[i]
elapsed_days1 += d1

for i in range(1, m2):
    elapsed_days2 += month[i]
elapsed_days2 += d2

count = (elapsed_days2 - elapsed_days1 + 2) // 7

if day[(elapsed_days2 - elapsed_days1) % 7] == input_day:
    count += 1

print(count)