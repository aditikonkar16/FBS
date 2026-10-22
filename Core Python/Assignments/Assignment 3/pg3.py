#Write a program to input angles of a triangle and check whether triangle is valid or not.
A1=int(input('enter angle 1:'))
A2=int(input('enter angle 2:'))
A3=int(input('enter angle 3:'))
if(A1+A2+A3==180):
    print('The triangle is valid')
else:
    print('The triangle is not valid')