# 3.3 turtle cannon 게임 만들기

# 가. 게임 초기화하기
# import turtle as t
# import random
# cannon = t.Turtle()
# def init():
#     global target
#     t.setup(700,500)
#     t.color('black')
#     t.pensize(1)
#     t.goto(-300,0)
#     t.down()
#     t.goto(300,0)
#     target=random.randint(50,150)
#     t.pensize(3)
#     t.color('green')
#     t.up()
#     t.goto(target - 25,2)
#     t.down()
#     t.goto(target +25,2)
#     t.hideturtle()
#     cannon.color('black')
#     cannon.up()
#     cannon.goto(-200,10)
#     cannon.setheading(20)
# init()
# t.mainloop()

# 나. 키 이벤트 처리하기
# import turtle as t
# import random
# cannon = t.Turtle()
# def init():
#     global target
#     t.setup(700,500)
#     t.color('black')
#     t.pensize(1)
#     t.goto(-300,0)
#     t.down()
#     t.goto(300,0)
#     target=random.randint(50,150)
#     t.pensize(3)
#     t.color('green')
#     t.up()
#     t.goto(target - 25,2)
#     t.down()
#     t.goto(target +25,2)
#     t.hideturtle()
#     cannon.color('black')
#     cannon.up()
#     cannon.goto(-200,10)
#     cannon.setheading(20)
# def turn_up():
#     cannon.left(2)
# def turn_down():
#     cannon.right(2)
# def fire():
#     global target
#     ang = cannon.heading()
#     while cannon.ycor()>0:
#         cannon.forward(15)
#         cannon.right(5)
# init()
# t.onkeypress(turn_up,'Up')
# t.onkeypress(turn_down,'Down')
# t.onkeypress(fire,'space')
# t.listen()
# t.mainloop()


# 다. 결과 화면에 출력하기
# import turtle as t
# import random
# cannon = t.Turtle()
# def init():
#     global target
#     t.setup(700,500)
#     t.color('black')
#     t.pensize(1)
#     t.goto(-300,0)
#     t.down()
#     t.goto(300,0)
#     target=random.randint(50,150)
#     t.pensize(3)
#     t.color('green')
#     t.up()
#     t.goto(target - 25,2)
#     t.down()
#     t.goto(target +25,2)
#     t.hideturtle()
#     cannon.color('black')
#     cannon.up()
#     cannon.goto(-200,10)
#     cannon.setheading(20)
# def turn_up():
#     cannon.left(2)
# def turn_down():
#     cannon.right(2)
# def fire():
#     global target
#     ang = cannon.heading()
#     while cannon.ycor()>0:
#         cannon.forward(15)
#         cannon.right(5)
#     d = cannon.distance(target,0)
#     cannon.sety(random.randint(10,100))
#     if d < 25:
#         cannon.color('blue')
#         cannon.write('Good!',False,'center',('',15))
#     else:
#         cannon.color('red')
#         cannon.write('Bad!', False, 'center', ('', 15))
# init()
# t.onkeypress(turn_up,'Up')
# t.onkeypress(turn_down,'Down')
# t.onkeypress(fire,'space')
# t.listen()
# t.mainloop()

# 라. 목표지점을 설정하고 2번에 기회를 주고 초기화하기
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
    if d < 25 or chance ==2:
        cannon.color('blue')
        cannon.write('Good!',False,'center',('',15))
        reset()
    else:
        cannon.color('red')
        cannon.write('Bad!', False, 'center', ('', 15))
    chance += 1
    cannon.color('black')
    cannon.goto(-200,10)
    cannon.setheading(ang)
init()
t.onkeypress(turn_up,'Up')
t.onkeypress(turn_down,'Down')
t.onkeypress(fire,'space')
t.listen()
t.mainloop()
