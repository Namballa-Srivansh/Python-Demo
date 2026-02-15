import json

# --------------------DEALING WITH JSON STRINGS OR PYTHON OBJECTS----------------------------------------------------

# json_str ='{"name": "Srivansh","isStudent": true}'

# py_obj = json.loads(json_str) # converts json string to python object

# py_obj = {
#     "name": "Srivansh",
#     "isStudent": True
# }

# json_str = json.dumps(py_obj) #coverts python object to json string

# print(json_str)
# print(type(json_str))

# -----------------------DEALING WITH FILES-----------------------------------------------------------------

d = {
    "name": "Srivansh",
    "isStudent": True,
    "scores": [10, 20, 30]
}

with open("data.json", "w") as f :
    json.dump(d, f, indent=4) # converts python object to json string and writes it to a file

with open("data.json", "r") as f :
    py_obj = json.load(f) # converts json string to python object
    print(py_obj)