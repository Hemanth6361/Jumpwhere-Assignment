original_matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
original_matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

sort_matrix_by_row_sum = lambda matrix: sorted(matrix, key=lambda row: sum(row))

sorted_matrix1 = sort_matrix_by_row_sum(original_matrix1)
sorted_matrix2 = sort_matrix_by_row_sum(original_matrix2)

print("Original Matrix 1:", original_matrix1)
print("Sort the matrix by row sum:", sorted_matrix1)

print("Original Matrix 2:", original_matrix2)
print("Sort the matrix by row sum:", sorted_matrix2)
