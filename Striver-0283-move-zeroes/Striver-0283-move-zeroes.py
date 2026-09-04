class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # write_idx tracks the position for the next non-zero element.
        # It also marks the boundary between non-zero elements (to its left)
        # and elements that are either zeros or will become zeros (to its right).
        write_idx = 0 
        
        # Iterate through the array with read_idx.
        for read_idx in range(len(nums)):
            # If the element at read_idx is non-zero, it needs to be moved
            # to the position indicated by write_idx.
            if nums[read_idx] != 0:
                # If read_idx and write_idx are different, it means nums[read_idx]
                # is a non-zero element found after a zero (or a position that
                # has been processed as a zero). A swap is necessary to move
                # the non-zero element to its correct place at write_idx,
                # effectively moving the zero element (at nums[write_idx]) to read_idx.
                # If read_idx == write_idx, the non-zero element is already in
                # its correct relative position, so no actual swap (data movement)
                # is needed. We just advance write_idx.
                if read_idx != write_idx:
                    nums[write_idx], nums[read_idx] = nums[read_idx], nums[write_idx]
                
                # Advance write_idx to the next position for a non-zero element.
                write_idx += 1