R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

count = 0

color = grid[0][0]

for i in range(1, R-2):
    for j in range(1, C-2):
        for k in range(i+1, R-1):
            for h in range(j+1, C-1):
                if grid[i][j] != color and grid[k][h] == color and grid[R-1][C-1] != color:
                    count += 1

print(count)