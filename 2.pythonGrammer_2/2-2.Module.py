#======================================================================
# 2.2 모듈
#가._name_변수
#======================================================================
import datetime


def main():
    print('a.py의 모듈이름', __name__)
if __name__=='__main__':
    main()
#======================================================================
import a
if __name__=='__main__':
    a.main()
# ======================================================================
#cmd 열어서 python실행하고 기본 디렉토리가 C드라이브 user로 되있어서 책대로 하면 작동이 안될꺼임.
# a.py를 해당 위치로 옮겨주거나 아니면 기본디렉토리를 변경.
#해당 내용은 바로 뒤에 나옴
import a
a.main()
#======================================================================
# 2.2 표준 라이브러리
#======================================================================
import os
os.getcwd()
os.chdir('./Python')#본인 컴퓨터에 맞게
os.getcwd()
os.system('mkdir today')#today는 파일이름이므로 맘대로 설정
#======================================================================
import shutil
shutil.copy('copy1.py','./today')#아까만든 폴더
shutil.move('copy1.py','./today')
#======================================================================
import sys
print(sys.argv)
print('Hello', sys.argv[1])
#======================================================================
import sys
for i in range(100):
    print(i)
    if i == 2:
        sys.exit()
#======================================================================
import math
print(math.pi)
print(math.cos(math.pi/4))
print(math.log(1024,2))
#======================================================================
from datetime import date
now=date.today()
print(now)
birth=date(2002, 7, 31)
age=now -birth
print(age)
print(age.days//365)
#======================================================================
import time
print(time.time())
t=time.localtime()
print(t)
print('{}년 {}월 {}일 {}시 {}분'.format(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))
for i in range(10):
    print(i)
    time.sleep(1)