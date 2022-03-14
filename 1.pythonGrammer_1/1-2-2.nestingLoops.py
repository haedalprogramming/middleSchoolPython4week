# 1.2 중첩 루프
# 1-2-2.nestingLoops.py

# ex1
for i in range(2, 10):
    for j in range(1, 10):
        print('{}x{}={}'.format(i,j,i*j))

# ex2
combs=[]
for x in [1,2,3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x,y))
print(combs)

# ex3
combs=[(x,y) for x in [1,2,3] for y in [3,1,4]
       if x !=y]
print(combs)