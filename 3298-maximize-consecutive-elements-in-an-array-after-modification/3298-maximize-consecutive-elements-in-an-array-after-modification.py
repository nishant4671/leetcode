import collections
from typing import List

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        # Sort the input array. This helps in processing numbers in increasing order,
        # which is crucial for dynamic programming where states depend on smaller values.
        nums.sort()
        
        # dp[x] will store the maximum length of a consecutive sequence ending with value x.
        # We use collections.defaultdict(int) so that accessing a non-existent key returns 0,
        # which correctly represents a base case (an empty sequence before x).
        dp = collections.defaultdict(int)
        
        # Initialize the maximum overall length found so far to 0.
        max_overall_len = 0
        
        # Iterate through each number in the sorted array.
        for num in nums:
            # For each 'num', we have two choices for how to use it:
            # 1. Use 'num' as its current value 'num'.
            #    If we use 'num' as 'num', it can extend a consecutive sequence that ends at 'num-1'.
            #    The length of such a sequence would be dp[num-1] + 1.
            # 2. Use 'num' by incrementing it to 'num+1'.
            #    If we use 'num' as 'num+1', it can extend a consecutive sequence that ends at 'num'.
            #    The length of such a sequence would be dp[num] + 1.

            # It's important to capture the 'dp[num]' value *before* it potentially gets updated
            # by the current 'num' itself (if 'num' is used as 'num').
            # This ensures that when we calculate `len_if_num_becomes_plus_1`, it correctly refers
            # to a sequence that does NOT include the current `num` (used as `num`).
            
            # Calculate the potential length if 'num' becomes 'num+1'.
            # This relies on a sequence ending at 'num' (from previous numbers or a base case).
            len_if_num_becomes_plus_1 = dp[num] + 1
            
            # Calculate the potential length if 'num' stays 'num'.
            # This relies on a sequence ending at 'num-1' (from previous numbers or a base case).
            len_if_num_stays_num = dp[num-1] + 1
            
            # Update the DP table:
            # First, update dp[num+1]. We take the maximum of its current value and the newly calculated length.
            dp[num+1] = max(dp[num+1], len_if_num_becomes_plus_1)
            
            # Next, update dp[num]. We take the maximum of its current value and the newly calculated length.
            # The calculation for dp[num] uses dp[num-1], which is guaranteed to be from numbers strictly
            # smaller than the current 'num', so there's no dependency issue.
            dp[num] = max(dp[num], len_if_num_stays_num)
            
            # Update the overall maximum length observed across all possible ending values.
            max_overall_len = max(max_overall_len, dp[num], dp[num+1])
            
        return max_overall_len