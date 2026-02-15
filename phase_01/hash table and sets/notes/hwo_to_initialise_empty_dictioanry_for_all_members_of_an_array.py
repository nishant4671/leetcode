# Create a separate dictionary for each element
nums = [1, 2, 3, 4, 5]
list_of_dicts = []

for num in nums:
    list_of_dicts.append({})  # Empty dictionary for each element

print(list_of_dicts)  # [{}, {}, {}, {}, {}]

# Or with dictionary comprehension
list_of_dicts = [{} for _ in nums]
print(list_of_dicts)  # [{}, {}, {}, {}, {}]