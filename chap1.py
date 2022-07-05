"""
    Project : First python program study
    Author : Ryun-Hyeong Kim
    Date of last : 2022-07-05
"""

'''
1. 데이터 입력 기능 연산
'''
x = int(input("input x = "))
y = int(input("input y = "))

sum_xy = x + y
sub_xy = x - y
mul_xy = x * y
div_xy = x / y
int_div_xy = x // y
print(sum_xy)
print(sub_xy)
print(mul_xy)
print(div_xy)
print(int_div_xy)

'''
2. 다양한 자료형 변수 선언 및 사용
'''
x = 1 #integer
print("x = ", x)
print("type(x) = ", type(x))

x = 2.33 #float
print("x = ", x)
print("type(x) = ", type(x))

x = [1,2,3] #list
print("x = ", x)
print("type(x) = ", type(x))

x = (1,2,3) #tuple
print("x = ", x)
print("type(x) = ", type(x))

x = {'A':1,'B':2,'c':3} #dictionary
print("x = ", x)
print("type(x) = ", type(x))

x = {1,2,3,4} #set
print("x = ", x)
print("type(x) = ", type(x))

'''
3. 출력 포맷 지정
'''