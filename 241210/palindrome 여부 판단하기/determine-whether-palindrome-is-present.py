def palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True

s = input()

if palindrome(s):
    print('Yes')
else:
    print('No')