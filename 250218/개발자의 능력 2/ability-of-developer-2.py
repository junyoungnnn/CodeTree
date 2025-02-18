import sys
ability = list(map(int, input().split()))

min_diff = sys.maxsize

n = 6

for i in range(n):
    for j in range(n):
        for k in range(n):
            for h in range(n):
                if i != k and j != h and i != h and j != k and i != j and k != h:
                    team1 = ability[i] + ability[j]
                    team2 = ability[k] + ability[h]
                    team3 = sum(ability) - team1 - team2

                    diff = max(team1, max(team2, team3)) - min(team1, min(team2, team3))

                    min_diff = min(diff, min_diff)


print(min_diff)
