from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store numbers and their indices.
        # Key: number, Value: index
        num_map = {} 
        
        # Iterate through the array with both index and value
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num
            
            # Check if the complement is already in our hash map
            if complement in num_map:
                # If it is, we found the two numbers.
                # Return the index of the complement and the current index.
                return [num_map[complement], i]
            
            # If the complement is not found, add the current number and its index 
            # to the hash map for future lookups.
            num_map[num] = i
        
        # According to the problem constraints, there will always be exactly one solution.
        # Therefore, the code should always find and return a pair of indices
        # within the loop, and this line should technically never be reached.
        # It's good practice to consider what to return if a solution isn't found,
        # but for this problem, it's not strictly necessary.
        # For instance, we could raise an error:
        # raise ValueError("No two sum solution")