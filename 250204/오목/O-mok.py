board = [list(map(int, input().split())) for _ in range(19)]

n = 19

dxs, dys = [0, 1, 1, 1], [1, 1, 0, -1]

color = 0
win = color

col, row = 0, 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y <n

for i in range(0, n):
    for j in range(0, n):
        if board[i][j] == 0:
            continue
        else:
            color = board[i][j]
            if in_range(i, j+1) and board[i][j+1] == color:
                if in_range(i, j+2) and board[i][j+2] == color:
                    if in_range(i, j+3) and board[i][j+3] == color:
                        if in_range(i, j+4) and board[i][j+4] == color:
                            win = color
                            col = j + 3
                            row = i + 1
            if in_range(i+1, j+1) and board[i+1][j+1] == color:
                if in_range(i+2, j+2) and board[i+2][j+2] == color:
                    if in_range(i+3, j+3) and board[i+3][j+3] == color:
                        if in_range(i+4, j+4) and board[i+4][j+4] == color:
                            win = color
                            col = j + 3
                            row = i + 3
            if in_range(i+1, j) and board[i+1][j] == color:
                if in_range(i+2, j) and board[i+2][j] == color:
                    if in_range(i+3, j) and board[i+3][j] == color:
                        if in_range(i+4, j) and board[i+4][j] == color:
                            win = color
                            col = j + 1
                            row = i + 3
            if in_range(i+1, j-1) and board[i+1][j-1] == color:
                if in_range(i+2, j-2) and board[i+2][j-2] == color:
                    if in_range(i+3, j-3) and board[i+3][j-3] == color:
                        if in_range(i+4, j-4) and board[i+4][j-4] == color:
                            win = color
                            col = j - 1
                            row = i + 3
print(win)
print(row, col)