n = int(input())
real_arr = [int(input()) for _ in range(n)]

max_sum = 0
max_value = -1

for i in range(n-2):
    
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            arr = real_arr.copy()
            max_len = max(len(str(arr[i])), max(len(str(arr[j])), len(str(arr[k]))))
            value = arr[i] + arr[j] + arr[k]
            #print('value 출력', value, arr[i], arr[j], arr[k])
            for h in range(max_len):
                #print('반복시작', h)
                #print((arr[i] % 10 + arr[j] % 10 + arr[k] % 10) % 10)
                #print(max(arr[i] % 10, max(arr[j] % 10, arr[k] % 10)))
                if (arr[i] % 10 + arr[j] % 10 + arr[k] % 10) % 10 < max(arr[i] % 10, max(arr[j] % 10, arr[k] % 10)):
                    value = 0
                    #print('arri, arrj, arrk 불충족', i, j, k)
                    break
                else:
                    arr[i] //= 10
                    arr[j] //= 10
                    arr[k] //= 10
            else:
                max_value = max(max_value, value)

print(max_value)