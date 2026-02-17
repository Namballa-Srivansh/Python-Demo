import pandas as pd 

df1 = pd.DataFrame({
    "id": [1,2,3],
    "name": ["Alice", "Bob", "Charlie"]
})

df2 = pd.DataFrame({
    "id": [4,5,6],
    "name": ["Diana", "Eve", "Frank"]
})

# print(df1)
# print(df2)

# df_concat = pd.concat([df1, df2]) # Row wise concatenation on top of each other
df_concat = pd.concat([df1, df2], ignore_index=True)
print(df_concat)

df_concat_col = pd.concat([df1, df2], axis=1) # Column wise concatenation next to each other
print(df_concat_col)
