original_list = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

divisible_by_19_or_13 = lambda x: x % 19 == 0 or x % 13 == 0

result = list(filter(divisible_by_19_or_13, original_list))
print("Original list:", original_list)
print("Numbers divisible by nineteen or thirteen:", result)
