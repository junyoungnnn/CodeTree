class Student():
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())

arr = [input().split() for _ in range(n)]

students = [Student(name, int(kor), int(eng), int(math)) for name, kor, eng, math in arr]

students.sort(key=lambda x: (-x.kor, -x.eng, -x.math))

for i in range(n):
    print(f'{students[i].name} {students[i].kor} {students[i].eng} {students[i].math}')