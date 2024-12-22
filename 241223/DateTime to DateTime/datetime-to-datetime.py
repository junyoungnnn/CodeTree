a, b, c = map(int, input().split())

total_min = (a- 11) * 24 * 60 + b * 60 + c

std_min = 11 * 60 + 11

if total_min - std_min >= 0:
    print(total_min - std_min)
else:
    print(-1)