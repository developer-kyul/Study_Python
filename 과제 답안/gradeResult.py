# 사용자로부터 점수를 받는다

 

midterm_score = int(input("당신의 중간 고사 점수는 몇 점입니까? "))

final_score = int(input("당신의 기말 고사 점수는 몇 점입니까? "))

 

#중첩 if문을 사용하여 점수를 계산한다. 

 

if midterm_score >= 60:

    if final_score >= 80:

        final_grade = 'A+'

    elif final_score >= 70:

        final_grade = 'A0'

    elif final_score >= 60:

        final_grade = 'A-'

    else:

        final_grade = 'C+'

else:

    if final_score >= 90:

        final_grade = 'A-'

    elif final_score >= 80:

        final_grade = 'B+'

    elif final_score >= 70:

        final_grade = 'B0'

    else:

        final_grade = 'C+'

 

# 마지막 점수값을 나오게 한다. 

 

print(f"당신의 최종성적은 {final_grade}입니다.")

 