import numpy as np

array1 = np.array([[5, 12, 7], [9, 3, 15], [2, 18, 6]])
array2 = np.array([[4, 10, 8], [7, 6, 2], [11, 1, 9]])

print("Array1:\n", array1)
print("Array2:\n", array2)

# CALCULATIONS
arraysum = array1 + array2
elem_multi = array1 * array2
matrix_multi = np.dot(array1, array2)

print(f"Sum of array1 and array2:\n{arraysum}")
print(f"Element-wise multiplication of array1 and array2:\n{elem_multi}")
print(f"Matrix multiplication of array1 and array2:\n{matrix_multi}")
