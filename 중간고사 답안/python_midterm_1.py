a = '8 - 케빈 코스트너 최고의 영화. 원주민인 인디언의 아픔을 제대로 짚어보기 시작한 영화사적 의미도 상당하다. 아직 백인의 시선을 완전히 거둘수 없던 점이 안타깝지만, 나에겐 3시간의 상영시간이 전혀 길게 느껴지지 않을 명작이다.'
#strip 문자열에서 평점 제거
a.lstrip('8 - ')

#replace를 사용해서 특수기호 제거
a.replace(',','')
a.replace('.','')
a.replace('-','')

#split를 이용하여 공백문자 기준으로 변경
a.split()

#join를 이용하여 문자열로 결합하여 출력
','.join(a)

print(a)

