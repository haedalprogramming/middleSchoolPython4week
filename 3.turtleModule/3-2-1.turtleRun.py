# 3.2 turtle run 게임 만들기
# 가. 윈도우 생성하고 제목과 배경색 설정

# import turtle as t
# def main():
#     t.setup(500,500)
#     t.title('Turtle Run')
#     t.bgcolor('forestgreen')
# if __name__ == '__main__':
#     main()
# t.mainloop()

# 나. 거북이 t 생성하기
# import  turtle as t
# gameon =False
# def turnright():
#     t.setheading(0)
# def turnleft():
#     t.setheading(180)
# def turnup():
#     t.setheading(90)
# def turndown():
#     t.setheading(270)
# def runforward():
#     global gameon
#     t.forward(10)
#     if gameon:
#         t.ontimer(runforward,100)
# def main():
#     global gameon
#     t.setup(500, 500)
#     t.title('Turtle Run')
#     t.bgcolor('forestgreen')
#     t.shape('turtle')
#     t.color('white')
#     t.up()
#     t.onkeypress(turnright,'Right')
#     t.onkeypress(turnleft, 'Left')
#     t.onkeypress(turnup, 'Up')
#     t.onkeypress(turndown, 'Down')
#     t.listen()
#     gameon = True
#     runforward()
# if __name__ == '__main__':
#     main()
# t.mainloop()

# 다. 거북이 t를 추격하는 거북이p 생성하기
# import  turtle as t
# gameon =False
# def turnright():
#     t.setheading(0)
# def turnleft():
#     t.setheading(180)
# def turnup():
#     t.setheading(90)
# def turndown():
#     t.setheading(270)
# def runforward():
#     global gameon, p
#     t.forward(10)
#     angle = p.towards(t.pos())
#     p.setheading(angle)
#     p.forward(7)
#     if gameon:
#         t.ontimer(runforward,100)
# def createpursuer():
#     global p
#     p=t.Turtle()
#     p.shape('turtle')
#     p.color('black')
#     p.up()
#     p.hideturtle()
#     p.goto(-250,-250)
#     p.showturtle()
# def main():
#     global gameon
#     t.setup(500, 500)
#     t.title('Turtle Run')
#     t.bgcolor('forestgreen')
#     t.shape('turtle')
#     t.color('white')
#     t.up()
#     t.onkeypress(turnright,'Right')
#     t.onkeypress(turnleft, 'Left')
#     t.onkeypress(turnup, 'Up')
#     t.onkeypress(turndown, 'Down')
#     t.listen()
#     gameon = True
#     createpursuer()
#     runforward()
# if __name__ == '__main__':
#     main()
# t.mainloop()

# 라. prey 생성하기
# import  turtle as t
# from random import randint
# gameon =False
# def turnright():
#     t.setheading(0)
# def turnleft():
#     t.setheading(180)
# def turnup():
#     t.setheading(90)
# def turndown():
#     t.setheading(270)
# def runforward():
#     global gameon, p
#     t.forward(10)
#     angle = p.towards(t.pos())
#     p.setheading(angle)
#     p.forward(7)
#     if t.distance(prey)<15:
#         prey.goto(randint(-200,200),randint(-200,200))
#     if gameon:
#         t.ontimer(runforward,100)
# def createpursuer():
#     global p
#     p=t.Turtle()
#     p.shape('turtle')
#     p.color('black')
#     p.up()
#     p.hideturtle()
#     p.goto(-250,-250)
#     p.showturtle()
# def createprey():
#     global prey
#     prey=t.Turtle()
#     prey.shape('circle')
#     prey.color('hotpink')
#     prey.up()
#     prey.goto(randint(-200, 200),randint(-200, -200))
# def main():
#     global gameon
#     t.setup(500, 500)
#     t.title('Turtle Run')
#     t.bgcolor('forestgreen')
#     t.shape('turtle')
#     t.color('white')
#     t.up()
#     t.onkeypress(turnright,'Right')
#     t.onkeypress(turnleft, 'Left')
#     t.onkeypress(turnup, 'Up')
#     t.onkeypress(turndown, 'Down')
#     t.listen()
#     gameon = True
#     createpursuer()
#     createprey()
#     runforward()
# if __name__ == '__main__':
#     main()
# t.mainloop()

# 마. 게임 끝내기
# import  turtle as t
# from random import randint
# gameon =False
# def turnright():
#     t.setheading(0)
# def turnleft():
#     t.setheading(180)
# def turnup():
#     t.setheading(90)
# def turndown():
#     t.setheading(270)
# def runforward():
#     global gameon, p
#     t.forward(10)
#     angle = p.towards(t.pos())
#     p.setheading(angle)
#     p.forward(7)
#     if t.distance(prey)<15:
#         prey.goto(randint(-200,200),randint(-200,200))
#     if t.distance(p)<15:
#         t.write('Game Over', font=('Aril', 20, 'bold'))
#         gameon = False
#         return
#     if gameon:
#         t.ontimer(runforward,100)
# def createpursuer():
#     global p
#     p=t.Turtle()
#     p.shape('turtle')
#     p.color('black')
#     p.up()
#     p.hideturtle()
#     p.goto(-250,-250)
#     p.showturtle()
# def createprey():
#     global prey
#     prey=t.Turtle()
#     prey.shape('circle')
#     prey.color('hotpink')
#     prey.up()
#     prey.goto(randint(-200, 200),randint(-200, -200))
# def main():
#     global gameon
#     t.setup(500, 500)
#     t.title('Turtle Run')
#     t.bgcolor('forestgreen')
#     t.shape('turtle')
#     t.color('white')
#     t.up()
#     t.onkeypress(turnright,'Right')
#     t.onkeypress(turnleft, 'Left')
#     t.onkeypress(turnup, 'Up')
#     t.onkeypress(turndown, 'Down')
#     t.listen()
#     gameon = True
#     createpursuer()
#     createprey()
#     runforward()
# if __name__ == '__main__':
#     main()
# t.mainloop()