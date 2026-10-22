P = float(input('enter the principal:'))
T = float(input('enter the time in years:'))
R = float(input('enter the rate of interest:'))

CI = P * (1 + R/100)**T-P
print(f'Compound Interest is {CI}')