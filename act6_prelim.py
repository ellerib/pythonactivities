import pandas as pd

df = pd.read_csv("messydata.csv")

print(df)

# Detect missing values
detection = df.isnull().sum()
print(detection)

# Fill missing age with mean
agemean = df["Age"].mean()
fill_age = df["Age"] = df["Age"].fillna(agemean)
print(df)
error_check1 = df.isnull().sum()
print("Errors: ", error_check1)

salarymedian = df["Salary"].median()
fill_salary = df["Salary"] = df["Salary"].fillna(salarymedian)
print(df)
error_check2 = df.isnull().sum()
print("Errors: ", error_check2)


df["Department"] = df["Department"].str.upper()
print(df)

df = df.drop_duplicates()
print(df)

# EXPORTING TO CSV
df.to_csv("cleaned_data.csv", index=False)
