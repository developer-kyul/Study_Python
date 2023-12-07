# initial review
review = ("8 - 케빈 코스트너 최고의 영화.\n"
         "원주민인 인디언의 아픔을 제대로 짚어보기 시작한 영화사적 의미도 상당하다.\n"
         "아직 백인의 시선을 완전히 거둘수 없던 점이 안타깝지만,\n"
         "나에겐 3시간의 상영시간이 전혀 길게 느껴지지 않을 명작이다.")

# remove rating
review = review.lstrip('0123456789')

# remove punctuation(.,-)
review = review.replace('.', '')
review = review.replace(',', '')
review = review.replace('-', '')

# remove stop words('영화', '점이', '나에겐')
review = review.replace('영화', '')
review = review.replace('점이', '')
review = review.replace('나에겐', '')

# split to word list
review = review.split()

# concatenate to CSV format
review = ','.join(review)

# print result
print(review)
