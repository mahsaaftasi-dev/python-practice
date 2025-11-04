import pandas as pd 
users = pd.DataFrame({
    "UserID": [1, 2, 3],
    "Name": ["Mahsa", "Ali", "Sara"]
})

orders = pd.DataFrame({
    "OrderID": [101, 102, 103],
    "UserID": [1, 1, 2],
    "Amount": [200, 150, 300]
})

merged = pd.merge(users, orders, on="UserID", how="inner")
print(merged)