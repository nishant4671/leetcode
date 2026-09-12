from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []

        # Separate positive and negative numbers while preserving their original order.
        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)

        n = len(nums)
        result = [0] * n  # Pre-allocate the result array for efficiency.

        # Construct the rearranged array by alternating positive and negative numbers.
        # The i-th positive number goes to result[2*i] (even index).
        # The i-th negative number goes to result[2*i + 1] (odd index).
        # This naturally satisfies all three conditions:
        # 1. Starts with positive (positives[0] at result[0]).
        # 2. Alternating signs (positive at even, negative at odd).
        # 3. Order preserved (by taking elements from 'positives' and 'negatives' sequentially).
        
        # There are n/2 positive and n/2 negative numbers.
        for i in range(n // 2):
            result[2 * i] = positives[i]
            result[2 * i + 1] = negatives[i]
            
        return result