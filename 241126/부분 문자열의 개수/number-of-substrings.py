a = input()
b = input()

count = 0

for i in range(len(a) - 1):
    if b[0] == a[i]:
        if b[1] == a[i+1]:
            count += 1

print(count)