# Total Marks and Percentage

s1 = int(input("Enter marks of Subject 1: "))
s2 = int(input("Enter marks of Subject 2: "))
s3 = int(input("Enter marks of Subject 3: "))
s4 = int(input("Enter marks of Subject 4: "))
s5 = int(input("Enter marks of Subject 5: "))

total_marks = s1 + s2 + s3 + s4 + s5
print("Total Marks =", total_marks)

percentage = (total_marks / 500) * 100
print("Percentage =", percentage)

average = total_marks / 5
print("Average=",average)