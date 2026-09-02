from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # `write_ptr` keeps track of the position where the next unique element should be placed.
        # It effectively points to the end of the unique sub-array (exclusive).
        # Since `nums[0]` is always unique (if `nums` is not empty), the first unique element
        # is already in place at index 0. So, the next unique element should be written
        # starting from index 1.
        write_ptr = 1
        
        # `read_ptr` iterates through the array from the second element.
        # Its purpose is to find new unique elements.
        for read_ptr in range(1, len(nums)):
            # If the element at `read_ptr` is different from the last unique element
            # identified and placed (which is at `nums[write_ptr - 1]`),
            # then we have found a new unique element.
            if nums[read_ptr] != nums[write_ptr - 1]:
                # Place this new unique element into the position indicated by `write_ptr`.
                nums[write_ptr] = nums[read_ptr]
                # Increment `write_ptr` to point to the next available slot for a unique element.
                write_ptr += 1
                
        # After iterating through the entire array, `write_ptr` will represent
        # the total count of unique elements. This is `k`.
        return write_ptr