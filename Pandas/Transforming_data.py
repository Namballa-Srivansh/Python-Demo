import pandas as pd

df = pd.read_csv("raw_data.csv")
# print(df)

df["tax"] = df["income"].apply(lambda x : "20%" if x > 50000 else "10%")
# print(df)

gender_map = {"Male" : "M", "Female" : "F", "Unknown" : "U"}
df["gender"] = df["gender"].map(gender_map)
# print(df) 

df = df.assign(new_income = df["income"] * 1.1)
# print(df)

df = df.replace({"country" : {"USA" : "US"}})
# print(df)

df2 = df.copy()

df2.columns = ["Id", "Name", "Age", "Country", "Gender", "Income", "Tax", "New Income"]
# print(df2)

df2.rename(columns={"Income" : "Salary"}, inplace=True)
# print(df2)

df2.rename(index={1: "First"}, inplace=True)
# print(df2)

df2.sort_values("Salary", inplace=True)
df2 = df2.fillna(50)
sorted_df = df2.sort_values(["Salary", "Age"])
# print(sorted_df)

sorted_df = sorted_df.sort_index(key=lambda x: x.astype(str))
# print(sorted_df)

sorted_df.reset_index(drop=True, inplace=True)
# print(sorted_df)

sorted_df["Ranking"] = sorted_df["Salary"].rank()
# print(sorted_df)

sorted_df = sorted_df[["Id", "Name", "Age", "Country", "Gender", "Salary", "New Income", "Ranking", "Tax"]]
# print(sorted_df)
 