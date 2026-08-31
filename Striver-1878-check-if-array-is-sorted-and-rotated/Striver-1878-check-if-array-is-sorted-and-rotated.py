from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # Count the number of "breaks" where an element is strictly greater than its successor.
        # In a non-decreasing array, there are zero such breaks.
        # In a rotated non-decreasing array, there should be at most one such break
        # when considering elements linearly from index 0 to n-2.
        
        violations = 0
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                violations += 1
        
        # Analyze based on the number of identified violations:
        if violations == 0:
            # If no violations, the array is already sorted in non-decreasing order.
            # This is a valid case (equivalent to 0 rotations).
            # Examples: [1,2,3], [3,3,3]
            return True
        elif violations == 1:
            # If exactly one violation, it means there's one "descent" in the linear scan.
            # This could be a valid rotated sorted array.
            # For it to be truly valid, the "wrap-around" condition must also hold:
            # The last element of the array must be less than or equal to the first element.
            # This ensures that if we conceptually place the second segment before the first,
            # the combined sequence remains non-decreasing.
            # Example: For nums = [3,4,5,1,2], the violation is 5 > 1.
            # The check is nums[4] (2) <= nums[0] (3), which is True. So, it's valid.
            # Example: For nums = [2,1,3,4], the violation is 2 > 1.
            # The check is nums[3] (4) <= nums[0] (2), which is False. So, it's invalid.
            return nums[n-1] <= nums[0]
        else: # violations > 1
            # If there are more than one violations, the array cannot be formed by a single rotation
            # of a non-decreasingly sorted array.
            # Example: [3,2,1] has two violations (3>2 and 2>1), hence it's invalid.
            return False