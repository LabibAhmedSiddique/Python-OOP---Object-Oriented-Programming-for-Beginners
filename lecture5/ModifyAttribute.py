from turtle import speed


class Enemy:

    speed = 8

    def __init__(self, x, y, difficulty):
        self.x = x
        self.y = y
        self.difficulty = difficulty


print(Enemy.speed)
Enemy.speed = 7
print(Enemy.speed)
