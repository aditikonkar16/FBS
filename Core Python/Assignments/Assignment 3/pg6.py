#Write a program to calculate profit or loss.
CP=int(input('enter cost price:'))
SP=int(input('enter selling price:'))
if(SP>CP):
    print('Profit:',SP-CP)
elif(CP>SP):
    print('Loss:',CP-SP)
else:
    print('No profit, no loss')