class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        max_len = 1
        current_inc_len = 1
        current_dec_len = 1

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                current_inc_len += 1
                current_dec_len = 1
            elif nums[i] < nums[i-1]:
                current_dec_len += 1
                current_inc_len = 1
            else: # nums[i] == nums[i-1]
                current_inc_len = 1
                current_dec_len = 1

            max_len = max(max_len, current_inc_len, current_dec_len)
        
        return max_len