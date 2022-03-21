#======================================================================
# 6.2 게임 구현하기
# 가. 게임 기본만들기
#======================================================================
import pygame
import sys

pygame.init() # 초기화
pygame.display.set_caption("saving Earth") # 게임 이름 써주기
screen_width = 400 # 넓이 설정
screen_height = 560 # 높이 설정
screen = pygame.display.set_mode((screen_width, screen_height)) # 넓이와 높이를 값으로 가지는 화면크기 생성
done = False # 게임 끝남
x = screen_width * 0.4 # 아래 코드에서 x좌표를 이미지의 left로 잡았으므로 0.4로해야 중앙배치
y = screen_height * 0.8 # 위아래 높이가 긴편이니까 0.8

clock = pygame.time.Clock() # 게임속도 조절을 위한 clock선언

img = pygame.image.load("shuttle.jpg") # 우주선 이미지

rect = img.get_rect()

# 게임이 끝나지 않았을때
while not done:
    for event in pygame.event.get():
        # 게임 종료
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()

        rect.left = x
        rect.top = y

        pressed = pygame.key.get_pressed() # 상하좌우 이동
        if pressed[pygame.K_UP]:
            y -= 10
        if pressed[pygame.K_DOWN]:
            y += 10
        if pressed[pygame.K_LEFT]:
            x -= 10
        if pressed[pygame.K_RIGHT]:
            x += 10

        screen.fill((255, 255, 255))
        screen.blit(img, rect)

        pygame.display.flip()
        clock.tick(60)
#======================================================================
# 나. 게임 초기화하기 
# 우주선 좌우 이동 + 가속도
#======================================================================
import pygame
import sys

# 화면 넓이 높이 우주선 넓이 높이를 사용하기 좋게 전역변수로 선언해준다.
screen_width = 480
screen_height = 640
shuttle_width = 53
shuttle_height = 111

# 게임 초기화를 함수로
def startGame():
    global screen, clock, shuttle
    pygame.init()  # 초기화
    screen = pygame.display.set_mode((screen_width, screen_height)) # 넓이와 높이를 값으로 가지는 화면크기 생성
    pygame.display.set_caption("saving Earth") # 게임 이름 써주기
    shuttle = pygame.image.load('shuttle.jpg')
    clock = pygame.time.Clock()

# 스프라이트 그리기 함수
def drawObject(obj, x, y):
    global screen
    screen.blit(obj, (x, y))

# 게임 실행 함수
def runGame():
    x = screen_width * 0.4  #우주선 좌표
    y = screen_height * 0.8
    x_change = 0

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

        screen.fill((255, 255, 255))

        x += x_change
        if x < 0:
            x = 0
        elif x > screen_width - shuttle_width:
            x = screen_width - shuttle_width

        drawObject(shuttle, x, y)

        pygame.display.update()
        clock.tick(60)

startGame()
runGame()
#======================================================================
#다. 미사일 발사
#======================================================================
import pygame
import sys

# 화면 넓이 높이 우주선 넓이 높이를 사용하기 좋게 전역변수로 선언해준다.
screen_width = 480 
screen_height = 640
shuttle_width = 53
shuttle_height = 111

# 게임 초기화를 함수로
def startGame():
    global screen, clock, shuttle, missile

    pygame.init()  # 초기화
    screen = pygame.display.set_mode((screen_width, screen_height)) # 넓이와 높이를 값으로 가지는 화면크기 생성
    pygame.display.set_caption("saving Earth") # 게임 이름 써주기
    shuttle = pygame.image.load('shuttle.jpg')
    missile = pygame.image.load('mis.png')
    clock = pygame.time.Clock()

# 스프라이트 그리기 함수
def drawObject(obj, x, y):
    global screen
    screen.blit(obj, (x, y))

# 게임 실행 함수
def runGame():
    missile_xy = [] # 미사일 리스트 생성

    x = screen_width * 0.4 # 우주선 좌표
    y = screen_height * 0.8
    x_change = 0

    done = False
    # 게임이 끝나지 않았을때
    while not done:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 게임 종료
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
                        missile_x = x + shuttle_width / 2 # 미사일 위치 추가
                        missile_y = y - shuttle_height / 4
                        missile_xy.append([missile_x, missile_y])

        screen.fill((255, 255, 255))

        x += x_change
        if x < 0:
            x = 0
        elif x > screen_width - shuttle_width:
            x = screen_width - shuttle_width

        drawObject(shuttle, x, y)

        if len(missile_xy) != 0:
            for i, bxy in enumerate(missile_xy):
                bxy[1] -= 10 # 미사일 10픽셀씩 위로 이동
                missile_xy[i][1] = bxy[1]
                
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

        pygame.display.update()
        clock.tick(60)

startGame()
runGame()
#======================================================================
#라. 운석 만들기
#======================================================================
import pygame
import random
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
                        missile_x = x + shuttle_width / 2 # 미사일 위치 추가
                        missile_y = y - shuttle_height / 4
                        missile_xy.append([missile_x, missile_y])

        screen.fill((255, 255, 255))

        x += x_change
        if x < 0:
            x = 0
        elif x > screen_width - shuttle_width:
            x = screen_width - shuttle_width

        drawObject(shuttle, x, y)

        if len(missile_xy) != 0:
            for i, bxy in enumerate(missile_xy):
                bxy[1] -= 10 # 미사일 10픽셀씩 위로 이동
                missile_xy[i][1] = bxy[1]

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

        asteroid_y += asteroid_speed # 운석 이동
        # 맵밖으로 사라지면 지워줌
        if asteroid_y > screen_height:
            asteroid_y = 0
            asteroid_x = random.randrange(0, screen_width - asteroid_width)
        drawObject(asteroid, asteroid_x, asteroid_y)

        pygame.display.update()
        clock.tick(60)

