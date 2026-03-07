import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

region_sales = df.groupby("Region")["Sales"].sum()
print(region_sales)

region_sales.plot(kind="bar")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.title("Total Sales per Region")
plt.show()