# 바. pygame.time 모듈
# Pong Game
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