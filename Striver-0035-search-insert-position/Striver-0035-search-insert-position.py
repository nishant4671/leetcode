class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # Target is in the right half, so search from mid + 1
                low = mid + 1
            else:  # nums[mid] > target
                # Target is in the left half, so search up to mid - 1
                high = mid - 1

        # If the loop finishes, the target was not found.
        # 'low' now indicates the insertion point.
        # It's the index where the first element greater than or equal to target would be.
        return low