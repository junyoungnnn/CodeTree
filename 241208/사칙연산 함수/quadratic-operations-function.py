a, o, c = input().split()

a, c = int(a), int(c)

arr = ['+', '-', '/', '*']

if o == arr[0]:
    print(a, arr[0], c, '=', a + c)
elif o == arr[1]:
    print(a, arr[1], c, '=', a - c)
elif o == arr[2]:
    print(a, arr[2], c, '=', a // c)
elif o == arr[3]:
    print(a, arr[3], c, '=', a * c)
else:
    print('False')