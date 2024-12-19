class Student():
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

n = int(input())

arr = [input().split() for _ in range(n)]

students = [Student(name, int(height), int(weight)) for name, height, weight in arr]

students.sort(key=lambda x : (x.height, -x.weight))

for student in students:
    print(student.name, student.height, student.weight)

