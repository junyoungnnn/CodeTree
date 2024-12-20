class Student():
    def __init__(self, height, weight, number):
        self.height, self.weight = height, weight
        self.number = number

n = int(input())

arr = []

for i in range(1, n+1):
    height, weight = input().split()
    arr.append(Student(int(height), int(weight), i))

arr.sort(key=lambda x: (x.height, -x.weight))

for a in arr:
    print(a.height, a.weight, a.number)


