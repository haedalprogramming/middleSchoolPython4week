# 1.2 내장함수 활용하기
# 1-2-1.builtInFunction.py

# 첫번째 예시
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 두번째 예시
fruit = ['Apple', 'Banana', 'Grape']
color = ['red', 'yellow', 'purple']
for f, c in zip(fruit, color):
    print('{}s are {}'.format(f,c))

# 세번째 예시
basket = ['apple', 'orange', 'pear', 'banana']
basket.sort()
print(basket)
for f in reversed(basket):
    print(f)

# 네번째 예시
basket = ['apple', 'orange', 'apple', 'pear', 'banana']
for f in sorted(set(basket)):
    print(f)