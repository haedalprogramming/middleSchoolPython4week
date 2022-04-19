# 6.2 게임 구현하기
# 가. 게임 기본만들기
# 상하좌우 방향키 입력되는 우주선

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