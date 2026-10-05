class Solution:
    def minFallingPathSum(self, grid):
        n = len(grid)
        if n == 1:
            return grid[0][0]
        dp = grid[0][:]
        for i in range(1, n):
            # find smallest and second smallest in dp
            min1 = min2 = float('inf')
            idx1 = -1
            for j, val in enumerate(dp):
                if val < min1:
                    min2 = min1
                    min1 = val
                    idx1 = j
                elif val < min2:
                    min2 = val
            new_dp = [0]*n
            for j in range(n):
                if j != idx1:
                    new_dp[j] = grid[i][j] + min1
                else:
                    new_dp[j] = grid[i][j] + min2
            dp = new_dp
        return min(dp)