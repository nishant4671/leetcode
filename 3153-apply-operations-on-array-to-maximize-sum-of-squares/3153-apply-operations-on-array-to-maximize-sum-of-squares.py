import sys
from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        BIT = 31
        cnt = [0] * BIT
        for x in nums:
            for b in range(BIT):
                if x >> b & 1:
                    cnt[b] += 1
        ans = 0
        for _ in range(k):
            cur = 0
            for b in range(BIT):
                if cnt[b]:
                    cur |= (1 << b)
                    cnt[b] -= 1
            ans = (ans + cur * cur) % MOD
        return ans