# PART 1
import pandas as pd

df = pd.read_csv("sales.csv")

print(df)

recordcount = len(df)
print(f"Total number of records: ", {recordcount})

summary = df.describe()
print(summary)

# PART 2
regiontotal = df.groupby("Region")["Sales"].sum()
print("Region total")
print(regiontotal)

producttotal = df.groupby("Product")["Sales"].sum()
topproduct = producttotal.max() 
topsales = producttotal.idxmax()

print(f"Top selling product: ")
print(topproduct)
print("Total sales")
print(topsales)

fill_region = df







