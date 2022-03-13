# 1.1 다.리스트 컴프리헨션(Comprehensions)
# 1-1-5.listComprehensions.py

# 첫번째 예시
for i in ['a', 'b', 'c']:
    print(i)

nums = [i for i in range(10)]
print(nums)

# 두번째 예시
even_nums = []
for i in range(1, 11):
    if i % 2 == 0:
        even_nums.append(i)
print(even_nums)

# 세번째 예시
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

# 네번째 예시
vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])
