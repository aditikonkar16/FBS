#Write a program to calculate area of circle
def areaofcircle(radius):
    return 3.14 * radius * radius
r = float(input("Enter radius: "))
area = areaofcircle(r)
print("Area of circle =", area)