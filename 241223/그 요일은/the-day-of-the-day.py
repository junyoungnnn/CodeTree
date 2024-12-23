m1, d1, m2, d2 = map(int, input().split())

input_day = input()

month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

elapsed_days1 = 0
elapsed_days2 = 0

for i in range(1, m1):
    elapsed_days1 += month[i]
elapsed_days1 += d1 -1

for i in range(1, m2):
    elapsed_days2 += month[i]
elapsed_days2 += d2 -1

# print('날짜차이: ', elapsed_days2 - elapsed_days1)
# print('elapsed_days1', elapsed_days1)
# print('elapsed_days2', elapsed_days2)
count = 0
for i in range(elapsed_days2- elapsed_days1 + 1):
    if i % 7 == day.index(input_day):
        count += 1

print(count)