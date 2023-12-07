Q1 = (7760, 6290, 450)
Q2 = (8920, 7800, 500)
Q3 = (8145, 7600, 485)
Q4 = (7105, 5920, 450)


result = {'Revenue': (Q1[0], Q2[0], Q3[0], Q4[0]),
        'COGS': (Q1[1], Q2[1], Q3[1], Q4[1]),
        'Operating Expenses': (Q1[2], Q2[2], Q3[2], Q4[2])}

print(result)


QGP = (result['Revenue'][0] - result['COGS'][0],
       result['Revenue'][1] - result['COGS'][1],
       result['Revenue'][2] - result['COGS'][2],
       result['Revenue'][3] - result['COGS'][3])

result['Gross profit'] = QGP

QOP = (result['Gross profit'][0] - result['Operating Expenses'][0],
       result['Gross profit'][1] - result['Operating Expenses'][1],
       result['Gross profit'][2] - result['Operating Expenses'][2],
       result['Gross profit'][3] - result['Operating Expenses'][3],)

result['Operating profit'] = QOP

print(result)
