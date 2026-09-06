from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        current_consecutive = 0

        for num in nums:
            if num == 1:
                # If the current number is 1, increment the counter for the current sequence
                current_consecutive += 1
            else:  # num is 0
                # If the current number is 0, the sequence of 1s is broken.
                # First, update max_consecutive if the current sequence was longer.
                max_consecutive = max(max_consecutive, current_consecutive)
                # Then, reset current_consecutive to 0 to start counting a new sequence.
                current_consecutive = 0
        
        # After the loop finishes, there might be a trailing sequence of 1s
        # that was never followed by a 0. The current_consecutive would hold its length.
        # We need to compare this final current_consecutive with max_consecutive one last time.
        max_consecutive = max(max_consecutive, current_consecutive)
        
        return max_consecutive