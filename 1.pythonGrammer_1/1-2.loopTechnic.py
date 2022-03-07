#======================================================================
# 1.2 내장함수 활용하기
#======================================================================
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

fruit = ['Apple', 'Banana', 'Grape']
color = ['red', 'yellow', 'purple']
for f, c in zip(fruit, color):
    print('{}s are {}'.format(f,c))

basket = ['apple', 'orange', 'pear', 'banana']
basket.sort()
print(basket)
for f in reversed(basket):
    print(f)

basket = ['apple', 'orange', 'apple', 'pear', 'banana']
for f in sorted(set(basket)):
    print(f)
#======================================================================
# 1.2 중첩 루프
#======================================================================
for i in range(2, 10):
    for j in range(1, 10):
        print('{}x{}={}'.format(i,j,i*j))

combs=[]
for x in [1,2,3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x,y))
print(combs)

combs=[(x,y) for x in [1,2,3] for y in [3,1,4]
       if x !=y]
print(combs)
#======================================================================
# 1.2 혼자서 해보기
#======================================================================
row, colum = input("행과 열을 입력하세요:").split()
for i in range(1, int(row) + 1):
    for j in range(1, int(colum) + 1):
        print(i * j, end=' ')
    print()


