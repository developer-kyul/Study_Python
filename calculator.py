# Assignment Number...: 05
# Student ID..........: 21102240
# Student Name........: 김한결
# File Name...........: calculator.py
# Program Description.:
# 계산기 구현하기
# 연산자와 정수 두 개를 입력받아 수치 연산을 수행한 후 결과를 반환하는 calculator 함수를 구현
# 함수를 정의할 때 세 개의 매개함수를 아래 순서로 정의
# operator, integer1, integer2
# ๏만약 operator가 'add'이면, 두 정수에 더하기 연산을 수행 : integer1 + integer2
# ๏만약 operator가 'sub'이면, 두 정수에 빼기 연산을 수행 : integer1 - integer2
# ๏만약 operator가 'mul'이면, 두 정수에 곱하기 연산을 수행 : integer1 * integer2
# ๏만약 operator가 'div'이면, 두 정수에 나누기 연산을 수행 : integer1 / integer2

def calculator(operator, integer1, integer2):
    if operator == 'add':
        return integer1 + integer2
    elif operator == 'sub':
        return integer1 - integer2
    elif operator == 'mul':
        return integer1 * integer2
    elif operator == 'div':
        return integer1 / integer2
    else:
        return f"{operator} is not supported." 