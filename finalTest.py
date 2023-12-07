#일시: 12월 16일 토요일 오전 10~11시30분 (90분)
#장소: 어의관 104호
#준비물: 개인 노트북
#시험 범위: 지금까지 배운 모든 범위이지만, 중간고사 이후에 배운 것
#시험 형식: 실습 문제 3문제, 부분점수 없음
#-문제 1: 조건문 if (7점)
#-문제 2: for 문 (8점)
#-문제 3: function 함수 (10점)


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

# 시험범위 정리 12


# 시험범위 정리 13
