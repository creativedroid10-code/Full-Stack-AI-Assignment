# Converts a temperature from Celsius to Fahrenheit
celsius = float(input("Enter temperature in °C: "))
if celsius < -273.15:
    print("Error")
else:
    fahrenheit = (celsius * 9/5) + 32
    print("%s °C = %.2f °F" % (celsius, fahrenheit))
