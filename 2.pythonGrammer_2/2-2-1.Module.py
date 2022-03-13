# 2.2 모듈
# 2-2-1.Module.py

#가._name_변수
# ex가-1
import datetime

def main():
    print('a.py의 모듈이름', __name__)
if __name__=='__main__':
    main()

# ex가-2
import a
if __name__=='__main__':
    a.main()

# ex가-3
#cmd 열어서 python실행하고 기본 디렉토리가 C드라이브 user로 되있어서 책대로 하면 작동이 안될꺼임.
# a.py를 해당 위치로 옮겨주거나 아니면 기본디렉토리를 변경.
#해당 내용은 바로 뒤에 나옴
import a
a.main()