n = int(input())

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

x, y = 0, 0

for i in range(n):
    direction, distance = input().split()
    distance = int(distance)
    if direction == 'E':
        nx, ny = dx[0] * distance, dy[0]
    

    x += nx
    y += ny

print(x, y)

테스트케이스


결과


코드 실행


제출 및 채점



    elif direction == 'S':
        nx, ny = dx[1], dy[1] * distance
    
    elif direction == 'W':
        nx, ny = dx[2] * distance, dy[2]

    elif direction == 'N':
        nx, ny = dx[3] , dy[3] * distance

    x += nx
    y += ny

print(x, y)