#Input 5 subject marks from user and display grade(eg.First class,Second class ..)
Sub1=int(input('enter marks of subject 1:'))
Sub2=int(input('enter marks of subject 2:'))   
Sub3=int(input('enter marks of subject 3:'))
Sub4=int(input('enter marks of subject 4:'))
Sub5=int(input('enter marks of subject 5:'))
Total=Sub1+Sub2+Sub3+Sub4+Sub5
if Total>=400:
    print('First class') 
elif Total>=300:
    print('Second class')
else:
    print('Third class')            
                
