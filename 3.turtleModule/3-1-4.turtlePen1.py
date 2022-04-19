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
# 색 채우기 끝
end_fill()
# 화면 유지
done()