class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        
        # Helper function to check if it's possible to split nums into `k`
        # or fewer subarrays, where each subarray's sum does not exceed `max_sum_limit`.
        def check(max_sum_limit: int) -> bool:
            current_sum = 0
            num_subarrays = 1 # Start with the first subarray
            
            for num in nums:
                # If adding the current number to the current subarray exceeds the limit,
                # we must start a new subarray.
                if current_sum + num > max_sum_limit:
                    num_subarrays += 1
                    current_sum = num # Start the new subarray with the current number
                    
                    # This check (num > max_sum_limit) is technically redundant for this problem
                    # because the binary search lower bound `low` is initialized to `max(nums)`.
                    # Any `mid` value (which becomes `max_sum_limit`) will thus always be
                    # greater than or equal to `max(nums)`. Since `num` is an element of `nums`,
                    # `num <= max(nums) <= max_sum_limit` will always hold true.
                    # However, in a more general scenario (e.g., negative numbers, or if `low` 
                    # was initialized to 0), this check would be crucial to handle cases where 
                    # a single element itself exceeds `max_sum_limit`.
                    if num > max_sum_limit: 
                         return False 
                else:
                    current_sum += num
            
            # We succeeded if the number of subarrays required is k or less.
            return num_subarrays <= k

        # The search space for the minimized largest sum:
        # The lower bound: The largest single element in nums. 
        # (Each element must be in some subarray, so the max sum must be at least the largest element).
        # This ensures that even the largest number fits into a subarray.
        low = max(nums)
        
        # The upper bound: The sum of all elements in nums.
        # (If k=1, the entire array is one subarray, and its sum is the largest possible sum).
        high = sum(nums)
        
        # 'ans' will store the minimum valid 'max_sum_limit' found.
        # Initialize with 'high' as it's a valid (though not necessarily optimal) answer.
        ans = high 
        
        # Binary search to find the smallest `max_sum_limit` that satisfies `check(max_sum_limit)`.
        while low <= high:
            mid = low + (high - low) // 2
            
            if check(mid):
                # If `mid` is a possible maximum sum, it means we can split
                # the array into `k` or fewer subarrays with this max sum.
                # This `mid` could be our answer, or maybe an even smaller sum is possible.
                ans = mid
                high = mid - 1 # Try to find a smaller possible maximum sum in the left half
            else:
                # If `mid` is not possible, it means `mid` is too small to split
                # the array into `k` subarrays with sums not exceeding `mid`.
                # We need a larger maximum sum.
                low = mid + 1 # Search in the right half for a larger possible maximum sum
                
        return ans