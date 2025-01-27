A = input()

n = len(A)

count = 0

for i in range(n-3):
    for k in range(i+2, n-1):
        if A[i] == '(' and A[i+1] == '(' and A[k] == ')' and A[k+1] == ')':
            count += 1

print(count)