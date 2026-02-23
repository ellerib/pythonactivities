import numpy as np

# ONE DIMENSIONAL ARRAY
onearr = np.array([1,2,3,5])

# TWO DIMENSION ARRAY
twodarr = np.array([
    [5,3,6, 8,9], 
    [8,2,1, 6,3], 
    [7,5,4, 3,6]
])

# 3-D ARRAY
threearry = np.array([
    [
        [5,8,3],
        [4,9,3]
    ],
    [
        [7,3,6],
        [5,7,2]
    ] 
])

# INDEXING = ROW THEN COLUMN, 2-D
retrieve = twodarr[1,0]
print(retrieve)

# SLICING AN ARRAY 2-D, FIRST FIND ROW THEN COLUMN AND ROW
slicing = twodarr[2, 1:2]
print(f"Slicing-2darray: {slicing}")

# OUTPUT
print(onearr)
print("\n")
print(twodarr)
print("\n")
print(threearry)


# NUMBER OF DIMENSIONS
print(onearr.ndim)
print(twodarr.ndim)
print(threearry.ndim)   

grades = np.array([85,90,78,92,88])

sumgrade = np.sum(grades)
average = np.average(grades)
highest = np.max(grades)
lowest = np.min(grades)
standard_dv = np.std(grades)

print(f"sum: {sumgrade}")
print(f"grades: {grades}")
print(f"average: {average}")
print(f"highest: {highest}")
print(f"lowest: {lowest}")
print(f"standard deviation: {standard_dv}")
