import pandas as pd

df = pd.read_csv("raw_data.csv")
# print(df)

# print(df.isnull())
#     OR      
# print(df.isna())

# print(df.isnull().sum()) # to count the number of null values in each column

# print(df.dropna()) # to drop the rows with null values

# print(df.dropna(axis=1)) # to drop the columns with null values

# print(df.fillna(0)) # to fill the null values with 0
# print(df.fillna(100)) # to fill the null values with 100

# age_mean = df["age"].mean()
# print(df["age"].fillna(age_mean)) # to fill the null values with the mean of the column

# cleaned_data = df.copy()
# age_mean = cleaned_data["age"].mean()
# cleaned_data["age"] = cleaned_data["age"].fillna(age_mean)
# print(cleaned_data) 

# print(df.ffill()) # forward fill

# print(df.bfill()) # backward fill


# --------------------------Duplicates-------------------------

# print(df.duplicated()) # to check for duplicate values
# print(df[["country", "gender"]].duplicated()) # to check for duplicate values in a specific column
# df2 = df.copy()
# print(df.drop_duplicates(i)) # to drop the duplicate values
 
#  --------------------------------DATA TYPES-------------------------

# print(df.dtypes)
# df2 = df.copy()
# df2 = df2.fillna(0)
# df2 = df2["age"].astype("int64")
# print(df2.dtypes)
# print(df2)
