# ======================================================================
# 1.1 기본적인 연산
# ======================================================================
squares = [1, 4, 9, 16]
print(squares)
print(squares + [25, 36])
print(squares * 2)
print(squares[0])
print(squares[-1])
print(squares[:])
# ======================================================================
letters = list('abcdefg')
print(letters)
letters[2:5]=['C','D','E']
print(letters)
print(len(letters))
letters[:]=[]
print(letters)
#del letters
#print(letters)
# ======================================================================
# 1.1 메서드를 사용하는 예
# ======================================================================
fruits = ['orange', 'apple', 'pear', 'banana', 'apple']
print(fruits.count('apple'))
print(fruits.index('banana'))
print(fruits.index('apple', 3))
fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
print(fruits.pop())
# ======================================================================
# 1.1 가.리스트를 스택으로 사용하기
# ======================================================================
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)
# ======================================================================
# 1.1 나.리스트를 큐로 사용하기
# ======================================================================
queue = [3, 4, 5]
queue.append(6)
queue.append(7)
print(queue)
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue)
# ======================================================================
# 1.1 다.리스트 컴프리헨션(Comprehensions)
# =======================================================================
for i in ['a', 'b', 'c']:
    print(i)

nums = [i for i in range(10)]
print(nums)
# ======================================================================
even_nums = []
for i in range(1, 11):
    if i % 2 == 0:
        even_nums.append(i)
print(even_nums)
# ======================================================================
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
# ======================================================================
vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])
# ======================================================================
# 1.1 혼자서 해보기

# 첫번째 문제
# 최대 100개의 정수를 입력받을 수 있으며, 
# 정수를 입력 받다가 ‘q'가 입력되면 입력을 중단하고, 
# 입력된 수 중 마지막 세 개의 수를 출력하는 스크립트를 작성해보자.
# ======================================================================
nums=[]
boolBreak=0
for i in range(1, 101):
    nums.append(input("%d번째 숫자를 입력" %i))
    if nums[i-1]=="q":
        boolBreak=1
        break
if(boolBreak==1):
    if(i<4):
        nums.pop()
        print(nums[0:i])
    else:
        nums.pop()
        print(nums[i-4:i])
else:
    print(nums[i-3:i+1])
#======================================================================
# 두번째 문제
# fruit = ['apple', 'strawberry', 'melon', 'orange', 'banana', 'grape'] 
# 1. fruit 리스트의 각 항목의 길이로 새로운 리스트를 만들어보자.
# 결과> fruit_len = [5, 10, 5, 6, 6, 5]
# 2. fruit 리스트의 항목의 길이가 5인 항목만으로 구성된 리스트를 만들어보자.
# 결과> result = ['apple', 'melon', 'grape']
#======================================================================
fruit=['apple', 'strawberry', 'melon', 'orange', 'banana', 'grape']
fruit_len=[]
result=[]
for i in range(len(fruit)):
    fruit_len.append(len(fruit[i]))
print(fruit_len)

for i in range(len((fruit))):
    if len(fruit[i]) == 5:
        result.append(fruit[i])
print(result)

