original_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]

sort_mixed_list = lambda lst: sorted(lst, key=lambda x: (isinstance(x, int), x))

sorted_list = sort_mixed_list(original_list)

print("Original mixed list:", original_list)
print("Sort the mixed list:", sorted_list)
