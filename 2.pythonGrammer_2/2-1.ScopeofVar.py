#======================================================================
# 2.1 변수의 범위(scope)
#======================================================================
x=10
def func():
    print('inside',x)
func()
print('outside',x)
#======================================================================
def func():
    x=10
    print('inside',x)
func()
print('outside',x)
#======================================================================
def func():
    global x
    x=10
    print('inside',x)
func()
print('outside',x)
#======================================================================
x=10
def func():
    x=20
    print('inside',x)
func()
print('outside',x)
#======================================================================
def a():
    x=10
    def b():
        print('inside b()',x)
    b()
    print('inside a()',x)
a()
#======================================================================
def a():
    x=10
    def b():
        x=20
        print('inside b()',x)
    b()
    print('inside a()',x)
a()
#======================================================================
def a():
    x=10
    def b():
        nonlocal x
        x=20
        print('inside b()',x)
    b()
    print('inside a()',x)
a()
#======================================================================
# 2.1 혼자서 해보기
#======================================================================
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

