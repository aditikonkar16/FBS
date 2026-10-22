n = int(input("Enter n: "))

factorial = 1
total = 0.0

for i in range(1, n + 1):
    factorial *= i
    total += i / factorial

print("Sum =", total)