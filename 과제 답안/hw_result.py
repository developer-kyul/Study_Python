#####1번 과제 
### input()함수를 통해 입력을 받는다
##  이때 입력받은 함수는 정수로 출력받도록 int 함수를 이용한다
a = int(input("직각을 낀 첫 번째 변의 길이를 입력하세요"))
b = int(input("직각을 낀 두 번째 변의 길이를 입력하세요"))

#넓이를 구하는 공식 
x = 0.5 * a * b

#빗변의 길이를 구하는 공식
y = (a**2 + b**2)**0.5

##문자열의 format() 메소드나 f-string을 사용해 결과를 출력한다.
# 가독성을 위해서 f-string를 사용
print(f"넓이는 {x}, 빗변의 길이는 {y}입니다.")

############2번 과제
# 수정 전 학생 성적 정보를 출력한다.
print('=' * 5 ,'수정 전 학생 성적 정보', '=' * 15)
print(students, end='\n\n')  # 출력 후 한줄 더 줄 바꾸기를 한다.

# ----- 중간고사 이후 변화 처리 -------------------------------------------------- #
del students[1]              # Chris 삭제 이후 Diana, Irene의 인덱스 변경에 유의한다.

students[1]['중간고사'] = 90   # Diana의 중간고사 점수를 수정한다(인덱스 변경에 유의).
# 바로 위 수정 사항은 students[1]['중간고사'] -= 5 등 다른 방법을 사용해도 된다.

students[2]['결석 횟수'] = 1   # Irene 결석 횟수를 수정한다(인덱스 변경의 유의).
# 바로 위 수정 사항은 students[2]['결석 횟수'] += 1 등 다른 방법을 사용해도 된다.

students[0]['기말고사'] = 85   # Bob의 기말고사 결과를 추가한다,
students[1]['기말고사'] = 100  # Diana 기말고사 결과를 추가한다.
students[2]['기말고사'] = 30   # Irene 기말고사 결과를 추가한다.

# 수정 후 학생 성적 정보를 출력한다.
print('=' * 5, '수정 후 학생 성적 정보', '=' * 15)
print(students)

# !!!!! END OF students_grades.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



################3번 과제
#학생들에게 중간고사와 기말고사 성적을 묻는다
a = int(input("당신의 중간 고사 점수는 몇 점입니까?"))
b = int(input("당신의 기말 고사 점수는 몇 점입니까?"))

#두 개의 성적을 값을 구한다
if a >=60 :
    if b >= 80 :
        print("당신의 성적은 A+입니다")
    elif b < 80 and b >= 70 :
        print("당신의 성적은 A0입니다")
    elif b < 70 and b >= 60 :
        print("당신의 성적은 A-입니다")
    else :
        print("당신의 성적은 C+입니다")
else : 
    if b >= 90 :
        print("당신의 성적은 A-입니다")
    elif b < 90 and b >= 80 :
        print("당신의 성적은 B+입니다")
    elif b < 80 and b >= 70 :
        print("당신의 성적은 B0입니다")
    else :
        print("당신의 성적은 C+입니다")

##############4번 과제
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


##################5번 과제
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
    


###########기말고사 정리
    
# 시험범위 정리 2, 3, 4

#인덱스
s = "안녕 파이썬"
print(s[0])

#길이 출력
len(s)

#문자열분할
#문자열 [시작: 끝 : 폭]
#s[0,3,2]

#문자열.split(spe="", maxsplit=-1)
#기본값인 -1이 주어지면 구분자 spe만큼 모두 분할
kor="파이썬을 배우면서 파이썬을 즐기자"
kor.split('을',1)
kor.rsplit('을',1)

# 시험범위 정리 9, 10, 11

#단순if - else
i = int(input('숫자(정수)를 입력하세요: '))
if i>0 :
    print('입력한 숫자는 양의 정수입니다.')
else: 
    print('입력한 숫자는 양의 정수가 아닙니다.')

#if - elif - else
prompt = "정수를 입력하세요 : "
result = "둘 중 더 큰 수는 {}입니다."

x=int(input(prompt))
y=int(input(prompt))

if x > y : 
    print(result.format(x))
elif x<y :
    print(result.format(y))
else:
    print("같은 숫자군요.")



#중첩 if문
#학생들에게 중간고사와 기말고사 성적을 묻는다
a = int(input("당신의 중간 고사 점수는 몇 점입니까?"))
b = int(input("당신의 기말 고사 점수는 몇 점입니까?"))

#두 개의 성적을 값을 구한다
if a >=60 :
    if b >= 80 :
        print("당신의 성적은 A+입니다")
    elif b < 80 and b >= 70 :
        print("당신의 성적은 A0입니다")
    elif b < 70 and b >= 60 :
        print("당신의 성적은 A-입니다")
    else :
        print("당신의 성적은 C+입니다")
else : 
    if b >= 90 :
        print("당신의 성적은 A-입니다")
    elif b < 90 and b >= 80 :
        print("당신의 성적은 B+입니다")
    elif b < 80 and b >= 70 :
        print("당신의 성적은 B0입니다")
    else :
        print("당신의 성적은 C+입니다")




#순환문 Looping
total = 0 
i = 0

#while -> 시험 x
#명령문을 10회 반복해서 수행한 후 종료
while i < 10:
    i+=1
    total +=i
else : 
    print(f'1부터 10까지의 합은 {total}입니다')

#for
#for 변수 in 순회형 : for-명령문
t = 0,1,2,3,4,5
for i in t: 
    print(i)


#range()
range()
range(끝번호)
range(시작번호, 끝번호)
range(시작번호, 끝번호, 폭)

#원하는 만큼 반복하는 for문

#예제1
n=int(input('반복 횟수를 입력하세요'))
for i in range(1, n+1):
    print('#'*i)

#예제2
total = 0
for i in  range(1,11):
    total += i
else:
    print(f'1부터 10까의 합은 {total}입니다')

#예제3
colors ="red", "blue", "pink", "green", "yellow", "purple"

for color in colors :
    if color.startswith("p"):
        print(color)
else:
    print("더이상 없음")

#예제4
color ="하양", "까망"
taste = "달콤한", "짭짤한"
food = "라면", "피자"

for c in color: 
    for t in  taste:
        for f in food:
            print(f"{c} {t} {f}")

#예제5 구구단
for i in range(2,10):
    for j in range(1,10):
        print(f'{i} x {j} =' , i*j)


#예제6 윤년계산기
leaps = []

for year in range(2001,3001):
    if year % 4 == 0 and year % 100 !=0 or year % 400 ==0:
        leaps.append(year)
else: 
    print(leaps)

#예제7
salary = {
    'david': 3000,
    'davia': 4000,
    'davib': 5000,
    'davic': 6000,
    'david': 7000,
}

for i in salary :
    if salary[i] >= 3000:
        print(f"{i}'s salary is {salary[i]:,}")


#예제8
x=('a', 'b', 'c')
y=['i','j','k','l']
z='12345'

for t in zip(x,y,z):
    print(t)

type(zip(x,y,z)) #class zip

#unzip
x,y =zip(*k)




