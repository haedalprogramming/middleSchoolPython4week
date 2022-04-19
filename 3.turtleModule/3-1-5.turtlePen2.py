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
forward(100)
# 터틀이 그린 펜 모두 지우고 터틀 위치 그대로
clear()
# 터틀이 그린 펜 모두 지우고 터틀 위치 정중앙
# reset()
# 화면에 글쓰기
write("Hello Turtle",True,align="center")
# write((0,0),True)
done() # 실행창 끄지 않고 유지하기