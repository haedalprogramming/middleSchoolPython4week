# 3.2 혼자해보기 
# prey에 닿을 때마다 점수를 올리거나 
# 일정 시간이 지남에 따라 추격하는 Turtle객체를 추가해보자.

# 점수추가 버전 turtle객체 추가는 너무 복잡해짐

import  turtle as t
from random import randint
gameon =False
def turnright():
    t.setheading(0)
def turnleft():
    t.setheading(180)
def turnup():
    t.setheading(90)
def turndown():
    t.setheading(270)
def runforward():
    global gameon, p
    t.forward(10)
    angle = p.towards(t.pos())
    p.setheading(angle)
    p.forward(7)
    if t.distance(prey)<15:
        prey.goto(randint(-200,200),randint(-200,200))
    if t.distance(p)<15:
        t.write('Game Over', font=('Aril', 20, 'bold'))
        gameon = False
        return
    if gameon:
        t.ontimer(runforward,100)
def createpursuer():
    global p
    p=t.Turtle()
    p.shape('turtle')
    p.color('black')
    p.up()
    p.hideturtle()
    p.goto(-250,-250)
    p.showturtle()
def createprey():
    global prey
    prey=t.Turtle()
    prey.shape('circle')
    prey.color('hotpink')
    prey.up()
    prey.goto(randint(-200, 200),randint(-200, -200))
def main():
    global gameon
    t.setup(500, 500)
    t.title('Turtle Run')
    t.bgcolor('forestgreen')
    t.shape('turtle')
    t.color('white')
    t.up()
    t.onkeypress(turnright,'Right')
    t.onkeypress(turnleft, 'Left')
    t.onkeypress(turnup, 'Up')
    t.onkeypress(turndown, 'Down')
    t.listen()
    gameon = True
    createpursuer()
    createprey()
    runforward()
if __name__ == '__main__':
    main()
t.mainloop()