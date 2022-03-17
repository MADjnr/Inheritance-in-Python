class Character:

    def __init__(self, x, y, num_lives): # x and y is to know where to position the image in the screen
        self.x = x
        self.y = y
        self.num_lives = num_lives


class Player(Character):
    INITIAL_X = 0
    INITIAL_Y = 0
    INITIAL_NUM_LIVES = 10


    def __init__(self, score=0):
        Character.__init__(self, Player.INITIAL_X, Player.INITIAL_Y, Player.INITIAL_NUM_LIVES) ##this is the point where
        ## where the constructor of the child class inherit the methods defined by the constructor of the parent class
        self.score = score ##this instance attribute was not defined in the parent class so, it is defined here for the purpose of the instances

class Enemy(Character):

    def __init__(self, x=15, y=15, num_lives=8, is_poisonous=False):
        Character.__init__(self, x, y, num_lives)
        self.is_poisonous = is_poisonous


my_player = Player()

print(my_player.score)
print(my_player.x)
print(my_player.y)
print(my_player.num_lives)

enemy_1 = Enemy(num_lives=1) ##this enemy has less number of lives
enemy_2 = Enemy(num_lives=30, is_poisonous=True) #this enemy is posinous and has a lot lives

print(enemy_1.is_poisonous)
print(enemy_1.x)
print(enemy_1.y)
print(enemy_1.num_lives)

print(enemy_2.is_poisonous)
print(enemy_2.x)
print(enemy_2.num_lives)



