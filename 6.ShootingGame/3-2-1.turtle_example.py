# 첫번째 시도
# import turtle as t


# def main():
#     t.setup(500, 500)
#     t.title('Turtle Run')
#     t.bgcolor('forestgreen')


# if __name__ == '__main__':
#     main()


# 튜토리얼 수정 1
# from turtle import *
# color('red')
# title('Turtle Run')
# # begin_fill()
# # delay(100)
# # end_fill()
# done()

# 튜토리얼 수정 2
# import turtle as t
# t.color('red')
# t.title('Turtle Run')
# t.done()

# 튜토리얼
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()