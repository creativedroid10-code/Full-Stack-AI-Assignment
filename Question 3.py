# Question 3: Calculate Compound Interest
Principal = float(input("Enter principal amount: "))
Rate = float(input("Enter rate of interest: "))
Time  = float(input("Enter time in years: "))
CI = Principal * (1 + Rate/100) ** Time - Principal
print("Compound Interest is:", CI)