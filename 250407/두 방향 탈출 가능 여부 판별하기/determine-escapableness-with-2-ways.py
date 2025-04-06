N, M = map(int, input().split())
gr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0 for i in range(M)] for _ in range(N)]

row = [1, 0]
col = [0, 1]

answer = 0

def dfs(r, c):
    global answer
    
    if r == N-1 and c == M-1:
        answer = 1
        return

    for i in range(2):
        nr = r + row[i]
        nc = c + col[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if visited[nr][nc] == 1:
            continue
        if gr[nr][nc] == 1:
            visited[nr][nc] = 1
            dfs(nr, nc)

visited[0][0] = 1
dfs(0, 0)

print(answer)