import pandas as pd

# Load CSV file (you can download a sample from kaggle or make your own)
data = pd.DataFrame({
    "Region": ["East", "West", "North", "South", "East", "West"],
    "Sales": [200, 150, 300, 250, 180, 210],
    "Rep": ["Ali", "Sara", "Reza", "Mahsa", "Nilo", "Omid"]
})

# Basic exploration
print("Head:")
print(data.head(), "\n")

print("Info:")
print(data.info(), "\n")

print("Statistics:")
print(data.describe(), "\n")