from turtle import Turtle, Screen

import random

colors = ["red", "yellow", "green", "blue", "brown"]
turtles = {}
offsetX = {}
offsetY = {}
for index_range in range(0, 5):
    turtles[colors[index_range]] = Turtle()
    turtles[colors[index_range]].shape("turtle")
    turtles[colors[index_range]].color(colors[index_range])
    turtles[colors[index_range]].penup()
    offsetX[colors[index_range]] = 0
    offsetY[colors[index_range]] = 0


def start():
    y = 0
    for turtle in colors:
        offsetX[turtle] = -210
        if y == 0:
            turtles[turtle].goto(x=-210, y=0)
            offsetY[turtle] = y
        if y > 0:
            turtles[turtle].goto(x=-210, y=y)
            offsetY[turtle] = y
            y = -y
        else:
            turtles[turtle].goto(x=-210, y=y)
            offsetY[turtle] = y
            y = -y
            y = y + 40


def move():
    for color in colors:
        randoms = int(offsetX[color]) + random.randrange(1, 5)
        # if color == "red":
        #     randoms = int(offsetX[color]) + 10
        offsetX[color] = randoms
        turtles[color].goto(x=randoms, y=offsetY[color])


def stats():
    key_max = max(offsetX, key=offsetX.get)
    if offsetX[key_max] >= 225:
        return False
    else:
        return True


def winner(win, bet):
    if win.capitalize() == str(bet).capitalize():
        print(f"Congrats {win} turtle win the game, You win")
    else:
        print(f"You lose, Winner is {win}  turtle")


screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Put Your Bet", prompt="Choose the color")
start()
while stats():
    move()

key = max(offsetX, key=offsetX.get)

winner(key, user_bet)
screen.exitonclick()
