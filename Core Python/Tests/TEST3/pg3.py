n = int(input("Number of employees: "))
all_total = 0

for i in range(n):
    basic = float(input("Enter basic salary: "))

    if basic < 20000:
        salary = basic + basic * 0.10 + basic * 0.12 + basic * 0.15
    else:
        salary = basic + basic * 0.15 + basic * 0.18 + basic * 0.20

    print("Employee", i + 1, "total salary:", salary)
    all_total += salary

print("Total salary of all employees:", all_total)