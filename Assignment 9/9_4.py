def convert_to_positive_coordinates(coordinates):
   
    min_x = min(coord[0] for coord in coordinates)
    min_y = min(coord[1] for coord in coordinates)

    
    offset_x = abs(min_x)
    offset_y = abs(min_y)

    positive_coordinates = [(coord[0] + offset_x, coord[1] + offset_y) for coord in coordinates]

    return positive_coordinates

input_coordinates = [(1, -2), (-2, 4), (-1, -1), (-8, -3), (0, 4), (10, -3)]
output_coordinates = convert_to_positive_coordinates(input_coordinates)
print(output_coordinates)
