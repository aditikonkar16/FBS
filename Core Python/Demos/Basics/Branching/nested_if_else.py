gender=input('enter gender(M/F):')
age = int(input('enter age:'))

if(gender == 'M'):
    if(age>=21):
        print('boy is eligible for marriage:')
    else:
        print('Pehle kama lo')
else:
    
        if(age>=18):
            print('Girl is eligible for marriage:')
        else:
            print('Pehle padhai kar lo')
            