# 3.1 turtle 모듈의 함수
# 3-1-1.turtleMovement.py

# 가. turtle의 움직임 관련 함수
# import turtle
# print(turtle.position())
# turtle.forward(25)
# print(turtle.position())
# turtle.forward(-75)
# print(turtle.position())
# turtle.right(45)
# print(turtle.heading())
# turtle.goto(150,150)
# turtle.circle(100)
# turtle.speed(0)
# turtle.circle(150)
# t2=turtle.Turtle()
# print(turtle.distance(t2.pos()))

# 나. 펜 제어 관련 함수
# import turtle
# turtle.pensize(1)
# print(turtle.pensize())
# turtle.pensize(3)
# turtle.forward(100)
# turtle.pencolor('pink')
# turtle.forward(100)
# turtle.goto(0,0)
# turtle.fillcolor('green')
# turtle.begin_fill()
# for i in range(3):
#     turtle.forward(100)
#     turtle.right(120)
# turtle.end_fill()
# turtle.clear()
# turtle.reset()
# turtle.write("Hello Turtle",True,align="center")
# turtle.write((0,0),True)


# 다. turtle의 상태 관련 함수와 이벤트 사용하기
# t.mainloop() 안넣어주면 뾱하고 거북이 사라짐

# import turtle as t
# import random as r
# t.shape('turtle')
# def turnLeft(t, angle):
#     t.left(angle)
# def chcolor(t):
#     t.pencolor(r.choice(['red','yellow','green']))
# def move(x,y):
#     t.goto(x,y)
# turnLeft(t, 180)
# chcolor(t)
# t.ondrag(move(100,100))
# t.mainloop()

# 3.1 라. turtle screen 관련 함수
# import turtle as t
# t.bgcolor('orange')
# print(t.screensize())
# t.screensize(1200, 1000)
# def f():
#     t.fd(50)
#     t.lt(60)
# t.onkey(f, "Up")
# t.listen()
# t.onscreenclick(t.goto)
# t.mainloop()

# 3.1 마. turtle screen 관련 함수 2
import turtle as t
t.title('ontimer test')
running = True
count=0
def f():
    if running:
        t.fd(50)
        t.lt(60)
        t.ontimer(f, 250)
        global count
        count += 1
        if count == 6:
            t.bye()
f()
t.mainloop()
