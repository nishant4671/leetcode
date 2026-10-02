class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # If nums[mid] is greater than nums[right],
            # it means the minimum element must be in the right half (mid+1 to right).
            # This happens when 'mid' is in the first (larger) sorted part
            # and 'right' is in the second (smaller) sorted part,
            # indicating the pivot (minimum) is to the right of 'mid'.
            if nums[mid] > nums[right]:
                left = mid + 1
            # If nums[mid] is less than nums[right],
            # it means the array segment from 'mid' to 'right' is sorted.
            # The minimum element is either nums[mid] itself or somewhere in the left half
            # (between 'left' and 'mid-1'). We cannot discard nums[mid] as it could be the minimum.
            # The elements from mid+1 to right are all greater than nums[mid].
            # (Note: nums[mid] == nums[right] is not possible because elements are unique).
            else: # nums[mid] < nums[right]
                right = mid
        
        # When the loop terminates, left == right.
        # This index points to the minimum element.
        return nums[left]