original_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_list = sorted(original_list, key=lambda x: x[1])

print("Original list of tuples:", original_list)
print("Sorting the List of Tuples:", sorted_list)
