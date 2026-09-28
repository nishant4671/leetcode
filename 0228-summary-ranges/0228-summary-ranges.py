class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []

        result = []
        i = 0
        n = len(nums)

        while i < n:
            start = nums[i]
            j = i 

            while j + 1 < n and nums[j+1] == nums[j] + 1:
                j += 1
            
            end = nums[j]

            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}->{end}")
            
            i = j + 1
        
        return result