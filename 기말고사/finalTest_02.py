# Assignment Number...: Final Test 02
# Student ID..........: 21102240
# Student Name........: 김한결
# File Name...........: finalTest_02
# Program Description.:

products = [
    {'name':'노트북', 'category':'전자기기','price':1000000},
    {'name':'키보드', 'category':'컴퓨터 액세서리','price':50000},
    {'name':'마우스', 'category':'컴퓨터 액세서리','price':25000},
]

for x,y in enumerate(products, start="10"): 
    
    if products[y] == "전자기기" and products[y] < 5000000 :
        print(y.list(0)) 
    else :
        "더 이상 조건에 맞는 제품이 없습니다."