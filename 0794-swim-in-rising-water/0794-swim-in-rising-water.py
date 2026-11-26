class Solution:
    def swimInWater(self, grid):
        import heapq
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]
        visited[0][0] = True
        while heap:
            t, x, y = heapq.heappop(heap)
            if x == n-1 and y == n-1:
                return t
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(heap, (max(t, grid[nx][ny]), nx, ny))