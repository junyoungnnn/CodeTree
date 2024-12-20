class Array():
    def __init__(self, num, index, afteridx=0):
        self.num, self.index = num, index
        self.afteridx = 0

n = int(input())

arr = list(map(int, input().split()))

arrs = []

for i in range(1, n+1):
    arrs.append(Array(arr[i-1], i))

arrs.sort(key=lambda x: x.num)

for i in range(1, n+1):
    arrs[i-1].afteridx = i

arrs.sort(key=lambda x: x.index)

for a in arrs:
    print(a.afteridx, end=' ')