import pandas as pd 
data = pd.DataFrame({
    "Name": ["Mahsa", "Ali", None, "Sara"],
    "Age": [35, None, 29, 40],
    "City": ["Tehran", "Shiraz", "Tehran", None]
})
#fill missing value
data["Age"].fillna(data["Age"].mean(),inplace=True)

#fill missing dity
data["City"].fillna("unkown",inplace=True)

#rename the column
data.rename(columns={"Name" : "Fullname"},inplace=True)


print (data)
