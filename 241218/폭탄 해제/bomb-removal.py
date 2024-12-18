class Boom():
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

code, color, second = input().split()

second = int(second)

boom = Boom(code, color, second)

print(f'code : {boom.code}')
print(f'color : {boom.color}')
print(f'second : {boom.second}')
