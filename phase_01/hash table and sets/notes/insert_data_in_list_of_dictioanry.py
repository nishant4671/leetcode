# Initialize list of dictionaries
nums = [1, 2, 3, 4, 5]
list_of_dicts = [{} for _ in nums]

# Insert data into each dictionary
for i, num in enumerate(nums):
    list_of_dicts[i]["value"] = num
    list_of_dicts[i]["squared"] = num ** 2
    list_of_dicts[i]["is_even"] = num % 2 == 0

print(list_of_dicts)
# [
#   {'value': 1, 'squared': 1, 'is_even': False},
#   {'value': 2, 'squared': 4, 'is_even': True},
#   {'value': 3, 'squared': 9, 'is_even': False},
#   {'value': 4, 'squared': 16, 'is_even': True},
#   {'value': 5, 'squared': 25, 'is_even': False}
# ]