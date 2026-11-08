class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        row_counts = [0] * m
        col_counts = [0] * n

        # First pass: populate row_counts and col_counts
        # For each server at (r, c), increment the count for its row and its column.
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    row_counts[r] += 1
                    col_counts[c] += 1

        # Second pass: count communicating servers
        communicating_servers = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    # A server at (r, c) communicates with another server if:
                    # 1. There is at least one other server in the same row (row_counts[r] > 1)
                    # OR
                    # 2. There is at least one other server in the same column (col_counts[c] > 1)
                    if row_counts[r] > 1 or col_counts[c] > 1:
                        communicating_servers += 1
                        
        return communicating_servers