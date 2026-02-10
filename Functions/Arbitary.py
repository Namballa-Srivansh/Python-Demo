# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#             * unpacking operator
#            1.positional 2.default 3.keyword 4. ARBITRARY

# def add(*args):
#     total = 0;
#     for arg in args:
#         total += arg
#     return total

# print(add(1, 2, 3, 4))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")


# display_name("Spongebob","Harold", "Squarepants", "III")

# ---------------------------------------------------------------------------------------------------

# def print_address(**kwargs):
#     # for value in kwargs.values():
#     #     print(value)
    
#     # for key in kwargs.keys():
#     #     print(key)
    
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")

# print_address(street = "123 Fake St.",
#               apt = "100",
#               city = "Fake City",
#               state = "HI",
#               zip = "13579")



# ------------------------------------------------------------------------------------------------------

# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()
    
#     print(f"{kwargs.get('street')}")
#     print(f"{kwargs.get('apt')} {kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

# shipping_label("Dr.", "Spongebob", "Harold", "Squarepants", "III",
#                street = "123 Fake St.",
#                apt = "100",
#                city = "Detroit",
#                state = "HI",
#                zip = "13579")