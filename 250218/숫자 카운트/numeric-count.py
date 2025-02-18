n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

count = 0

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or i == k or j == k:
                continue

            for A, B, C in zip(a, b, c):
                z = A % 10
                y = A // 10 % 10
                x = A // 100 % 10

                cnt1 = 0
                cnt2 = 0

                if i == x:
                    cnt1 += 1
                if j == y:
                    cnt1 += 1
                if k == z:
                    cnt1 += 1
                if i == y or i == z:
                    cnt2 += 1
                if j == x or j == z:
                    cnt2 += 1
                if k == x or k == y:
                    cnt2 += 1

                if cnt1 != B or cnt2 != C:
                    break
            else:
                count += 1

print(count)