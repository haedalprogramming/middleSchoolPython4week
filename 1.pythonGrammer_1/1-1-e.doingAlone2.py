# 두번째 문제
# fruit = ['apple', 'strawberry', 'melon', 'orange', 'banana', 'grape'] 
# 1. fruit 리스트의 각 항목의 길이로 새로운 리스트를 만들어보자.
# 결과> fruit_len = [5, 10, 5, 6, 6, 5]
# 2. fruit 리스트의 항목의 길이가 5인 항목만으로 구성된 리스트를 만들어보자.
# 결과> result = ['apple', 'melon', 'grape']

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