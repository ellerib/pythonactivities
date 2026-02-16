import numpy as np
from numpy import random

x = random.randint(100, size=(10))

print("Array: ", x)

mean = np.mean(x)
max = np.max(x)
min = np.min(x)
st_deviation = np.std(x)

print(f"Mean: {mean}")
print(f"Max: {max}")
print(f"Min: {min}")
print(f"Standard deviation: {st_deviation}")