a, b = map(int, input().split())

def cal(n):
    if n % 2 == 0 or n % 10 == 5 or n % 3 == 0 and n % 9 != 0:
        return False
    return True

count = 0

for i in range(a, b+1):
    if cal(i):
        count += 1
print(count)