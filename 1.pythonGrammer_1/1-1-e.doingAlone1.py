# 첫번째 문제
# 최대 100개의 정수를 입력받을 수 있으며, 
# 정수를 입력 받다가 ‘q'가 입력되면 입력을 중단하고, 
# 입력된 수 중 마지막 세 개의 수를 출력하는 스크립트를 작성해보자.

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