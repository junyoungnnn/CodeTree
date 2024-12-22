m1, d1, m2, d2 = map(int, input().split())

day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

elapsed_days1 = 0
elapsed_days2 = 0

for i in range(1, m1):
    elapsed_days1 += month[i]
elapsed_days1 += d1

for i in range(1, m2):
    elapsed_days2 += month[i]
elapsed_days2 += d2

print(day[(elapsed_days2 - elapsed_days1 + 1) % 7])
