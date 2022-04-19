# 사. pygame.Rect
# 실행 파일 디렉토리에 intro_ball.gif파일필요
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