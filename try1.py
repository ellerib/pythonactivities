import pandas as pd
df = pd.read_csv("age_debt1.csv")

print(df)

print(df.isnull().sum())
avg_age = df["age"].mean()
avg_debt = df["debt"].mean()
print("Average Age:", avg_age)
print("Average Debt:", avg_debt)

df["age"] = df["age"].fillna(avg_age)
df["debt"] = df["debt"].fillna(avg_debt)
print(df.isnull().sum())


