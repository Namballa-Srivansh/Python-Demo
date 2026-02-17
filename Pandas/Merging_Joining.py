import pandas as pd 

df_customers = pd.DataFrame({
    "customer_id": [1,2,3,4],
    "name": ["Alice", "Bob", "Charlie", "Diana"]
})

df_orders = pd.DataFrame({
    "order_id": [101,102,103,104],
    "customer_id": [2,1,4,5],
    "amount": [100,200,300,400]
})

# print(df_customers)
# print(df_orders)

# df_merged = pd.merge(df_customers, df_orders, on="customer_id") # Inner join
# df_merged = pd.merge(df_customers, df_orders, on="customer_id", how="left") # Left join
# df_merged = pd.merge(df_customers, df_orders, on="customer_id", how="right") # Right join
df_merged = pd.merge(df_customers, df_orders, on="customer_id", how="outer") # Outer join

print(df_merged)
