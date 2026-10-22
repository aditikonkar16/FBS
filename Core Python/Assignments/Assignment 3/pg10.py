#Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)
age=int(input('enter age:'))
gender=input('enter gender:')
if(gender=='male'):
    if(age>=21):
        print('Eligible to marry')
    else:
        print('Not eligible to marry')
else:
    if(age>=18):
        print('Eligible to marry')
    else:
        print('Not eligible to marry')