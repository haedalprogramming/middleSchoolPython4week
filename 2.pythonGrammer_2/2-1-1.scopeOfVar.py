# 2.1 변수의 범위(scope)
# 2-1-1.scopeOfVar.py

# ex1
x=10
def func():
    print('inside',x)
func()
print('outside',x)

# ex2
def func():
    x=10
    print('inside',x)
func()
print('outside',x)

# ex3
def func():
    global x
    x=10
    print('inside',x)
func()
print('outside',x)

# ex4
x=10
def func():
    x=20
    print('inside',x)
func()
print('outside',x)

# ex5
def a():
    x=10
    def b():
        print('inside b()',x)
    b()
    print('inside a()',x)
a()

# ex6
def a():
    x=10
    def b():
        x=20
        print('inside b()',x)
    b()
    print('inside a()',x)
a()

# ex7
def a():
    x=10
    def b():
        nonlocal x
        x=20
        print('inside b()',x)
    b()
    print('inside a()',x)
a()