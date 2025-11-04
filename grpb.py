import pandas as pd

data = pd.DataFrame({
    "Name": ["Mahsa", "Ali", "Sara", "Omid", "Reza", "Lina"],
    "Gender": ["F", "M", "F", "M", "M", "F"],
    "Steps": [10000, 8500, 12000, 7000, 11000, 9500],
    "Calories": [300, 250, 350, 200, 320, 280]
})
grouped = data.groupby("Gender")[["Steps","Calories"]].mean()
print(grouped)