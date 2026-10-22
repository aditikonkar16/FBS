#Sum of all odd numbers between 1 to n
def oddnum(n):
    total = 0
    for i in range (1,n+1,2):
        total+=i
        return total
n = int(input("Enter value of n: "))
result = oddnum(n)
print("Sum of odd numbers from 1 to", n, "=", result)
    