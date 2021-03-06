# moving Ball 2
# 마지막 프레임 이후 변경된 부분만 업데이트

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