m1, d1, m2, d2 = map(int, input().split())

input_day = input()

month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

elapsed_days1 = 0
elapsed_days2 = 0

elapsed_days1 = sum(month[:m1]) + d1 - 1
elapsed_days2 = sum(month[:m2]) + d2 - 1

start_day_idx = 0
day1_idx = (start_day_idx + elapsed_days1) % 7
day2_idx = (start_day_idx + elapsed_days2) % 7

target_day_idx = day.index(input_day)

count = 0
for days in range(elapsed_days1, elapsed_days2 + 1):
    if (start_day_idx + days) % 7 == target_day_idx:
        count += 1

print(count)