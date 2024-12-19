class Student():
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())

arr = [input().split() for _ in range(n)]

data = [Student(name, int(kor), int(eng), int(math)) for name, kor, eng, math in arr]

data.sort(key=lambda x: (x.kor + x.eng + x.math))


for student in data:
    print(student.name, student.kor, student.eng, student.math)