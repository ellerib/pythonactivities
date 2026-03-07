import pandas as pd

# PART 1
df = pd.read_csv("students.csv")
df.head(5)

print(df)
print("\n")

# DATA SHAPE
print("Data shape")
print(df.shape)
print("\n")

#DATA TYPES
print("Data types")
print(df.dtypes)

# SUMMARY STATISTIC

summarydataset = df.describe()
print("Summary statistic")
print(summarydataset)

# PART 2

df["Average"] = (df["Midterm"] + df["Final"]) / 2
print(df)

print("\n")

countaverage = df[df["Average"]>=85]
countattendance = df[df["Attendance"]<90]

print("Total average")
print(countaverage)
print("\n")

print("Total attendance")
print(countattendance)
print("\n")

# PART 3
sort_average = df.sort_values("Average", ascending=False)
print("Average sort(highest to lowest)")
print(sort_average)
print("\n")

groupcourse = df.groupby("Course")["Average"].mean()

print("Group courses: ",groupcourse)


