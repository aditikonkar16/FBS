#Write a program to check if entered number is a palindrome or not.
def is_palindrome(n):
    return n == n[::-1]
num = input("Enter a number:")
if is_palindrome(num):
    print("Palindrome number")
else:
    print("Not a palindrome number")