# format specifiers = {value : find format a value based on whar flags are inserted}

price1 = 3.14159
price2 = -987.65
price3 = 12.34

# print(f"Price 1 is {price1 : .2f}") decimal point precion upto two points
# print(f"Price 1 is {price2 : 10}")  Adds 10 spaces before the pronted value
# print(f"Price 1 is {price3 : 010}") Adds zeroes before values
# print(f"Price 1 is {price3 : <10}") Numbers will be left justified
# print(f"Price 1 is {price3 : >10}") Right justified
# print(f"Price 1 is {price3 : ^10}") Center aligned
# print(f"Price 1 is {price3 : +}")   Adds + sign before number and negative -
# print(f"Price 1 is {price3 : ,}")   Adds comma at Thousand place