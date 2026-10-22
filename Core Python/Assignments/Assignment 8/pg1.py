# Write a program to calculate area of rectangle.

def calculate_area(length, width):
    return length * width
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area = calculate_area(length, width)
print("Area of rectangle =", area)
    
