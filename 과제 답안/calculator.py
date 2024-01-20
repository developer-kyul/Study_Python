def calculator(operator, integer1, integer2):

     if operator == 'add':
         return integer1 + integer2
     elif operator == 'sub':
         return integer1 - integer2
     elif operator == 'mul':
         return integer1 * integer2
     elif operator == 'div':
         return integer1 / integer2
     else:
         print(operator + ' is not supported.')