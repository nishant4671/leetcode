from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Boyer-Moore Voting Algorithm
        # This algorithm finds the majority element in O(n) time and O(1) space.
        # It relies on the fact that if an element is a majority element,
        # it will appear more than n/2 times, outnumbering all other elements combined.
        # The problem statement guarantees that a majority element always exists,
        # so a second pass to verify the candidate is not needed.

        candidate = 0  # Initialize candidate. Its initial value doesn't matter as it will be overwritten.
        count = 0      # Initialize count for the current candidate.

        for num in nums:
            if count == 0:
                # If count is 0, it means the current candidate (if any) has been "canceled out".
                # We pick the current number as the new potential candidate.
                candidate = num
                count = 1
            elif num == candidate:
                # If the current number is the same as the candidate, increment its count.
                count += 1
            else:
                # If the current number is different, it "cancels out" one instance of the candidate.
                count -= 1
        
        # After iterating through all elements, the 'candidate' variable will hold
        # the majority element because its occurrences overwhelmed all others.
        return candidate