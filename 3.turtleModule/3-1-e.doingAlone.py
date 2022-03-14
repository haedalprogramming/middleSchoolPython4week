# 3.1 혼자서 해보기
# 5개의 원을 그려 과녁을 만드는 스크립트를 작성해보자.

import turtle as t
t.bgcolor('black')
def circle(rad, col):
    t.pencolor("")
    t.goto(0,-(rad))
    t.fillcolor(col)
    t.begin_fill()
    t.circle(rad)
    t.end_fill()
circle(300,'white')
circle(250,'black')
circle(200,'blue')
circle(150,'red')
circle(100,'yellow')
t.mainloop()