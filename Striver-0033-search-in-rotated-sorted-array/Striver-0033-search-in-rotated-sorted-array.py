class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            # Determine which half is sorted
            if nums[low] <= nums[mid]:
                # The left half [low...mid] is sorted
                # Check if target is in this sorted left half
                if nums[low] <= target < nums[mid]:
                    # Target is in the left half, so discard the right half
                    high = mid - 1
                else:
                    # Target is not in the left sorted half,
                    # so it must be in the right (unsorted or rotated) half
                    low = mid + 1
            else:
                # The right half [mid...high] is sorted
                # (because nums[low] > nums[mid] implies the pivot is in the left half)
                # Check if target is in this sorted right half
                if nums[mid] < target <= nums[high]:
                    # Target is in the right half, so discard the left half
                    low = mid + 1
                else:
                    # Target is not in the right sorted half,
                    # so it must be in the left (unsorted or rotated) half
                    high = mid - 1
        
        # If the loop finishes, target was not found
        return -1