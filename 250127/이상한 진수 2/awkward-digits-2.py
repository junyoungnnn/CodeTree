a = input()

n = len(a)

result = 0

flag = False
count = 0

for i in range(n):
    if a[i] == '0' and flag == False:
        result = result + 2 ** (n- i- 1)
        flag = True
    elif a[i] == '1':
        result = result + 2 ** (n- i- 1)
        count += 1

if count == n:
    result -= 1

print(result)
