import numpy as np

grade = np.random.randint(60, 101, size=50)
print("Grades: ", grade)

gradeaverage = np.mean(grade)
pass_count = np.sum(grade>=75)
fail_count = np.sum(grade<=75)
highest = np.max(grade)
lowest = np.min(grade)

print(f"Average grade: {gradeaverage:.2f}")
print(f"Number of passing grades: {pass_count}")
print(f"Number of failing grades: {fail_count}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")

