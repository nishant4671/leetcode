def is_subset(dict1, dict2):
    """
    Check if all elements with their quantities in dict1 are present in dict2
    """
    for key, quantity_needed in dict1.items():
        # Check if key exists in dict2
        if key not in dict2:
            return False
        # Check if dict2 has enough quantity
        if dict2[key] < quantity_needed:
            return False
    return True