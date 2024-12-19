class Student():
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

n = 5

arr = [input().split() for _ in range(n)]

students = [Student(name, int(height), float(weight)) for name, height, weight in arr]

students.sort(key=lambda x: x.name)

print('name')
for student in students:
    print(student.name, student.height, student.weight)

print()

print('height')
students.sort(key=lambda x: -x.height)
for student in students:
    print(student.name, student.height, student.weight)