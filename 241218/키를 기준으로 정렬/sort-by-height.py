class People():
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())

arr = [input().split() for _ in range(n)]

people = [People(name, int(height), int(weight)) for name, height, weight in arr]

people.sort(key=lambda x: x.height)

for i in range(n):
    print(f'{people[i].name} {people[i].height} {people[i].weight}')