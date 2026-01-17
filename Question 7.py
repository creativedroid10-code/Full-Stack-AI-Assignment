# Distribute Items Equally

candies = int(input("Enter number of candies: "))
students = int(input("Enter number of students: "))

equal = candies // students
candies_left = candies % students

print("Each student gets:", equal, "candies")
print("Candies left:",candies_left)