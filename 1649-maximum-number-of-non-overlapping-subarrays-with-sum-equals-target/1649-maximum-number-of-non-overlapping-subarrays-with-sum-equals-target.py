class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        count = 0
        current_sum = 0
        # Stores prefix sums encountered since the last successful subarray match.
        # Initialize with 0 to account for subarrays that start from the very beginning 
        # of the current segment (either nums[0] or after a previous reset).
        seen_prefix_sums = {0} 

        for num in nums:
            current_sum += num
            
            # Check if there's a previous prefix sum 'P' such that 'current_sum - P == target'.
            # This implies a subarray ending at the current position with sum 'target'.
            if current_sum - target in seen_prefix_sums:
                count += 1
                # If a valid subarray is found, we make a greedy choice:
                # we count it and then reset our state to start searching for
                # the next non-overlapping subarray from the *next* element.
                # This is done by resetting current_sum to 0 and 
                # seen_prefix_sums to contain only 0.
                current_sum = 0
                seen_prefix_sums = {0}
            else:
                # If no subarray ending here sums to target (yet), 
                # add the current_sum to the set of seen prefix sums.
                # This prefix sum might be used later to form a subarray.
                seen_prefix_sums.add(current_sum)
                
        return count