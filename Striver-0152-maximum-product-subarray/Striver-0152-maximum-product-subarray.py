class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # Constraints guarantee that nums.length >= 1, so nums will not be empty.

        # Initialize current_max_prod and current_min_prod with the first element.
        # current_max_prod tracks the maximum product of a subarray ending at the current position.
        # current_min_prod tracks the minimum product of a subarray ending at the current position.
        # This is crucial because multiplying a small negative by another negative can yield a large positive.
        current_max_prod = nums[0]
        current_min_prod = nums[0]
        
        # overall_max_prod stores the maximum product encountered anywhere in the array.
        overall_max_prod = nums[0]

        # Iterate through the array starting from the second element.
        for i in range(1, len(nums)):
            num = nums[i]
            
            # Store the current_max_prod from the previous iteration.
            # This is necessary because current_min_prod's calculation might
            # need the *old* current_max_prod before it gets updated for the current element.
            temp_max_prod = current_max_prod 
            
            # The new current_max_prod could be:
            # 1. The number itself (starting a new subarray).
            # 2. Product of num and the previous current_max_prod.
            # 3. Product of num and the previous current_min_prod (if num is negative, 
            #    this could turn a large negative into a large positive).
            current_max_prod = max(num, current_max_prod * num, current_min_prod * num)
            
            # Similarly, the new current_min_prod could be:
            # 1. The number itself.
            # 2. Product of num and the previous current_max_prod (if num is negative,
            #    this could turn a large positive into a large negative).
            # 3. Product of num and the previous current_min_prod.
            current_min_prod = min(num, temp_max_prod * num, current_min_prod * num)
            
            # Update the overall maximum product found so far.
            overall_max_prod = max(overall_max_prod, current_max_prod)
            
        return overall_max_prod