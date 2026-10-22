import math
a = float(input('enter value of a :'))
b = float(input('enter value of b :'))
c = float(input('enter value of c :'))

D = b**2 - 4*a*c

if D>0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print(f'The roots are real and different: {root1} and {root2}')
    
elif D == 0:
    root1 = root2 = -b / (2*a)
    print(f'Both roots are same: {root1}')
    
else:
    print('The roots are imaginary')
    
