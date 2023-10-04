check_string = lambda s: any(c.isupper() for c in s) and any(c.islower() for c in s) and any(c.isdigit() for c in s) and len(s) >= 10

input_string = "PaceWisd0m"
result = check_string(input_string)

if result:
    print("Valid string")
else:
    print("Invalid string")
