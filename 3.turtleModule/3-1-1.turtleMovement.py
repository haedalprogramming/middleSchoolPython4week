# 3.1 turtle 모듈의 함수
# 3-1-1.turtleMovement.py

# 가. turtle의 움직임 관련 함수
# from turtle import *

# forward(25)
# forward(-75)
# right(45)
# goto(150,150)
# circle(100)
# speed(0)
# circle(150)
# mainloop() # 실행창 끄지 않고 유지하기

# 나. 펜 제어 관련 함수
# # 너무 빠르게 실행창이 꺼짐
# from turtle import *
# pensize(3)
# forward(100)
# pencolor('pink')
# forward(100)
# goto(0,0)
# fillcolor('green')
# begin_fill()
# for i in range(3):
#     forward(100)
#     right(120)
# end_fill()
# clear()
# reset()
# write("Hello Turtle",True,align="center")
# write((0,0),True)
# mainloop() # 실행창 끄지 않고 유지하기

from turtle import *

# 터틀 펜 사이즈 설정
pensize(3)
# 앞으로 100 픽셀
forward(100)
# 핑크색 펜 색
pencolor('pink')
# 앞으로 100 픽셀
forward(100)
# 화면 중앙 (0,0)으로 가라
goto(0,0)
# 채우기 칼라 그린
fillcolor('green')
# 색 채우기 시작
begin_fill()
# 삼각형 그리기
for i in range(3):
    forward(100)
    right(120)
end_fill()
clear()
reset()
write("Hello Turtle",True,align="center")
write((0,0),True)
mainloop() # 실행창 끄지 않고 유지하기


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
# import turtle as t
# t.title('ontimer test')
# running = True
# count=0
# def f():
#     if running:
#         t.fd(50)
#         t.lt(60)
#         t.ontimer(f, 250)
#         global count
#         count += 1
#         if count == 6:
#             t.bye()
# f()
# t.mainloop()
