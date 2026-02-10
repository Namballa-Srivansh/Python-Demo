unit = input("Is the Temperature is in Fahrenheit or Celsius (F/C) : ")
temp = float(input("Enter the Temperature : "))

if unit == 'C':
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is : {temp}deg F")
    
elif unit == 'F':
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}deg C")
    
else:
    print(f"{unit} is an invalid unit of measurement")