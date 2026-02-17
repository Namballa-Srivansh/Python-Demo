import pandas as pd

df = pd.read_csv("raw_data.csv")

# print(df.groupby("country")["income"].mean())
# print(df.groupby("country")["income"].max())
# print(df.groupby("country")["income"].min())

# print(df.groupby("gender")["income"].mean())
# print(df.groupby("gender")["income"].max())
# print(df.groupby("gender")["income"].min())

# print(df.groupby("country")["income"].agg(["mean", "min", "max"]))
# -------------------OR------------------------------------
# print(df.groupby("country")["income"].aggregate(["mean", "min", "max"]))

# print(df.groupby("country")["income"].aggregate(avg_salary = "mean", min_salary = "min", max_salary = "max"))

# print(df.groupby("country").agg({
#     "income": ["mean", "min", "max"],
#     "age": ["mean", "min", "max"]
# }))