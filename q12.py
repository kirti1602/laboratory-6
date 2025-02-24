# Remove the 0th, 4th, and 5th elements from a list
sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Remove elements by index
new_list = [sample_list[i] for i in range(len(sample_list)) if i not in [0, 4, 5]]
print("List after removing 0th, 4th, and 5th elements:", new_list)
