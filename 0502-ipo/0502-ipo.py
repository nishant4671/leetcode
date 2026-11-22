class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        projects = list(zip(capital, profits))
        projects.sort()
        import heapq
        max_heap = []
        idx = 0
        n = len(projects)
        for _ in range(k):
            while idx < n and projects[idx][0] <= w:
                heapq.heappush(max_heap, -projects[idx][1])
                idx += 1
            if not max_heap:
                break
            w += -heapq.heappop(max_heap)
        return w