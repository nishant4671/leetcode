class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]

        # Helper function to find the first occurrence of the target
        def find_first_occurrence(arr, t):
            low, high = 0, n - 1
            first_idx = -1
            while low <= high:
                mid = low + (high - low) // 2
                if arr[mid] == t:
                    first_idx = mid
                    # Target found, but it might not be the first one.
                    # Try to find an even smaller index in the left half.
                    high = mid - 1
                elif arr[mid] < t:
                    # Target is in the right half
                    low = mid + 1
                else: # arr[mid] > t
                    # Target is in the left half
                    high = mid - 1
            return first_idx

        # Helper function to find the last occurrence of the target
        def find_last_occurrence(arr, t):
            low, high = 0, n - 1
            last_idx = -1
            while low <= high:
                mid = low + (high - low) // 2
                if arr[mid] == t:
                    last_idx = mid
                    # Target found, but it might not be the last one.
                    # Try to find an even larger index in the right half.
                    low = mid + 1
                elif arr[mid] < t:
                    # Target is in the right half
                    low = mid + 1
                else: # arr[mid] > t
                    # Target is in the left half
                    high = mid - 1
            return last_idx

        start_index = find_first_occurrence(nums, target)
        
        # If the target was not found at all, find_first_occurrence will return -1.
        # In this case, the last occurrence also doesn't exist.
        if start_index == -1:
            return [-1, -1]
        
        # If target was found (start_index is not -1), proceed to find its last occurrence.
        end_index = find_last_occurrence(nums, target)
        
        return [start_index, end_index]