import sys
ability = list(map(int, input().split()))

min_diff = sys.maxsize

n = 5

for i in range(n):
    for j in range(i+1, n):
        for k in range(n):
            for h in range(k+1, n):
                if i != k and i != h and j != k and j != h:
                    team1 = ability[i] + ability[j]
                    team2 = ability[k] + ability[h]
                    team3 = sum(ability) - team1 - team2

                    if team1 != team2 and team2 != team3 and team2 != team3:
                        diff = max(team1, max(team2, team3)) - min(team1, min(team2, team3))
                        min_diff = min(diff, min_diff)

if min_diff == sys.maxsize:
    min_diff = -1

print(min_diff)

