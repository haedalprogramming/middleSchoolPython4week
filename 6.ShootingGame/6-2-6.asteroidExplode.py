# 바. 미사일 맞은 운석처리
# 미사일과 운석 충돌처리

import pygame
import random
from time import sleep
import sys

# 화면 넓이 높이 우주선 넓이 높이를 사용하기 좋게 전역변수로 선언해준다.
screen_width = 480 
screen_height = 640
shuttle_width = 53
shuttle_height = 111
asteroid_width = 39
asteroid_height = 22

# 게임 초기화를 함수로
def startGame():
    global screen, clock, shuttle, missile, asteroid

    pygame.init()  # 초기화
    screen = pygame.display.set_mode((screen_width, screen_height))#넓이와 높이를 값으로 가지는 화면크기 생성
    pygame.display.set_caption("saving Earth")#게임 이름 써주기
    shuttle = pygame.image.load('shuttle.jpg')
    asteroid = pygame.image.load('ast.png')
    missile = pygame.image.load('mis.png')
    clock = pygame.time.Clock()

# 스프라이트 그리기 함수
def drawObject(obj, x, y):
    global screen
    screen.blit(obj, (x, y))

# 운석이랑 충돌
def explode():
    pygame.display.update()
    sleep(3)
    runGame()

# 게임 실행 함수
def runGame():
    missile_xy = []#미사일 리스트 생성

    x = screen_width * 0.4  #우주선 좌표
    y = screen_height * 0.8
    x_change = 0
    asteroid_x = random.randrange(0, screen_width - asteroid_width)#운석 시작위치 랜덤
    asteroid_y = 0#운석 초기값들 설정
    asteroid_speed = 3

    done = False
    # 게임이 끝나지 않았을때
    while not done:  
        for event in pygame.event.get():
            # 게임 종료
            if event.type == pygame.QUIT:  
                done = True
                pygame.quit()
                sys.exit()
            
            # 버튼이 눌렸을때로 변경 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= 5

                elif event.key == pygame.K_RIGHT:
                    x_change += 5
                # 스페이스바 미사일
                elif event.key == pygame.K_SPACE:
                    # 미사일이 2개 미만이면
                    if len(missile_xy) < 2:
                        missile_x = x + shuttle_width / 2#미사일 위치 추가
                        missile_y = y - shuttle_height / 4
                        missile_xy.append([missile_x, missile_y])

        screen.fill((255, 255, 255))

        x += x_change
        if x < 0:
            x = 0
        elif x > screen_width - shuttle_width:
            x = screen_width - shuttle_width

        if y < asteroid_y + asteroid_height:
            if asteroid_x > x and asteroid_x < x + shuttle_width:
                explode()# 우주선 범위에 운석이 닿으면 충돌함수 불러오기

        drawObject(shuttle, x, y)

        if len(missile_xy) != 0:
            for i, bxy in enumerate(missile_xy):
                bxy[1] -= 10#미사일 10픽셀씩 위로 이동
                missile_xy[i][1] = bxy[1]
                
                # 미사일의 y좌표가 운석의 y좌표보다 작으면
                if bxy[1] < asteroid_y:
                    if bxy[0] > asteroid_x and bxy[0] < asteroid_x + asteroid_width:#x좌표가 겹치면
                        missile_xy.remove(bxy)#미사일 제거
                        asteroid_x = random.randrange(0, screen_width - asteroid_width)
                        asteroid_y = 0#운석 위치 조정으로 없어진것처럼
                # y가 0의 위치까지 가면 제거
                if bxy[1] <= 0:
                    try:
                        missile_xy.remove(bxy)
                    except:
                        pass
        # 미사일 리스트에 미사일이 있으면 그리기
        if len(missile_xy) != 0:
            for bx, by in missile_xy:
                drawObject(missile, bx, by)

        asteroid_y += asteroid_speed#운석 이동
        # 맵밖으로 사라지면 지워줌
        if asteroid_y > screen_height:
            asteroid_y = 0
            asteroid_x = random.randrange(0, screen_width - asteroid_width)
        drawObject(asteroid, asteroid_x, asteroid_y)

        pygame.display.update()
        clock.tick(60)

startGame()
runGame()