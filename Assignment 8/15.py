is_number = lambda string: string.replace(".", "", 1).isdigit()

string1 = "12345"
string2 = "12.34"
string3 = "abc"

result1 = is_number(string1)
result2 = is_number(string2)
result3 = is_number(string3)

print(result1, result2, result3)  # Output: True True False
