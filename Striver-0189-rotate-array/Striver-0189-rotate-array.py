class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Normalize k to be within [0, n-1]

        # If k is 0 after modulo, no rotation is needed.
        # This handles cases where k is a multiple of n, or k is 0 initially.
        if k == 0:
            return

        # Helper function to reverse a sub-array in-place
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        # The three-reversal algorithm:
        # This algorithm performs the rotation in O(n) time and O(1) space.
        
        # Step 1: Reverse the entire array.
        # This brings the elements that should be at the end to the beginning,
        # and vice versa, but in reversed order.
        # Example: nums = [1,2,3,4,5,6,7], k=3
        # After this step: [7,6,5,4,3,2,1]
        reverse(nums, 0, n - 1)
        
        # Step 2: Reverse the first k elements.
        # These are the elements that originally occupied the last k positions
        # and after step 1 are now at the beginning (but reversed).
        # Reversing them again puts them in their correct final order.
        # Example: From [7,6,5,4,3,2,1] (where k=3)
        # Reverse [7,6,5]: [5,6,7,4,3,2,1]
        reverse(nums, 0, k - 1)
        
        # Step 3: Reverse the remaining n-k elements.
        # These are the elements that originally occupied the first n-k positions
        # and after step 1 are now at the end (but reversed).
        # Reversing them again puts them in their correct final order.
        # Example: From [5,6,7,4,3,2,1] (where k=3, n-k=4)
        # Reverse [4,3,2,1]: [5,6,7,1,2,3,4]
        reverse(nums, k, n - 1)