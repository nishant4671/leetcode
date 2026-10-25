import sys

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # Increase recursion limit for DFS, as a path could be R*C long.
        # Max R*C is 100*100 = 10000. Default recursion limit is often 1000 or 3000.
        sys.setrecursionlimit(rows * cols + 100)

        def dfs_mark_water(r, c):
            # Base cases for DFS:
            # 1. Out of bounds
            # 2. Already water (1)
            # If any of these conditions are met, we stop exploring this path.
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
                return
            
            # Mark the current land cell as water (1) to indicate it's visited
            # or part of an "open" island that should be ignored.
            grid[r][c] = 1
            
            # Recursively visit all 4-directionally adjacent cells.
            dfs_mark_water(r + 1, c)
            dfs_mark_water(r - 1, c)
            dfs_mark_water(r, c + 1)
            dfs_mark_water(r, c - 1)

        # Step 1: "Drown" all land cells (0s) that are connected to the grid boundary.
        # These cells and any land connected to them cannot be part of a closed island.

        # Iterate through the first and last rows
        for j in range(cols):
            # Check top row
            if grid[0][j] == 0:
                dfs_mark_water(0, j)
            # Check bottom row
            if grid[rows - 1][j] == 0:
                dfs_mark_water(rows - 1, j)
        
        # Iterate through the first and last columns (excluding corners already handled by row checks)
        for i in range(1, rows - 1):
            # Check left column
            if grid[i][0] == 0:
                dfs_mark_water(i, 0)
            # Check right column
            if grid[i][cols - 1] == 0:
                dfs_mark_water(i, cols - 1)

        # Step 2: After marking boundary-connected islands as water, count the remaining islands.
        # Any '0' found now must be part of a closed island.
        closed_islands_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    # Found a new land cell (0) that is not connected to the boundary.
                    # This signifies the start of a closed island.
                    closed_islands_count += 1
                    # "Drown" this entire closed island to mark its cells as visited (water)
                    # so we don't count its parts again.
                    dfs_mark_water(i, j)
        
        return closed_islands_count