Q1 = 7760, 6290, 450
Q2 = 8920, 7800, 500
Q3 = 8145, 7600, 485
Q4 = 7105, 5920, 450

values = list(zip(Q1, Q2, Q3, Q4))
keys = ['매출액', '매출원가', '판매관리비']
result = dict(zip(keys, values))
print(result)

t1 = (
    result['매출액'][0] - result['매출원가'][0],
    result['매출액'][1] - result['매출원가'][1],
    result['매출액'][2] - result['매출원가'][2],
    result['매출액'][3] - result['매출원가'][3]
    )

t2 = (
    t1[0] - result['판매관리비'][0],
    t1[1] - result['판매관리비'][1],
    t1[2] - result['판매관리비'][2],
    t1[3] - result['판매관리비'][3]
    )

result['매출총이익'] = t1
result['영업이익'] = t2

print(result)
    

