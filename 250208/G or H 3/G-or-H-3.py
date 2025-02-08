n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

placed = [0] * 10000

max_score = 0

for i in range(n):
    placed[x[i]] = c[i]

for i in range(1, 20-k+1):
    score = 0
    for j in range(i, i+k+1):
        if placed[j] == 'G':
            score += 1
        elif placed[j] == 'H':
            score += 2
    max_score = max(max_score, score)
        
print(max_score)
