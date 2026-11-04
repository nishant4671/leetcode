class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        N = len(arr)
        
        # First pass: Determine the effective length of the modified array
        # and the index of the last element from the original array that fits.
        end_idx = -1  # Pointer to the last element in original arr that will be considered
        write_idx = 0 # Pointer to where the current element would be written in an extended array
        
        for i in range(N):
            if arr[i] == 0:
                write_idx += 2
            else:
                write_idx += 1
            
            # If write_idx has reached or exceeded N,
            # then 'i' is the last original array index we care about.
            if write_idx >= N:
                end_idx = i
                break
            end_idx = i # If loop finishes, end_idx will be N-1
            
        # Handle the special case where the last element considered (arr[end_idx]) is 0
        # and duplicating it would cause write_idx to exactly overshoot N by 1.
        # In this scenario, the last zero is only written once at arr[N-1].
        
        # If write_idx > N, it implies arr[end_idx] must be 0 and caused the overshoot.
        # This zero (arr[end_idx]) will occupy arr[N-1] only (its duplicate is discarded).
        if write_idx > N:
            arr[N-1] = 0
            # Adjust pointers for the main reverse loop:
            # The last slot (N-1) is now taken by a single zero.
            # So, we start writing from N-2 backwards.
            # And the arr[end_idx] has been handled, so we start reading from end_idx - 1.
            dest_ptr = N - 2
            src_ptr = end_idx - 1
        else:
            # No overshoot, or exact fit.
            # Start writing from N-1 backwards.
            # Start reading from end_idx backwards.
            dest_ptr = N - 1
            src_ptr = end_idx
            
        # Second pass: Copy elements from right to left
        # using src_ptr for original array and dest_ptr for modified array.
        while src_ptr >= 0:
            if arr[src_ptr] == 0:
                # Duplicate the zero
                arr[dest_ptr] = 0
                dest_ptr -= 1 
                arr[dest_ptr] = 0
            else:
                arr[dest_ptr] = arr[src_ptr]
            
            src_ptr -= 1
            dest_ptr -= 1