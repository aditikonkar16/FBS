#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
a=int(input('enter side a:'))
b=int(input('enter side b:'))
c=int(input('enter side c:'))
if(a==b and b==c):
    print('The triangle is equilateral')
elif(a==b or b==c or c==a):
    print('The triangle is isosceles')
else:
    print('The triangle is scalene')