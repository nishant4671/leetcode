class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        squared_nums = [x * x for x in nums]
        
        squared_nums.sort(reverse=True)
        
        max_score = 0
        
        positive_term_count = (n + 1) // 2 
        
        for i in range(n):
            if i < positive_term_count:
                max_score += squared_nums[i]
            else:
                max_score -= squared_nums[i]
                
        return max_score