startGame()
runGame()
#======================================================================
# 마. 충돌처리
# 우주선과 운석 충돌처리
#======================================================================
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

        asteroid_y += asteroid_speed # 운석 이동
        # 맵밖으로 사라지면 지워줌
        if asteroid_y > screen_height:
            asteroid_y = 0
            asteroid_x = random.randrange(0, screen_width - asteroid_width)
        drawObject(asteroid, asteroid_x, asteroid_y)

        pygame.display.update()
        clock.tick(60)

startGame()
runGame()
#======================================================================
# 바. 미사일 맞은 운석처리
# 미사일과 운석 충돌처리
#======================================================================
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
#======================================================================
# 사. 운석처리 점수 
# 미사일로 운석을 맞출때마다 10점
#======================================================================
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
d_count = 0#운석처리 점수 선언

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

# 점수출력
def showScore(count):
    global screen
    font = pygame.font.SysFont('malgungothic',20)
    text = font.render("Score: " +str(count), True, (0, 0, 255))
    screen.blit(text, (0, 0))
# 게임 실행 함수
def runGame():
    global d_count # 점수를 위해 전역변수
    missile_xy = [] # 미사일 리스트 생성

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
                        d_count += 10#운석 제거시 점수 증가
                
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
        showScore(d_count)#운석처리한 갯수 곱하기 10만큼 점수 출력

        pygame.display.update()
        clock.tick(60)

startGame()
runGame()
#======================================================================
# 아. 게임 종료 조건
#======================================================================
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
d_count = 0#운석처리 점수 선언
s_num = 3#폭파 3번

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
    font = pygame.font.SysFont('malgungothic', 50)
    text = font.render("Play Again", True, (255, 0, 0))
    screen.blit(text, (screen_width/2 - 150, screen_height/2 - 30))
    pygame.display.update()
    sleep(3)
    runGame()


# 점수출력
def showScore(count):
    global screen
    font = pygame.font.SysFont('malgungothic',20)
    text = font.render("점수" +str(count), True, (0, 0, 255))
    screen.blit(text, (0, 0))

def gameOver():
    global screen
    font = pygame.font.SysFont('malgungothic', 50)
    if d_count == 100:
        text = font.render("Mission Complete!", True, (0, 255, 0))
        screen.blit(text, (screen_width/2 - 210, screen_height/2 - 30))
    else:
        text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(text, (screen_width/2 - 150, screen_height/2 - 30))

    pygame.display.update()
    sleep(2)
    runGame()

# 게임 실행 함수
def runGame():
    global d_count, s_num # 점수를 위해 전역변수, 게임 종료를위한 폭파횟수

    missile_xy = [] # 미사일 리스트 생성

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
                s_num -= 1#목숨 1감소
                explode()# 우주선 범위에 운석이 닿으면 충돌함수 불러오기

        # 우주선 폭파 3회되면
        if s_num == 0:
            gameOver()
        # 점수가 100점 이상인 경우
        if d_count == 100:
            gameOver()

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
                        d_count += 10#운석 제거시 점수 증가
                
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

        showScore(d_count)#점수 보여주기

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
#======================================================================
#자. 소리 효과 넣기
#======================================================================
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
d_count = 0#운석처리 점수 선언
s_num = 3#폭파 3번

# 게임 초기화를 함수로
def startGame():
    global screen, clock, shuttle, missile, asteroid, s_shot, s_explode, s_destroy

    pygame.init()  # 초기화
    screen = pygame.display.set_mode((screen_width, screen_height))#넓이와 높이를 값으로 가지는 화면크기 생성
    pygame.display.set_caption("saving Earth")#게임 이름 써주기
    shuttle = pygame.image.load('shuttle.jpg')
    asteroid = pygame.image.load('ast.png')
    missile = pygame.image.load('mis.png')
    s_shot = pygame.mixer.Sound('shot.wav')#소리 클립들 추가
    s_explode = pygame.mixer.Sound('big.wav')
    s_destroy = pygame.mixer.Sound('small.wav')
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

# 점수출력
def showScore(count):
    global screen
    font = pygame.font.SysFont('malgungothic',20)
    text = font.render("Score: " +str(count), True, (0, 0, 255))
    screen.blit(text, (0, 0))

def gameOver():
    global screen
    font = pygame.font.SysFont('malgungothic', 50)
    if d_count == 100:
        text = font.render("Mission Complete!", True, (0, 255, 0))
        screen.blit(text, (screen_width/2 - 210, screen_height/2 - 30))
    else:
        text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(text, (screen_width/2 - 150, screen_height/2 - 30))

    pygame.display.update()
    sleep(2)
    runGame()

# 게임 실행 함수
def runGame():
    global d_count, s_num#점수를 위해 전역변수, 게임 종료를위한 폭파횟수

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
                    s_shot.play()#미사일 발사 효과음
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
                s_num -= 1#목숨 1감소
                s_explode.play()#우주선 폭파 효과음
                explode()# 우주선 범위에 운석이 닿으면 충돌함수 불러오기
        
        # 우주선 폭파 3회되면
        if s_num == 0:
            gameOver()
        # 점수가 100점 이상인 경우
        if d_count == 100:
            gameOver()

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
                        d_count += 10#운석 제거시 점수 증가
                        s_destroy.play()#운석 제거시 효과음
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

        showScore(d_count)#점수 보여주기

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