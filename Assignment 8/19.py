original_list = ['red', 'black', 'white', 'green', 'orange']
substring_to_search1 = "ack"
substring_to_search2 = "abc"

contains_substring = lambda s, sub: sub in s

result1 = list(filter(lambda x: contains_substring(x, substring_to_search1), original_list))
result2 = list(filter(lambda x: contains_substring(x, substring_to_search2), original_list))

print("Original list:", original_list)
print("Substring to search:", substring_to_search1)
print("Elements containing the specific substring:", result1)

print("Substring to search:", substring_to_search2)
print("Elements containing the specific substring:", result2)
