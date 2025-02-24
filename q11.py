# Check if two lists have at least one common member
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

if any(item in list1 for item in list2):
    print("The lists have at least one common member.")
else:
    print("The lists have no common members.")
