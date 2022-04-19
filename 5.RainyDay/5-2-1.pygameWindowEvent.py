# 5.2 애니메이션 구현하기
# 가. 파이게임 윈도우 생성과 이벤트 처리하기

import sys, random
import pygame
from pygame.locals import *

SCREEN_RECT = pygame.Rect(0, 0, 1000, 600)

def main():
    global screen

    pygame.init()
    pygame.display.set_caption("Rainy Day")
    screen = pygame.display.set_mode(SCREEN_RECT.size)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        pygame.display.update()

if __name__ == '__main__':
    main()