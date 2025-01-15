s = input()

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

x, y = 0, 0
d = 0
count = 0

for i in s:
    if i == 'R':
        d = (d + 1) % 4
    elif i == 'L':
        d = (d - 1) % 4
    else:
        x, y = x + dxs[d], y + dys[d]
    count += 1
    if x == 0 and y == 0:
        print(count)
        break
else:
    print(-1)