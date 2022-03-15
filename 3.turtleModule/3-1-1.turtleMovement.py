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
# turtle.mainloop() # 실행창 끄지 않고 유지하기

# 나. 펜 제어 관련 함수
# 너무 빠르게 실행창이 꺼짐
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
# turtle.mainloop() # 실행창 끄지 않고 유지하기


# 다. turtle의 상태 관련 함수와 이벤트 사용하기
# 거북이 누르고, 옮기고, 색 바뀌기

# import turtle as t
# import random as r
# t.shape('turtle')
# def turn(x,y):
#     t.left(180)
# def chcolor(x,y):
#     t.pencolor(r.choice(['red','yellow','green']))
# def move(x,y):
#     t.goto(x,y)
# t.onclick(turn)
# t.ondrag(move)
# t.onrelease(chcolor)
# t.mainloop()

# 3.1 라. turtle screen 관련 함수
# 마우스 클릭하면 이동하고, 위쪽 방향키 누르면 육각형 한변씩 그리기
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
# 육각형 그리고 프로그램 종료
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
