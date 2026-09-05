from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Calculate the sum of all integers from 0 to n.
        # This uses the formula for the sum of an arithmetic series: n * (n + 1) / 2.
        # For example, if n=3, the full range of numbers is [0, 1, 2, 3].
        # The expected sum would be 0 + 1 + 2 + 3 = 6.
        # Using the formula: 3 * (3 + 1) // 2 = 3 * 4 // 2 = 6.
        expected_sum = n * (n + 1) // 2
        
        # Calculate the actual sum of numbers present in the given array `nums`.
        # For example, if nums = [3, 0, 1], the actual sum is 3 + 0 + 1 = 4.
        actual_sum = sum(nums)
        
        # The difference between the expected sum and the actual sum
        # will be the single number that is missing from the array.
        # In the example: 6 (expected) - 4 (actual) = 2 (missing number).
        return expected_sum - actual_sum