
# Calculate Area of a Rectangle
length = float(input("Enter length in cm: "))
width  = float(input("Enter width in cm: "))

if length <= 0 or width <= 0:
 print("Invalid input!")
else:
    area = length * width
    print("Area = %.2f cm²" % area)
