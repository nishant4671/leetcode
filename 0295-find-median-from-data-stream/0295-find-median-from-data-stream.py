class MedianFinder:
    def __init__(self):
        import heapq
        self.lo = []  # max-heap (store negatives)
        self.hi = []  # min-heap

    def addNum(self, num: int) -> None:
        import heapq
        if not self.lo or num <= -self.lo[0]:
            heapq.heappush(self.lo, -num)
        else:
            heapq.heappush(self.hi, num)
        # rebalance
        if len(self.lo) > len(self.hi) + 1:
            heapq.heappush(self.hi, -heapq.heappop(self.lo))
        elif len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return float(-self.lo[0])
        else:
            return (-self.lo[0] + self.hi[0]) / 2.0