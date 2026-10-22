#Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

a1=int(input('enter age of person 1:'))
a2=int(input('enter age of person 2:'))
a3=int(input('enter age of person 3:'))
a4=int(input('enter age of person 4:'))
a5=int(input('enter age of person 5:'))
t1=int(input('enter ticket amount of person 1:'))
t2=int(input('enter ticket amount of person 2:'))   
t3=int(input('enter ticket amount of person 3:'))
t4=int(input('enter ticket amount of person 4:'))
t5=int(input('enter ticket amount of person 5:'))
if(a1<12):
    t1=t1-(t1*30/100)
elif(a1>59):
    t1=t1-(t1*50/100)
if(a2<12):
    t2=t2-(t2*30/100)
elif(a2>59):
    t2=t2-(t2*50/100)
if(a3<12):
    t3=t3-(t3*30/100)
elif(a3>59):
    t3=t3-(t3*50/100)
if(a4<12):
    t4=t4-(t4*30/100)
elif(a4>59):
    t4=t4-(t4*50/100)
if(a5<12):
    t5=t5-(t5*30/100)
elif(a5>59):
    t5=t5-(t5*50/100)
total=t1+t2+t3+t4+t5
print('Total amount to be paid:',total)




