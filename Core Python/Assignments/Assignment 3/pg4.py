#Write a program to input all sides of a triangle and check whether triangle is valid or not.
a=int(input('enter side 1:'))
b=int(input('enter side 2:'))
c=int(input('enter side 3:'))
if(a+b>c and b+c>a and c+a>b):
    print('The triangle is valid')
else:
    print('The triangle is not valid')