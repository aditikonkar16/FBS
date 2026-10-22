D = int(input('enter the total days == '))
years = D // 365
remaining_days = D % 365
weeks = remaining_days // 7
days = remaining_days % 7
print (f'{years} Years, {weeks} Weeks, and {days} Days')