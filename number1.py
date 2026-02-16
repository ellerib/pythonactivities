# Number 1
def process():
	collection = []

	while True:
		fruits = input("Enter fruits (type stop to stop inputting): ")

		if fruits.lower() != "stop":
			collection.append(fruits)
			print(collection)
			continue
		else:
			break
	return collection

#Output
print("Fruits that are in the lists")
collection = process()
print(collection)
