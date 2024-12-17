class CodeName():
    def __init__(self, code, score):
        self.code = code
        self.score = score

users = []

for _ in range(5):
    code, score = input().split()
    score = int(score)
    users.append(CodeName(code, score))

minScore = users[0].score
minScoreUser = users[0].code

for i in range(5):
    if users[i].score < minScore:
        minScore = users[i].score
        minScoreUser = users[i].code

print(minScoreUser, minScore)