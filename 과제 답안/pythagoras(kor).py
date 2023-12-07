"""
File name.....: pythagoras.py
Module name...: 5 - Basic Data Types
Description...: This program computes height and hypotenuse lengths of a
                right-angled triangle.
"""

__author__ = 'Jihae Suh'
__version__ = '0.2'
__email__ = 'jihae@seoultech.ac.kr'


# 직각삼각형에서 직각을 낀 두 변의 길이를 입력받는다.
x = int(input('직각을 낀 첫 번째 변의 길이를 입력하세요 : '))
y = int(input('직각을 낀 두 번째 변의 길이를 입력하세요 : '))

# 넓이와 빗변의 길이를 계산한다.
area = 1/2 * x * y
hypotenuse = (x ** 2 + y ** 2) ** (1/2)

# 결과를 출력한다.
print(f'넓이는 {area}, 빗변의 길이는 {hypotenuse}입니다.')

# !!!!! END OF pythagoras.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
