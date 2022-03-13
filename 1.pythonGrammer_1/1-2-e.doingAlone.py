# 1.2 혼자서 해보기
# 1-2-e.doingAlone.py

# 행과 열의 수를 입력 받아 아래와 같이 출력하는 프로그램을 만들어보자.
# 입력 예> 3 4 
# 출력 예> 1 2 3 4
#         2 4 6 8 
#         3 6 9 12


row, colum = input("행과 열을 입력하세요:").split()
for i in range(1, int(row) + 1):
    for j in range(1, int(colum) + 1):
        print(i * j, end=' ')
    print()