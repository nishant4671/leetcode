class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_set = set(nums)
        ans = k
        while ans in num_set:
            ans += k
        return ans