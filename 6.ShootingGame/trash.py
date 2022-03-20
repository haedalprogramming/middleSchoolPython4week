import pygame
import random
from time import sleep
import sys

# 전역 변수
screen_width = 480
screen_height = 640
shuttle_width = 53
shuttle_height = 111
asteroid_width = 39
asteroid_height = 22
d_count = 0
s_num = 3


# 게임 초기화 함수
def startGame():
    global screen, clock, shuttle, missile, asteroid

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Saving Earth')
    shuttle = pygame.image.load('shuttle.jpg')
    asteroid = pygame.image.load('ast.png')
    missile = pygame.image.load('mis.png')
    clock = pygame.time.Clock()


# 화면에 객체 그리기
def drawObject(obj, x, y):
    global screen
    screen.blit(obj, (x, y))


# 우주선과 운석 충돌
def explode():
    pygame.display.update()
    sleep(3)
    runGame()


# 점수 출력
def showScore(count):
    global screen
    font = pygame.font.SysFont('malgungothic', 20)
    text = font.render("점수: " + str(count), True, (0, 0, 255))
    screen.blit(text, (0, 0))


# 게임 오버
def gameOver():
    global screen
    font = pygame.font.SysFont('malgungothic', 50)
    if d_count == 100:
        text = font.render("Misssion Complete!", True, (0, 255, 0))
        screen.blit(text, (screen_width / 2 - 210, screen_height / 2 - 30))
    else:
        text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(text, (screen_width / 2 - 150, screen_height / 2 - 30))

    pygame.display.update()
    sleep(2)
    runGame()


# 게임 실행 함수
def runGame():
    global d_count, s_num

    # 미사일 리스트 생성
    missile_xy = []

    # 우주선 좌표
    x = screen_width * 0.40
    y = screen_height * 0.75
    x_change = 0

    # 운석 초기 위치
    asteroid_x = random.randrange(0, screen_width - asteroid_width)
    asteroid_y = 0
    asteroid_speed = 3

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ongame = True
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= 5

                elif event.key == pygame.K_RIGHT:
                    x_change += 5

                elif event.key == pygame.K_SPACE:
                    if len(missile_xy) < 2:
                        missile_x = x + shuttle_width / 2
                        missile_y = y - shuttle_height / 4
                        missile_xy.append([missile_x, missile_y])

        screen.fill((255, 255, 255))

        # 우주선 이동 범위 제한
        x += x_change
        if x < 0:
            x = 0
        elif x > screen_width - shuttle_width:
            x = screen_width - shuttle_width

        # 우주선과 운석 충돌 체크
        if y < asteroid_y + asteroid_height:
            if asteroid_x > x and asteroid_x < x + shuttle_width:
                s_num -= 1
                explode()

        # 게임 오버 조건
        if s_num == 0:
            gameOver()
        if d_count == 100:
            gameOver()

        drawObject(shuttle, x, y)

        # 미사일 이동
        if len(missile_xy) != 0:
            for i, bxy in enumerate(missile_xy):
                bxy[1] -= 10
                missile_xy[i][1] = bxy[1]

                if bxy[1] < asteroid_y:
                    if bxy[0] > asteroid_x and bxy[0] < asteroid_x + asteroid_width:
                        missile_xy.remove(bxy)
                        asteroid_x = random.randrange(0, screen_width - asteroid_width)
                        asteroid_y = 0
                        d_count += 10

                if bxy[1] <= 0:
                    try:
                        missile_xy.remove(bxy)
                    except:
                        pass
        if len(missile_xy) != 0:
            for bx, by in missile_xy:
                drawObject(missile, bx, by)

        showScore(d_count)

        # 운석 이동
        asteroid_y += asteroid_speed
        if asteroid_y > screen_height:
            asteroid_y = 0
            asteroid_x = random.randrange(0, screen_width - asteroid_width)

        drawObject(asteroid, asteroid_x, asteroid_y)

        pygame.display.update()
        clock.tick(60)


startGame()
runGame()
