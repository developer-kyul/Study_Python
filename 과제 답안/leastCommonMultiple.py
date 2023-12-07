# --- 세 정수의 최소 공배수를 구하는 while문 작성하기

prompt = '{} 정수를 입력하세요: '

x = int(input(prompt.format('첫번째')))

y = int(input(prompt.format('두번째')))

z = int(input(prompt.format('세번째')))

i = 1

while i % x != 0 or i % y != 0 or i % z != 0:

    i += 1

else:

    print(f'최소공배수는 {i}입니다.')