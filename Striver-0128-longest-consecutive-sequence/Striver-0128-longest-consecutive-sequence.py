from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Handle the edge case of an empty array
        if not nums:
            return 0

        # Store all numbers in a hash set for O(1) average time lookups.
        # This also handles duplicate numbers automatically.
        num_set = set(nums)
        
        longest_sequence = 0

        # Iterate through each unique number in the set.
        # We only try to build a sequence if 'num' is its starting point.
        for num in num_set:
            # Check if 'num' is the start of a consecutive sequence.
            # A number 'num' is a starting point if 'num - 1' is not present in the set.
            if (num - 1) not in num_set:
                current_num = num
                current_sequence_length = 1

                # Extend the sequence by checking for consecutive numbers (num + 1, num + 2, ...)
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_sequence_length += 1
                
                # Update the maximum length found so far
                longest_sequence = max(longest_sequence, current_sequence_length)
        
        return longest_sequence