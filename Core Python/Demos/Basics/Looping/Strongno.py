num=145
temp = num
sum=0
while(num > 0):
    d = num % 10
    num = num //10
    #print(d)
    fact = 1
    for i in range(1,d+1):
        fact *= i
    #print(fact)
    sum+=fact
if(sum == temp):
    print(f" is a strong number")
else:
    print(f" is not a strong number")