#Salary Calculator

basic_salary = int(input("Enter Basic Salary: "))

house_rent_allowance = (basic_salary * 20) / 100
dearness_allowance = (basic_salary * 15) / 100

total_salary = basic_salary + house_rent_allowance + dearness_allowance
print("Total Salary =",total_salary)