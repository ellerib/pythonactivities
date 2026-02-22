
# TUPLE CANT CHANGE
person = ("anne", "jake", "kate", "cath")
change = list(person)
change[2] = "jekel"
person = tuple(change)
print(person)

change1 = list(person)
change1.append("jubs")
person = tuple(change1)

print(person)

print("\n")
print("\n")

# JOINING TWO LISTS
things = ["pen", "pencil ", "notebook", "eraser"]
gadgets = ["laptop", "cellphone", "monitor"]

for x in things:
    gadgets.append(x)
print(gadgets)

combined_lists = things + gadgets
print(combined_lists)

print("\n")

# ADD A VALUE
things.append("mouse")
print(things)

# APPEND VALUE AT SPECIFIC
things.insert(5,"envelope")
print(things)

gadgets[3] = "tablet"
print(gadgets)

# REMOVE LISTS
gadgets.remove("laptop")
print(gadgets)
gadgets.pop()
print(gadgets)

# DELETE ALL ITEMS ON LISTS
gadgets.clear()
print(gadgets)

# LOOP TROUGH LISTS
for x in things:
    print(things)

"""
#CHNAGE A VALUE AT SPECIFIC
things[3] = "ruler"
print(things)
"""


