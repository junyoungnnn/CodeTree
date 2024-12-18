class Information():
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city

n = int(input())

arr = []

for i in range(n):
    arr.append(input().split())

arr_sorted = sorted(arr)

user = Information(arr_sorted[-1][0], arr_sorted[-1][1], arr_sorted[-1][2])

print(f'name {user.name}')
print(f'addr {user.addr}')
print(f'city {user.city}')