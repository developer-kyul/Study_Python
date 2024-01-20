# Assignment Number...: 03
# Student ID..........: 21102240
# Student Name........: 김한결
# File Name...........: pythagoras.py
# Program Description.:
#성적산출
#if문 사용 

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
