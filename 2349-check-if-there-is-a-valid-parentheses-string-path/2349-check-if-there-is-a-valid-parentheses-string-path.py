class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        # DP state: dp[i][j] is a bitmask where bit b is set iff there exists a path
        # from (0,0) to (i,j) with current parentheses balance = b (open minus close).
        # Balance never exceeds path length (m+n) and never goes negative.
        m, n = len(grid), len(grid[0])
        max_len = m + n                     # upper bound on possible balance
        limit_mask = (1 << (max_len + 1)) - 1  # mask to keep bits within range

        def apply(mask: int, ch: str) -> int:
            # Update balance after visiting a cell containing ch.
            # '(' increases balance, ')' decreases it.
            if ch == '(':
                return (mask << 1) & limit_mask
            else:
                return mask >> 1

        dp = [[0] * n for _ in range(m)]
        # start with balance 0 before processing (0,0)
        dp[0][0] = apply(1, grid[0][0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                prev = 0
                if i > 0:
                    prev |= dp[i - 1][j]
                if j > 0:
                    prev |= dp[i][j - 1]
                dp[i][j] = apply(prev, grid[i][j])

        # Valid path ends with balance 0, i.e., bit 0 set.
        return (dp[m - 1][n - 1] & 1) != 0