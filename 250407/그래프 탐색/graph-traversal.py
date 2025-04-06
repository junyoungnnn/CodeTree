N, M = map(int, input().split())

gr = [[] for _ in range(N+1)]

visited = [0 for _ in range(N+1)]

cnt = 0

def dfs(vertex):
    global cnt

    for curr in gr[vertex]:

        if not visited[curr]:
            visited[curr] = 1
            cnt += 1
            dfs(curr)

for i in range(M):
    v1, v2 = map(int, input().split())

    gr[v1].append(v2)
    gr[v2].append(v1)

visited[1] = 1
dfs(1)

print(cnt)