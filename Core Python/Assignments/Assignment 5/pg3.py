#Accept no. of passengers from user and per ticket cost. Then accept age of each
#passenger and then calculate total amount to ticket to travel for all of them based on
#following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

n = int(input("Enter number of passengers: "))
ticket= float(input("Enter per ticket cost: "))
total = 0
for i in range(n):
    age = int(input("Enter age of passenger {}: ".format(i+1)))
    if age < 12:
        cost = ticket * 0.7
    elif age > 59:
        cost = ticket * 0.5
    else:
        cost = ticket
    total += cost
print("Total amount to be paid:", total)