class Distance():
    def __init__(self, number, x, y):
        self.number, self.x, self.y = number, x, y

n = int(input())

arr = [input().split() for _ in range(n)]

points = [Distance(number, abs(int(x)), abs(int(y))) for number, (x, y) in enumerate(arr, start=1)]

points.sort(key=lambda x: (x.x+x.y))

for point in points:
    print(point.number)