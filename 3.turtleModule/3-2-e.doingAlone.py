# 3.2 혼자해보기 
# prey에 닿을 때마다 점수를 올리거나 
# 일정 시간이 지남에 따라 추격하는 Turtle객체를 추가해보자.

# 점수추가 버전 turtle객체 추가는 너무 복잡해짐
# 먹이 먹을때마다 속도 추가해주는건 어떨지?

import  turtle as t
from random import randint
import time

start = time.time() # 게임 실행 시간으로 적 속도 조절하자
gameon =False
score = 0#점수
def turnright():
    t.setheading(0)
def turnleft():
    t.setheading(180)
def turnup():
    t.setheading(90)
def turndown():
    t.setheading(270)
def runforward():
    global gameon, p, score
    t.forward(10)
    angle = p.towards(t.pos())
    p.setheading(angle)
    p.forward(6+(time.time()-start)/2) # 적 속도 조절
    if t.distance(prey)<15:
        prey.goto(randint(-200,200),randint(-200,200))
        score += 1#먹으면 점수추가
    if t.distance(p)<15:
        t.write("Game Over\nScore:{}".format(score), font=('Aril', 20, 'bold'))#끝나면 점수출력
        gameon = False
        return
    if gameon:
        t.ontimer(runforward,100)
def createpursuer(): # 적
    global p
    p=t.Turtle()
    p.shape('turtle')
    p.color('black')
    p.up()
    p.hideturtle()
    p.goto(-250,-250)
    p.showturtle()
def createprey(): #먹이
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