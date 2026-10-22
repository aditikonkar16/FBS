#Sum of all prime numbers between 1 to n
def prime(n):
    total = 0
    for i in range(2, n + 1):
        if prime(i):
            total += i
    return total
n = int(input("Enter value of n: "))
result = prime(n)
print("Sum of prime numbers from 1 to", n, "=", result)