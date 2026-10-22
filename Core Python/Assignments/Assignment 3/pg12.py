#Write a program to check if given 3 digit number is a palindrome or not.
n=int(input('Enter a 3 digit number:'))
if n<100 or n>999:
    print('Please enter a valid 3 digit number')
else:
    rev=0
    temp=n
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp//=10
    if n==rev:
        print(n,'is a palindrome number')
    else:
        print(n,'is not a palindrome number')