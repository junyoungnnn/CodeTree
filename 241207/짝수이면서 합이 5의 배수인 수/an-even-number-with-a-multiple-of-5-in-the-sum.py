def is_even_and_five(n):
    if n % 2 == 0 and (n % 10 + n // 10) % 5 == 0:
        return True
    return False

n = int(input())

if is_even_and_five(n):
    print("Yes")
else:
    print("No")