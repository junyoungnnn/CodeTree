class Forcast():
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())

arr = [input().split() for _ in range(n)]

data = [Forcast(date, day, weather) for date, day, weather in arr]

idx = 0
last_date = '2200-01-01'

for i in range(n):
    if data[i].weather == "Rain":
        if last_date > data[i].date:
            last_date = data[i].date
            idx = i

print(f'{data[idx].date} {data[idx].day} {data[idx].weather}')
