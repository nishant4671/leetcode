class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        dq = collections.deque()
        
        dq.append(0)
        
        for i in range(1, n):
            while dq and dq[0] < i - k:
                dq.popleft()
            
            nums[i] += nums[dq[0]]
            
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            
            dq.append(i)
            
        return nums[n-1]

import collections