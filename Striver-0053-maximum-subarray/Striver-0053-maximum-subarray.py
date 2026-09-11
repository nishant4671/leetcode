from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm:
        # This algorithm finds the maximum sum of a contiguous subarray.

        # `current_max` keeps track of the maximum sum of a subarray ending at the current position.
        # It's initialized to 0. If current_max (sum of previous elements) becomes negative, 
        # it means extending the subarray is worse than starting a new one. 
        # The `max(num, current_max + num)` step handles this logic implicitly.
        current_max = 0 
        
        # `global_max` stores the overall maximum sum found across all subarrays processed so far.
        # It's initialized to negative infinity (`float('-inf')`) to ensure that any
        # valid sum (even a single negative number, like -1 in [-2, -1, -3]) will be greater
        # and correctly update `global_max`. The problem constraints guarantee
        # `nums.length >= 1`, so there will always be at least one number to update it.
        global_max = float('-inf') 
        
        # Iterate through each number in the input array.
        for num in nums:
            # For each `num`, we decide whether to extend the subarray ending at the previous
            # position or start a new subarray with `num`.
            # - If `current_max + num` is greater than `num`, it means extending the current
            #   subarray (current_max) with `num` is beneficial.
            # - If `num` is greater than `current_max + num`, it means the `current_max`
            #   (sum of previous elements) was negative or made `current_max + num` smaller
            #   than `num`. In this case, it's better to "reset" and start a new subarray 
            #   from `num` itself.
            current_max = max(num, current_max + num)
            
            # After updating `current_max` for the subarray ending at the current `num`,
            # compare it with `global_max` to see if we've found a new overall maximum.
            global_max = max(global_max, current_max)
            
        # After iterating through all elements, `global_max` will hold the maximum subarray sum.
        return global_max