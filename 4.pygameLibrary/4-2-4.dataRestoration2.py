# 4-2-4.dataRestoration2.py
# 파이게임에서 이미지의 원본을 유지해야할까?
# 복원할 데이터의 원본이 있는 예시
background = [1, 1, 2, 2, 2, 1]
screen = [0]*6
for i in range(6):
    screen[i] = background[i]

print(screen)
playerpos = 3
screen[playerpos] = 8
print(screen)
screen[playerpos] = background[playerpos]
playerpos -= 1
screen[playerpos] = 8
print(screen)
print("원본: ", background)