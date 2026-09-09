from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # Pointers for the three regions:
        # [0...low-1] contains all 0s
        # [low...mid-1] contains all 1s
        # [mid...high] contains unknown elements
        # [high+1...n-1] contains all 2s
        
        low = 0    # Pointer for the next position to place a 0
        mid = 0    # Current element under consideration
        high = n - 1 # Pointer for the next position to place a 2

        while mid <= high:
            if nums[mid] == 0:
                # If current element is 0, swap it with the element at 'low' pointer.
                # Increment both 'low' and 'mid' pointers.
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # If current element is 1, it's already in its correct relative position.
                # Just move the 'mid' pointer forward.
                mid += 1
            else: # nums[mid] == 2
                # If current element is 2, swap it with the element at 'high' pointer.
                # Decrement 'high' pointer.
                # Do NOT increment 'mid' because the element swapped into 'nums[mid]'
                # could be 0, 1, or 2 and needs to be re-evaluated.
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1