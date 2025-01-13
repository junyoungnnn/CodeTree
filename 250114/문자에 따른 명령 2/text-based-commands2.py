c = input()

x, y = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

dir_num = 0

for i in c:
    if i == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    elif i == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)