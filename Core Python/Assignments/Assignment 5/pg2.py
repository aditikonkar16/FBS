#Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. Display all percentage and 
# average percentage of students.
n = int (input("enter no. of students: "))
total = 0
for i in range(n):
    sum = 0
for j in range(5):
        marks = int(input("Enter marks of subject {} for student {}: ".format(j+1, i+1)))
        sum += marks
percentage = sum / 500 
print("Percentage =", percentage * 100)
total += percentage
print("Average percentage of students =", (total / n) * 100)

                                                     