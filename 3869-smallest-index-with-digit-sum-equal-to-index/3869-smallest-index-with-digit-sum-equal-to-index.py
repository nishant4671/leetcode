class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        def sum_digits(n: int) -> int:
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s

        for i in range(len(nums)):
            if sum_digits(nums[i]) == i:
                return i
        
        return -1