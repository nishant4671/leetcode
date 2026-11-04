import sys, heapq, collections
from typing import List

class SlidingWindowCost:
    def __init__(self):
        self.low = []   # max-heap (store -val)
        self.high = []  # min-heap
        self.delayed = collections.Counter()
        self.sumLow = 0
        self.sumHigh = 0
        self.sizeLow = 0
        self.sizeHigh = 0

    def _prune(self, heap):
        while heap:
            val = -heap[0] if heap is self.low else heap[0]
            if self.delayed[val]:
                self.delayed[val] -= 1
                if self.delayed[val] == 0:
                    del self.delayed[val]
                heapq.heappop(heap)
            else:
                break

    def _balance(self):
        # ensure sizeLow >= sizeHigh and diff <=1
        if self.sizeLow > self.sizeHigh + 1:
            val = -heapq.heappop(self.low)
            self.sumLow -= val
            self.sizeLow -= 1
            heapq.heappush(self.high, val)
            self.sumHigh += val
            self.sizeHigh += 1
        elif self.sizeLow < self.sizeHigh:
            val = heapq.heappop(self.high)
            self.sumHigh -= val
            self.sizeHigh -= 1
            heapq.heappush(self.low, -val)
            self.sumLow += val
            self.sizeLow += 1
        self._prune(self.low)
        self._prune(self.high)

    def add(self, num: int):
        if not self.low or num <= -self.low[0]:
            heapq.heappush(self.low, -num)
            self.sumLow += num
            self.sizeLow += 1
        else:
            heapq.heappush(self.high, num)
            self.sumHigh += num
            self.sizeHigh += 1
        self._balance()

    def remove(self, num: int):
        self.delayed[num] += 1
        if self.low and num <= -self.low[0]:
            self.sumLow -= num
            self.sizeLow -= 1
            if -self.low[0] == num:
                self._prune(self.low)
        else:
            self.sumHigh -= num
            self.sizeHigh -= 1
            if self.high and self.high[0] == num:
                self._prune(self.high)
        self._balance()

    def cost(self) -> int:
        if not self.low:
            return 0
        median = -self.low[0]
        left = median * self.sizeLow - self.sumLow
        right = self.sumHigh - median * self.sizeHigh
        return left + right

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        if x * k > n:
            return -1
        sw = SlidingWindowCost()
        costs = [0] * (n - x + 1)
        for i in range(x):
            sw.add(nums[i])
        costs[0] = sw.cost()
        for i in range(1, n - x + 1):
            sw.remove(nums[i - 1])
            sw.add(nums[i + x - 1])
            costs[i] = sw.cost()
        INF = 10**18
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            dp[i][0] = 0
            for j in range(1, k + 1):
                dp[i][j] = dp[i - 1][j]
                if i >= x:
                    cand = dp[i - x][j - 1] + costs[i - x]
                    if cand < dp[i][j]:
                        dp[i][j] = cand
        return dp[n][k]