# 혼자서 해보기
# pygame.time.Clock 객체를 활용해 1초동안 업데이트되는 프레임 수 제한하기
# 초당 20프레임부터 할만하고 60프레임이면 아주 쾌적
#======================================================================
import sys, random
import pygame
from pygame.locals import *

SCREEN_RECT = pygame.Rect(0, 0, 1000, 600)
RAINDROP_SPAWN_TIME = 10  # milliseconds 빗방울 떨어지는 속도
RAINDROP_SPAWN_EVENT = pygame.USEREVENT + 1#객체 생성을 위한 이벤트 ID


class Cloud:  # Cloud 정의
    def __init__(self):
        self.surface = pygame.image.load("cloud.png").convert()
        self.rect = self.surface.get_rect()
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.y = 50

    def blit(self):
        screen.blit(self.surface, self.rect)

    def move(self, x):  # 구름 방향키 이동
        self.rect.x += x

class Raindrop:  # raindrop 클래스 정의
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(5, 18)

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x, self.y + 5))

    def off_screen(self):#빗방울이 화면을 벗어났는지 여부 확인
        return self.y >= SCREEN_RECT.height

class Mike:#Mike클래스 정의
    def __init__(self):#이미지 surface를 생성,  rect속성 저장후 위치 설정
        self.surface = pygame.image.load("Mike.png").convert(),pygame.image.load("Mike_umbrella.png").convert()#우산쓴 mike와 우산벗은 mike를 surface로 가지도록 설정
        self.idx = True#idx가 참이면 우산을 쓰고 거짓이면 우산안씀
        self.rect = self.surface[self.idx].get_rect()
        self.rect.x = 300
        self.rect.y = 400

    def blit(self):#화면에 이미지 복사
       screen.blit(self.surface[self.idx], self.rect)#idx값에 따라 이미지 변경

    def hit_by(self, raindrop):#빗방울이 Mike에 닿았는지 검사
        return self.rect.collidepoint(raindrop.x, raindrop.y)

    def wear_umbrella(self, flag):#flag값에 따라 이미지를 설정, rect속성을 바꿔줌
        self.idx = flag
        self.rect = self.surface[self.idx].get_rect()
        self.rect.x = 300
        self.rect.y = 400

def main():
    global screen
    global screen, cloud  # 클라우드 변수를 전역변수로 선언

    pygame.init()
    pygame.display.set_caption("Rainy Day")
    screen = pygame.display.set_mode(SCREEN_RECT.size)
    cloud = Cloud()  # 클라우드 객체 생성해 할당
    movex = 0  # cloud 이동값 선언
    pygame.time.set_timer(RAINDROP_SPAWN_EVENT, RAINDROP_SPAWN_TIME)#0.01초마다 이벤트 발생
    raindrops = []#빗방울 객체들을 저장할 리스트를 생성

    mike = Mike() #mike클래스의 객체를 생성하고 mike변수에 할당

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == KEYDOWN:  # 키 누르면 movex값 변경
                if event.key == K_RIGHT:
                    movex += 1
                elif event.key == K_LEFT:
                    movex -= 1
            elif event.type == KEYUP:  # 키 때면 초기화
                movex = 0
            elif event.type == RAINDROP_SPAWN_EVENT:#이벤트 발성시 빗방울들 위치
                for i in range(10):
                    x = random.randint(cloud.rect.x, cloud.rect.x+300)
                    raindrops.append(Raindrop(x, cloud.rect.y + 100))

        screen.fill((255, 255, 255))

        rmdropsidx = [i for i, drop in enumerate(raindrops) if drop.off_screen() or mike.hit_by(drop)]#화면을 벗어난or Mike범위에 포함된 빗방울들을 인덱스로 리스트 생성
        for i in reversed(rmdropsidx):#화면을 벗어난놈들 모조리 삭제
            raindrops.pop(i)

        if movex:  # movex값이 0이 아니면 이동
            cloud.move(movex)
        cloud.blit()  # display 업데이트전 화변에 복사

        flag = True
        if mike.rect.x > cloud.rect.x + cloud.rect.width or\
            mike.rect.x + mike.rect.width < cloud.rect.x:
            flag = False# mike가 구름아래에 있으면 flag를 True로, 구름아래 없다면 false로 설정
        mike.wear_umbrella(flag)
        mike.blit() #마이크도 화면에 복사

        for drop in raindrops:#빗방울 화면에 복사
            drop.move()
            drop.draw()

        pygame.time.Clock().tick(60)#1초동안 업데이트되는 프레임수를 제한
        pygame.display.update()


if __name__ == '__main__':
    main()