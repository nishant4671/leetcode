from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            # Ensure mid is even so we can compare with the next element
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                # The single element is after this pair
                low = mid + 2
            else:
                # The single element is at mid or before
                high = mid
        return nums[low]