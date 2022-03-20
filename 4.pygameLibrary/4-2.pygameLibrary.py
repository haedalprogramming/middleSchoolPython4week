#======================================================================
# 4.2 파이게임 라이브러리 살펴보기
# 다. pygame.Surface 객체
# 파이게임 실행하기
#======================================================================
import pygame
from pygame.locals import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((250, 50))
    pygame.display.set_caption('First Pygame program')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    font = pygame.font.Font(None, 36)
    text = font.render("Hello Pygame", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx

    background.blit(text, textpos)
    screen.blit(background, (0, 0))
    pygame.display.update()

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return None
        screen.blit(background, (0, 0))
        pygame.display.update()

if __name__ == '__main__':
    main()
#======================================================================
#바. pygame.time 모듈
# Pong Game
#======================================================================
import pygame, random
from pygame.locals import *

pygame.init()

w, h = 500, 500
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Pong Game')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ball_x = random.randint(0, 250)
ball_y = random.randint(0, 250)
move_x, move_y = 8, 8
paddle_x, paddle_y = 220, 470

fps = pygame.time.Clock()
gameover = False
while not gameover:
    for event in pygame.event.get():
        if event.type == QUIT:
            gameover = True
        elif event.type == MOUSEMOTION:
            paddle_x = event.pos[0]

    ball_x += move_x
    ball_y += move_y

    ball_rect = Rect(ball_x, ball_y, 20, 20)
    paddle_rect = Rect(paddle_x, paddle_y, 60, 20)

    if ball_y+20 >= paddle_y and \
        paddle_x <= ball_x <= paddle_x+60:
            move_y = -abs(move_y)
    if ball_x < 0 or ball_x > w:
        move_x = -move_x
    if ball_y < 0:
        move_y = -move_y
    if ball_y > paddle_y+20:
        gameover = True
        print('You lost! Game over!')

    screen.fill(BLACK)
    pygame.draw.ellipse(screen, WHITE, ball_rect)
    pygame.draw.rect(screen, WHITE, paddle_rect)
    pygame.display.update()
    fps.tick(40)

pygame.quit()
#======================================================================
#사. pygame.Rect
#실행 파일 디렉토리에 intro_ball.gif파일필요
# moving Ball
# 무식하게 프레임별로 전부 컴퓨터가 연산하기 - 기본버전
#======================================================================
import pygame, sys
from pygame.locals import *

pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load('intro_ball.gif')
ballrect = ball.get_rect()

c = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.update()

    c.tick(120)
#======================================================================
# moving Ball 2
# 마지막 프레임 이후 변경된 부분만 업데이트
#======================================================================
import pygame, sys
from pygame.locals import *

pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load('intro_ball.gif')
ballrect = ball.get_rect()

c = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            sys.exit()

    dirty_rects = []
    dirty_rects.append(ballrect)
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.update()

    c.tick(120)
#======================================================================
# 4-2-4.dataRestoration.py
# 파이게임에서 이미지의 원본을 유지해야할까?
# 복원할 데이터의 원본이 없는 예시
screen = [1, 1, 2, 2, 2, 1]
print(screen)
playerpos = 3
screen[playerpos] = 8
print(screen)
playerpos -= 1
screen[playerpos] = 8
print(screen)
#======================================================================
# 4-2-4.dataRestoration2.py
# 파이게임에서 이미지의 원본을 유지해야할까?
# 복원할 데이터의 원본이 있는 예시
background = [1, 1, 2, 2, 2, 1]
screen = [0]*6
for i in range(6):
    screen[i] = background[i]

print(screen)
playerpos = 3
screen[playerpos] = 8
print(screen)
screen[playerpos] = background[playerpos]
playerpos -= 1
screen[playerpos] = 8
print(screen)
print("원본: ", background)