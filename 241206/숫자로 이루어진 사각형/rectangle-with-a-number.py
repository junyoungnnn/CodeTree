def print_rect(n):
    cnt = 0
    for i in range(1, n * n + 1):
        cnt += 1
        if cnt > 9:
            cnt = 1
        print(cnt, end=' ')
        if i % n == 0:
            print()

n = int(input())

print_rect(n)
