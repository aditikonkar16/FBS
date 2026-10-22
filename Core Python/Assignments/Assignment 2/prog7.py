num = int(input('enter the number:'))
hunderds = num //100
tens = (num // 10) % 10
units = num % 10

sum = hunderds + tens + units
print('sum of three digit no:',sum)