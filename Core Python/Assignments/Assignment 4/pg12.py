#Write a program to check if given number is Armstrong number or not.(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +4*4*4*4)
n=int(input("Enter a number: "))
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if sum==n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")
        