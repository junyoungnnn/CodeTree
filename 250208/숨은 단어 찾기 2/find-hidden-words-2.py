N, M = map(int, input().split())
arr = [input() for _ in range(N)]

dxs, dys = [1, 0, -1, -1, -1, 0, 1, 1], [1, 1, 1, 0, -1, -1, -1, 0]

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < M

count = 0

for i in range(N):
    for j in range(M):

        if arr[i][j] != 'L':
            continue
		
        for dx, dy in zip(dxs, dys):
            curx = i
            cury = j
            curt = 0
            while True:
                nx = curx + dx
                ny = cury + dy

                if in_range(nx, ny) == False:
                    break
                
                if arr[nx][ny] != 'E':
                    break
                else:
                    curx = nx
                    cury = ny
                    curt += 1
                if curt >= 2:
                    count += 1
                    break
print(count)