#1 If Statement 
gpa = float(input("학점(GPA)을 입력하세요: "))

if gpa >= 3.3:
    print("축하합니다! 다음 단계를 진행하세요.")
    toeic_score = int(input("토익(TOEIC) 점수를 입력하세요: "))
    if toeic_score >= 800:
        print("축하합니다! 다음 단계를 진행하세요.")
        work_experience = input("근무 경력이 있습니까(예/아니요): ")
        if work_experience == '예':
            print("축하합니다! 당신의 지원서를 인사과에서 검토할 예정입니다")
        else:
            print("죄송합니다. 당신은 최소 요구 조건을 만족하지 못했습니다.")
    else:
        print("죄송합니다. 당신은 최소 요구 조건을 만족하지 못했습니다.")
else:
    print("죄송합니다. 당신은 최소 요구 조건을 만족하지 못했습니다.")



#2 특정 속성을 만족하는 제품을 출력하는 for-else문 작성하기
products = [
    {'name': '노트북', 'category': '전자기기', 'price': 1000000},
    {'name': '키보드', 'category': '컴퓨터 액세서리', 'price': 50000},
    {'name': '마우스', 'category': '컴퓨터 액세서리', 'price': 25000},
   ]

for product in products:
    if product['category'] == '전자기기' and product['price'] < 5000000:
        print(product['name'])
else:
    print("더 이상 조건에 맞는 제품이 없습니다.")

#3 function 
def pick_numbers(seq):
    numbers = []
    for i in seq:
        if type (i) == int or type (i) ==float:
            numbers.append(i)
    return sum(numbers)
               
