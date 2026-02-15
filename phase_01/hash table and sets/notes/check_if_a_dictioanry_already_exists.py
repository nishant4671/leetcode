# List of dictionaries
list_of_dicts = [
    {"name": "apple", "count": 5},
    {"name": "banana", "count": 3},
    {"name": "orange", "count": 2}
]

# Dictionary to check
my_dict = {"name": "banana", "count": 3}

# Check if the dictionary exists in the list
if my_dict in list_of_dicts:
    print("Found! The dictionary is in the list")
else:
    print("Not found")
# Output: Found! The dictionary is in the list