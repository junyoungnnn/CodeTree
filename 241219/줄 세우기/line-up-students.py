class Student():
    def __init__(self, number, height, weight):
        self.height = height
        self.weight = weight
        self.number = number

n = int(input())

arr = [input().split() for _ in range(n)]

students = [Student(int(number), int(height), int(weight)) for number, (height, weight) in enumerate(arr, start=1)]


students.sort(key=lambda x: (-x.height, -x.weight, x.number))

for student in students:
    print(student.height, student.weight, student.number)