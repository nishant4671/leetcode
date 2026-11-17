class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()

        left = 0
        current_sum = 0
        max_frequency = 0 

        for right in range(len(nums)):
            current_sum += nums[right]
            
            # The cost to make all elements in the current window nums[left...right]
            # equal to nums[right] is calculated as:
            # (target_sum_for_window - actual_sum_of_window)
            # where target_sum_for_window = (window_size * nums[right])
            # and actual_sum_of_window = current_sum.
            # window_size = (right - left + 1).
            
            # If the operations needed exceed k, shrink the window from the left.
            while (right - left + 1) * nums[right] - current_sum > k:
                current_sum -= nums[left]
                left += 1
            
            # The current window [left...right] is valid (operations <= k).
            # Its length (right - left + 1) is a possible frequency.
            max_frequency = max(max_frequency, right - left + 1)
        
        return max_frequency