# Assignment Number...: 04
# Student ID..........: 21102240
# Student Name........: 김한결
# File Name...........: leastCommonMultiple.py
# Program Description.:
#최소공배수 구하는 while-else문
#최소공배수란 2개 이상의 수의 공배수 가운데서 최소인 수


def find_num(num1, num2, num3):
  # 세 개의 숫자 중 가장 큰 수를 찾기
  max_num = max(num1, num2, num3)

  # 센티널 변수 i를 초기화
  i = max_num

  while True:
    # 세 숫자로 나누어 나머지가 모두 0이 되면 최소 공배수를 찾은 것이므로 루프를 종료
    if i % num1 == 0 and i % num2 == 0 and i % num3 == 0:
      break
    # 센티널 변수 i를 증가
    i += max_num

  # while 루프가 조건을 만족하지 않고 종료된 경우, 즉 모든 숫자에 대해 나머지가 0이 됐을 때 실행
  print(f"최소 공배수는 {i}입니다.")


# 3개의 정수를 입력
num1 = int(input("첫번째 정수를 입력하세요: "))
num2 = int(input("두번째 정수를 입력하세요: "))
num3 = int(input("세번쨰 정수를 입력하세요: "))

# 함수를 호출하여 최소 공배수를 출력합니다.
find_num(num1, num2, num3)
