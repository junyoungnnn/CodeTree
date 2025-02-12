import sys

N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

min_price = sys.maxsize

for i in range(N-T):
    price = 0
    for j in range(i, i + T):
        price += abs(H - arr[j])

    min_price = min(min_price, price)

print(min_price)
