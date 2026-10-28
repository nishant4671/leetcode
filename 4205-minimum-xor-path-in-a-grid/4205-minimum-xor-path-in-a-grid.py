class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # dp[i][j] will store a set of all possible XOR sums to reach cell (i, j).
        # The maximum possible value for any grid[x][y] is 1023 (10 bits).
        # Thus, any XOR sum will also be within the range [0, 1023].
        # So, each set will contain at most 1024 distinct values.
        dp = [[set() for _ in range(n)] for _ in range(m)]

        # Base case: starting cell (0, 0)
        dp[0][0].add(grid[0][0])

        # Fill the DP table
        for i in range(m):
            for j in range(n):
                current_val = grid[i][j]

                # If not in the first row, we can reach (i, j) from (i-1, j)
                if i > 0:
                    for prev_xor_sum in dp[i-1][j]:
                        dp[i][j].add(prev_xor_sum ^ current_val)

                # If not in the first column, we can reach (i, j) from (i, j-1)
                if j > 0:
                    for prev_xor_sum in dp[i][j-1]:
                        dp[i][j].add(prev_xor_sum ^ current_val)
        
        # The result is the minimum XOR sum found in the set for the bottom-right cell (m-1, n-1)
        return min(dp[m-1][n-1])