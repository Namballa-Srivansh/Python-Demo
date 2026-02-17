import pandas as pd

df = pd.read_csv("raw_data.csv")

df2 = df.copy()
df2.drop_duplicates(inplace=True)
df2 = df2.fillna(0)

df2 = df2.sort_values("income")
df2 = df2.reset_index(drop=True)

df2.to_csv("cleaned_data.csv")
print("Data cleaned and saved to cleaned_data.csv") 