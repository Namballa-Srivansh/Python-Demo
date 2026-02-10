# Python writing files (.txt, .json, .csv)

import json
import csv

# employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

txt_data = "I like pizza!"
file_path = ""

# with open(file_path, "w") as file:
#     file.write(txt_data)
#     print(f"txt file '{file_path}' was created")

# with open(file_path, "a") as file:
#     file.write('\n' + txt_data)
#     print(f"txt file '{file_path}' was created")

# with open(file_path, "w") as file:
#     for employee in employees:
#         file.write(employee + "\n")
#     print(f"txt file '{file_path}' was created")

# +++++++++++++ Json +++++++++++++++++++++++++++++

# employee = {
#     "name" : "Spongebob",
#     "age" : 30,
#     "job" : "cook"
# }

# try:
#     with open(file_path, "w") as file:
#         json.dump(employee, file, indent = 4)
#         print(f"json file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists")

# --------------------- Csv ---------------------------------

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")