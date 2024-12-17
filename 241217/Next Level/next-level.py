ID, level = input().split()

class NextLevel:
    def __init__(self, ID='codetree', level=10):
        self.ID = ID
        self.level = level

user1 = NextLevel()
user2 = NextLevel(ID, level)

print('user', user1.ID, 'lv', user1.level)
print('user', user2.ID, 'lv', user2.level)

