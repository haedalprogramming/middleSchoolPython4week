# 4-2-4.dataRestoration.py
# 파이게임에서 이미지의 원본을 유지해야할까?
# 복원할 데이터의 원본이 없는 예시

screen = [1, 1, 2, 2, 2, 1]
print(screen)
playerpos = 3
screen[playerpos] = 8
print(screen)
playerpos -= 1
screen[playerpos] = 8
print(screen)