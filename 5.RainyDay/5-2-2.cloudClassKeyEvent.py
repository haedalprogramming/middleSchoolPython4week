# 나. cloud 클래스를 생성하고 키 이벤트 처리하기
# cloud.png 따로 저장
# 좌우 화살표로 구름 움직이기

import sys, random
import pygame
from pygame.locals import *

SCREEN_RECT = pygame.Rect(0, 0, 1000, 600)

# Cloud 정의
class Cloud:
    def __init__(self):
        self.surface = pygame.image.load("cloud.png").convert()
        self.rect = self.surface.get_rect()
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.y = 50

    def blit(self):
        screen.blit(self.surface, self.rect)
    # 구름 방향키 이동
    def move(self, x):
        self.rect.x += x

def main():
    global screen
    # 클라우드 변수를 전역변수로 선언
    global screen, cloud

    pygame.init()
    pygame.display.set_caption("Rainy Day")
    screen = pygame.display.set_mode(SCREEN_RECT.size)
    cloud = Cloud() # 클라우드 객체 생성해 할당
    movex = 0 # cloud 이동값 선언

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit()
            # 키 누르면 movex값 변경
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    movex += 1
                elif event.key == K_LEFT:
                    movex -= 1
            # 키 때면 초기화
            elif event.type == KEYUP:
                movex = 0

        screen.fill((255, 255, 255))
        # movex값이 0이 아니면 이동
        if movex:
            cloud.move(movex)
        # display 업데이트전 화변에 복사
        cloud.blit()
        pygame.display.update()

if __name__ == '__main__':
    main()