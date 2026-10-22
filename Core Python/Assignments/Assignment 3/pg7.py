#Write a program to check if user has entered correct userid and password.
userid=input('enter userid:')
password=input('enter password:')
if(userid=='admin' and password=='admin123'):
    print('Login successful')
else:
    print('Login failed')
    
    