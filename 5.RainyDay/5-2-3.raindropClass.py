# 다. Raindrop 클래스를 정의하고 비 표현하기.

import sys, random
import pygame
from pygame.locals import *

SCREEN_RECT = pygame.Rect(0, 0, 1000, 600)
RAINDROP_SPAWN_TIME = 10  # milliseconds 빗방울 떨어지는 속도
RAINDROP_SPAWN_EVENT = pygame.USEREVENT + 1 # 객체 생성을 위한 이벤트 ID

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

# raindrop 클래스 정의
class Raindrop:  
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(5, 18)

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x, self.y + 5))
    # 빗방울이 화면을 벗어났는지 여부 확인
    def off_screen(self):
        return self.y >= SCREEN_RECT.height

def main():
    global screen
    global screen, cloud  # 클라우드 변수를 전역변수로 선언

    pygame.init()
    pygame.display.set_caption("Rainy Day")
    screen = pygame.display.set_mode(SCREEN_RECT.size)
    cloud = Cloud()  # 클라우드 객체 생성해 할당
    movex = 0  # cloud 이동값 선언
    pygame.time.set_timer(RAINDROP_SPAWN_EVENT, RAINDROP_SPAWN_TIME)#0.01초마다 이벤트 발생
    raindrops = [] # 빗방울 객체들을 저장할 리스트를 생성

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
            elif event.type == RAINDROP_SPAWN_EVENT:#이벤트 발성시 빗방울들 위치
                for i in range(10):
                    x = random.randint(cloud.rect.x, cloud.rect.x+300)
                    raindrops.append(Raindrop(x, cloud.rect.y + 100))

        screen.fill((255, 255, 255))

        rmdropsidx = [i for i, drop in enumerate(raindrops) if drop.off_screen()]#화면을 벗어난 빗방울들을 인덱스로 리스트 생성
        # 화면을 벗어난놈들 모조리 삭제
        for i in reversed(rmdropsidx): 
            raindrops.pop(i)
        # movex값이 0이 아니면 이동
        if movex:  
            cloud.move(movex)
        cloud.blit()  # display 업데이트전 화변에 복사
        # 빗방울 화면에 복사
        for drop in raindrops:
            drop.move()
            drop.draw()

        pygame.display.update()


if __name__ == '__main__':
    main()