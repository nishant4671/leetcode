class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_distance = float('inf')
        n = len(nums)
        
        for i in range(n):
            if nums[i] == target:
                current_distance = abs(i - start)
                if current_distance < min_distance:
                    min_distance = current_distance
        
        return min_distance