import numpy as np

sales = np.random.randint(1000, 4001, size=(5, 4))

totalperproduct = np.sum(sales, axis=1)
totalperquarter = np.sum(sales, axis=0)
bestproduct = np.argmax(totalperproduct)
bestquarter = np.argmax(totalperquarter)

print("Sales Data:\n", sales)
# Total sales
print("\nTotal sales per product:", totalperproduct)
print("\nTotal sales per quarter:", totalperquarter)

# Best product
print(f"Best product: Product #{bestproduct + 1}")

# Best quarter
print(f"Best quarter: Quarter #{bestquarter + 1}")
