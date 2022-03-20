# 4.2 파이게임 라이브러리 살펴보기
# 다. pygame.Surface 객체
# 파이게임 실행하기
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