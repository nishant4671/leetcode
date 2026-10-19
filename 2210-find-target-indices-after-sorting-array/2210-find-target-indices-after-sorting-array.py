class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        count_less = 0
        count_equal = 0

        for num in nums:
            if num < target:
                count_less += 1
            elif num == target:
                count_equal += 1
        
        result = []
        for i in range(count_equal):
            result.append(count_less + i)
            
        return result