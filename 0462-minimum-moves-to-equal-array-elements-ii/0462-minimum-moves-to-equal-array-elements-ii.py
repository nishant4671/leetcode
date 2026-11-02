class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        
        median = nums[n // 2]
        
        total_moves = 0
        for num in nums:
            total_moves += abs(num - median)
            
        return total_moves