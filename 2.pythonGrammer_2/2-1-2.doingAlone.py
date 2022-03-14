# 2.1 혼자서 해보기
# 아래 스크립트의 실행 결과를 예측 해보자.

def scope_test():
    def do_local():
        x='local x'
    def do_nonlocal():
        nonlocal x
        x= 'nonlocal x'
    def do_global():
        global x
        x= 'global x'
    x='test x'
    do_local()
    print('After local assignment:',x)
    do_nonlocal()
    print('After nonlocal assignment:',x)
    do_global()
    print('After global assignment:',x)
scope_test()
print('in global scope:',x)