import pandas as pd

df = pd.read_csv("globalAirQuality.csv")
# print(df.head())
# print(df.tail())
# print(df.describe())

# -------------------------------Selecting data------------------------

# print(df[["country","city","aqi"]]) # Selecting multiple columns
# print(df.loc[0]) # Selecting a row by label
# print(df.loc[0:5]) # Selecting multiple rows by label
# print(df.iloc[0]) # Selecting a row by index
# print(df.iloc[0:5]) # Selecting multiple rows by index

# -------------------------Selecting a specific value i.e row and column---------------------------

# print(df.loc[0, "aqi"])
# print(df.loc[0:2,["city", "aqi"]])

# print(df.iloc[0:3, 2]) iloc works with numeric data we cannot provide column like city instead use index of the column

# print(df.iloc[0:3, 1:5])

# -------------------------------TO ACCESS SCALAR VALUE OR INDIVIDUAL CELL-----------------------------

# print(df.at[0, "city"])
# print(df.iat[0, 2])

# cities = df["city"] Not a copy but view(original)
# cities = df["city"].copy() # copy
# cities[0] = "Mumbai"
# print(df["city"])
# print(cities)

# ------------------------------------FILTERING-----------------------------------------    

# print(df)
# print(df[df["aqi"] > 100])
# print(df[(df["aqi"] > 100) & (df["temperature"] > 30)])
# aqi_data = df[(df["aqi"] > 100) & (df["temperature"] > 30)][["city", "aqi"]]
# print(aqi_data.iloc[0])
# print(aqi_data.loc[0]) gives error cause labe 0 is not present in filtered data
# print(aqi_data.loc[6])

# ------------------------------------FILTERING WITH QUERY-----------------------------------------    

# OUERY returns copy

# print(df.query("aqi > 100 and temperature > 30") [["city", "aqi"]])
# aqi_val = 100
# print(df.query("aqi > @aqi_val and temperature > 30") [["city", "aqi"]])