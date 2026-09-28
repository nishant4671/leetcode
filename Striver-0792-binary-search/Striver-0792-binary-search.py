class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            # Calculate mid index.
            # Using left + (right - left) // 2 prevents potential overflow
            # compared to (left + right) // 2 for very large left/right values,
            # though it's less of an issue in Python.
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid  # Target found, return its index
            elif nums[mid] < target:
                # Target is in the right half, so discard the left half
                left = mid + 1
            else: # nums[mid] > target
                # Target is in the left half, so discard the right half
                right = mid - 1
        
        # If the loop finishes, the target was not found in the array
        return -1