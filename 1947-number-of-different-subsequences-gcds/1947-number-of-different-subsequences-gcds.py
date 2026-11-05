import math

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: list[int]) -> int:
        if not nums:
            return 0
        M = max(nums)
        cnt = [0] * (M + 1)
        for x in nums:
            cnt[x] += 1
        ans = 0
        for g in range(1, M + 1):
            cur = 0
            for mult in range(g, M + 1, g):
                if cnt[mult]:
                    cur = math.gcd(cur, mult)
                    if cur == g:
                        break
            if cur == g:
                ans += 1
        return ans