# NUMBER 2
def power_of(sets):     
   new_sets = set()

   if sets is None:
       print("Set is empty")
   else:
       for x in sets:
           result = x ** 2
           new_sets.add(result)
   return new_sets

print("Before sets are powered of 2: ")
sets = {1, 2, 3, 4, 5}
print(sets)

print("After sets are powered of 2: ")
new_sets = power_of(sets)
print(new_sets)
