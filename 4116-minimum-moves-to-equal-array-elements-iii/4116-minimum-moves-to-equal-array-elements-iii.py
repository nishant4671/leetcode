from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # The problem asks for the minimum total moves to make all elements in 'nums' equal.
        # In one move, we can increase the value of any single element nums[i] by 1.

        # Let the target value to which all elements will become equal be 'k'.
        # Since we can only *increase* elements, 'k' must be greater than or equal
        # to the maximum element currently in 'nums'. If 'k' were less than max(nums),
        # it would be impossible to reach 'k' for all elements by only increasing them.

        # The total number of moves required to make all elements equal to 'k' is:
        # moves = sum(k - num for num in nums)
        # This can be expanded as:
        # moves = (k - nums[0]) + (k - nums[1]) + ... + (k - nums[n-1])
        # moves = n * k - sum(nums)
        # where 'n' is the number of elements in 'nums'.

        # To minimize the total 'moves', we need to minimize 'n * k'.
        # Since 'n' is constant and positive, we must minimize 'k'.
        # As established, the smallest possible value for 'k' is the maximum element
        # in the original 'nums' array.
        # If we choose k = max(nums) + x where x > 0, the moves would be
        # (n * (max(nums) + x)) - sum(nums) = (n * max(nums) - sum(nums)) + n * x.
        # This is clearly greater than when x = 0 (i.e., k = max(nums)).

        # Therefore, the optimal strategy is to increase all elements until they reach
        # the value of the maximum element in the initial array.

        # Calculate the number of elements in the array
        n = len(nums)
        
        # Find the maximum element in the array. This will be our target value 'k'.
        max_val = max(nums)
        
        # Calculate the sum of all elements in the array.
        total_sum = sum(nums)
            
        # Apply the derived formula: n * max_val - total_sum
        return n * max_val - total_sum