#WAP to print Armstrong number within a given range
a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))
for n in range(a, b + 1):
    s = 0
    temp = n
    while temp > 0:
        r = temp % 10
        s = s + r ** 3
        temp = temp // 10
        if s == n:
            print(n)