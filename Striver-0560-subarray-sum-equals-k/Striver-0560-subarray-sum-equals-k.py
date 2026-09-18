import collections
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        
        # A dictionary to store the frequency of prefix sums encountered so far.
        # Key: prefix sum, Value: frequency
        # Using collections.defaultdict(int) simplifies handling cases where a key
        # might not yet exist; it defaults to 0.
        prefix_sum_counts = collections.defaultdict(int)
        
        # Initialize with a prefix sum of 0 having a count of 1.
        # This is crucial for handling subarrays that start from index 0 and sum to `k`.
        # If `current_sum` becomes `k` at some point (meaning `nums[0...j]` sums to `k`),
        # then `current_sum - k == 0`. By having `prefix_sum_counts[0] = 1` initially,
        # we correctly count this subarray starting from index 0.
        prefix_sum_counts[0] = 1 
        
        for num in nums:
            current_sum += num
            
            # We are looking for a previous prefix sum, `P_i`, such that:
            # `current_sum - P_i = k` (where `current_sum` is `P_{j+1}`)
            # Rearranging, we need to find `P_i = current_sum - k`.
            # The number of times `current_sum - k` has appeared as a prefix sum `P_i`
            # tells us how many subarrays ending at the current position `j` sum to `k`.
            count += prefix_sum_counts[current_sum - k]
            
            # Increment the frequency of the current `current_sum` in the map.
            # This `current_sum` will be `P_{j+1}` for subsequent iterations.
            prefix_sum_counts[current_sum] += 1
            
        return count