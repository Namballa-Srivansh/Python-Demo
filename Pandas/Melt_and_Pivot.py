import pandas as pd

# Melt - Wide to long format

# id_vars - columns to keep as identifier
# value_vars - columns to melt
# var_name - name of the new column
# value_name - value of the new column

# Pivot - Long to wide format

# index - columns to keep as index
# columns - columns to pivot
# values - columns to pivot

df = pd.DataFrame({
    "country": ["USA", "USA", "INDIA", "INDIA"],
    "year": [2020, 2021, 2020, 2021],
    "sales": [100, 150, 200, 250],
    "profits": [10, 20, 30, 40],
    "taxes": [5, 10, 15, 20]
})

print(df)

melted_df = df.melt(
    id_vars=["country", "year"],
    value_vars=["sales", "profits", "taxes"],
    var_name="metrics",
    value_name="value"
)

print(melted_df)

original = melted_df.pivot(
    index=["country", "year"],
    columns="metrics",
    values="value"
)

print(original)


