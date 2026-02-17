import pandas as pd

df = pd.read_csv("raw_data.csv")
print(df)
df2 = df.copy()

# new_col_order = [col for col in df2.columns if col != "id"] + ["id"]

# print(new_col_order)

# df2 = df2[new_col_order]
# print(df2)

# df2 = df2[["name", "age", "country", "gender", "income", "id"]]
# print(df2)