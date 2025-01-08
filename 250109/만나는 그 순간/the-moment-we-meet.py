n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

arr1 = []
move1 = 0
for i in range(n):
    if d[i] == 'R':
        for j in range(t[i]):
            move1 += 1
            arr1.append(move1)
    else:
        for j in range(t[i]):
            move1 -= 1
            arr1.append(move1)

arr2 = []
move2 = 0
for i in range(m):
    if d2[i] == 'R':
        for j in range(t2[i]):
            move2 += 1
            arr2.append(move2)
    else:
        for j in range(t2[i]):
            move2 -= 1
            arr2.append(move2)

for i in range(len(arr1)):
    if arr1[i] == arr2[i]:
        print(i+1)
        break