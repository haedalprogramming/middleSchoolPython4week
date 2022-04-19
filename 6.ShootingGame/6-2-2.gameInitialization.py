# 나. 게임 초기화하기 
# 우주선 좌우 이동 + 가속도

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