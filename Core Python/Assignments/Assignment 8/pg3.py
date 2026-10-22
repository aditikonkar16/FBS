#Write a program to find sum of following series using functions :
#a. 1+ 2 + 3 + 4+..... + n
def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
n = int(input("Enter value of n: "))
print("a. Sum of 1 + 2 + ... + n =", sum_natural(n))
#b.
def sumfact(n):
    total = 0
    for i in range(1, n + 1):
        total += sumfact(i)
    return total
n = int(input("Enter value of n: "))
print("b. Sum of 1! + 2! + ... + n! =", sumfact(n))


#c.
def sum_power(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total
n = int(input("Enter value of n: "))
print("c. Sum of 1^1 + 2^2 + ... + n^n =", sum_power(n))


