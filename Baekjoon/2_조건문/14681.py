# 14681 번
# 사분면 고르기
# 알고리즘 분류 : 구현, 기하학

x = int(input())
y = int(input())

if (x > 0 and y > 0 ):
    print(1)
elif (x < 0 and y > 0):
    print(2)
elif(x < 0 and y < 0):
    print(3)
elif(x > 0 and y < 0):
    print(4)
