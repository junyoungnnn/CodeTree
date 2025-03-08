X, Y = map(int, input().split())

count = 0

for i in range(X, Y+1):
    for j in range(len(str(i))//2):
        if str(i)[j] != str(i)[-1-j]:
            break
    else:
        count += 1

print(count)

