#WAP to print all numbers in a range divisible by a given number.
n=int(input("Enter the value of n: "))
divisor=int(input("Enter the divisor: "))   
for i in range(1,n+1):
    if(i % divisor == 0):
        print(i)
        