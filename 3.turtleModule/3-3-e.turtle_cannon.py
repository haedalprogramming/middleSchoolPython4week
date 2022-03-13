# 3.3 혼자해보기
# 게임이 무한히 계속 되지 않도록 게임 종료 조건을 추가해보자.

import time
import turtle as t
import random

cannon = t.Turtle()
def init():
    global target, chance
    chance = 0


    t.setup(700,500)
    t.color('black')
    t.pensize(1)
    t.goto(-300,0)
    t.down()
    t.goto(300,0)


    target=random.randint(50,150)
    t.pensize(3)
    t.color('green')
    t.up()
    t.goto(target - 25,2)
    t.down()
    t.goto(target +25,2)
    t.hideturtle()


    cannon.color('black')
    cannon.up()
    cannon.goto(-200,10)
    cannon.setheading(20)
def reset():
    t.reset()
    cannon.reset()
    init()

def turn_up():
    cannon.left(2)

def turn_down():
    cannon.right(2)

def fire():
    global target, chance
    ang = cannon.heading()
    while cannon.ycor()>0:
        cannon.forward(15)
        cannon.right(5)

    d = cannon.distance(target,0)
    cannon.sety(random.randint(10,100))
    if d < 25:
        cannon.color('blue')
        cannon.write('Good!',False,'center',('',15))
        time.sleep(2)
    else:
        cannon.color('red')
        cannon.write('Bad!', False, 'center', ('', 15))
    chance += 1
    if chance==2:
        time.sleep(2)
        reset()
    cannon.color('black')
    cannon.goto(-200,10)
    cannon.setheading(ang)
init()
t.onkeypress(turn_up,'Up')
t.onkeypress(turn_down,'Down')
t.onkeypress(fire,'space')
t.listen()
t.mainloop()