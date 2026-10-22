#Write a program to prompt user to enter userid and password. If Id andpassword is incorrect give him chance to re-enter the credentials. Let him try 3times. After that program to terminate.
userid = "admin"
password = "admin123"
for i in range(3):
    uid=input("Enter user id: ")
    pwd=input("Enter password: ")
    if uid==userid and pwd==password:
        print("Login successful")
        break
    else:
        print("Invalid credentials. Please try again.")
else:
    print("You have exceeded the maximum number of attempts. Program terminated.")
    