class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        total_sum = sum(nums)

        # The problem asks to remove elements from the ends such that their sum equals x.
        # If we remove a prefix of length `L` and a suffix of length `R`,
        # the remaining elements form a contiguous subarray in the middle.
        # The sum of these remaining elements must be `total_sum - x`.
        # To minimize the number of removed elements (L + R), we need to maximize
        # the length of this middle subarray.

        target_sum_middle = total_sum - x

        # Case 1: If target_sum_middle is negative, it means sum of all elements is less than x.
        # So, it's impossible to make x exactly 0 by removing elements.
        if target_sum_middle < 0:
            return -1
        
        # Case 2: If target_sum_middle is 0, it means sum of all elements equals x.
        # We must remove all elements from the array. The number of operations is n.
        if target_sum_middle == 0:
            return n

        # Case 3: target_sum_middle is positive.
        # We need to find the longest contiguous subarray whose sum is target_sum_middle.
        
        max_len = -1  # Initialize max_len to -1, indicating no such subarray found yet.
        current_sum = 0
        left = 0

        # Use a sliding window approach to find the longest subarray with sum target_sum_middle.
        for right in range(n):
            current_sum += nums[right]
            
            # Shrink the window from the left if current_sum exceeds target_sum_middle.
            # Since nums[i] >= 1, current_sum is always increasing or staying same (if element is 0, not in this problem)
            # So, if current_sum > target_sum_middle, we must remove elements from left.
            while current_sum > target_sum_middle and left <= right:
                current_sum -= nums[left]
                left += 1
            
            # If current_sum equals target_sum_middle, we've found a valid subarray.
            # Update max_len with the length of this subarray.
            if current_sum == target_sum_middle:
                max_len = max(max_len, right - left + 1)
        
        # If max_len is still -1 after checking all subarrays, it means no subarray
        # with the required sum was found. So, it's impossible to make x exactly 0.
        if max_len == -1:
            return -1
        else:
            # The minimum number of operations is n minus the length of the longest
            # middle subarray (which remains).
            return n - max_len