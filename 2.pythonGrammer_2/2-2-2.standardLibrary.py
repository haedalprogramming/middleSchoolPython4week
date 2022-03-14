# 2.2 표준 라이브러리
# 2-2-1.standardLibrary.py

# # ex1
# import os
# os.getcwd()
# os.chdir('./Python')#본인 컴퓨터에 맞게
# os.getcwd()
# os.system('mkdir today')#today는 파일이름이므로 맘대로 설정

# # ex2
# import shutil
# shutil.copy('copy1.py','./today')#아까만든 폴더
# shutil.move('copy1.py','./today')

# # ex3 
# import sys
# print(sys.argv)
# print('Hello', sys.argv[1])

# # ex4
# import sys
# for i in range(100):
#     print(i)
#     if i == 2:
#         sys.exit()

# # ex5
# import math
# print(math.pi)
# print(math.cos(math.pi/4))
# print(math.log(1024,2))

# # ex6
# from datetime import date
# now=date.today()
# print(now)
# birth=date(2002, 7, 31)
# age=now -birth
# print(age)
# print(age.days//365)

# ex7
import time
print(time.time())
t=time.localtime()
print(t)
print('{}년 {}월 {}일 {}시 {}분'.format(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))
for i in range(10):
    print(i)
    time.sleep(1)