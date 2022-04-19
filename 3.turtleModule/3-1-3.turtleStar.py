# from turtle import *
 
# color('red', 'yellow')

# begin_fill()
# for _ in range(5):
#     forward(100)
#     right(360 / 5 * 2)
# end_fill()

# done()

from turtle import *

# 펜 칼라, 채우기 칼라 설정
color('red', 'yellow')

# 색 채우기 시작
begin_fill()
# 별 그리기
for _ in range(5):
    # 한 변 길이 100
    forward(100)
    # 외각 회전
    right(360 / 5 * 2)
# 색 채우기 끝
end_fill()
# 화면 유지
done()