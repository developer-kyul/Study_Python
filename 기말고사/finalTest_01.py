# Assignment Number...: Final Test 01
# Student ID..........: 21102240
# Student Name........: 김한결
# File Name...........: finalTest_01
# Program Description.: 


gpa = float(input("학점(GPA)을 입력하세요"))
if gpa >= 3.3 :
    print ("축하합니다! 다음 단계를 진행하세요")
    toeic = int(input("토익(TOEIC) 점수를 입력하세요"))
    if toeic >= 800 : 
        print ("축하합니다! 다음 단계를 진행하세요")
        work = input("근무 경력이 있습니까(예/아니요)?")
        if work == "예" :
            print ("축하합니다! 당신의 지원서를 인사과에서 검토할 예정입니다.")
else: 
    print("죄송합니다. 당신은 최소 요구 조건을 만족하지 못했습니다.")
