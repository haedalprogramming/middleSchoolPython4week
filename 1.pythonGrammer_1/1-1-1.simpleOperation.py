# 1.1 기본적인 연산
# 1-1-1.simpleOperation.py

# 첫번째 예시
squares = [1, 4, 9, 16]
print(squares)
print(squares + [25, 36])
print(squares * 2)
print(squares[0])
print(squares[-1])
print(squares[:])

# 두번째 예시
letters = list('abcdefg')
print(letters)
letters[2:5]=['C','D','E']
print(letters)
print(len(letters))
letters[:]=[]
print(letters)
# del letters
# print(letters)
