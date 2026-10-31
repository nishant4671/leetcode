class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7

        dp = [[0] * n for _ in range(m)]
        memo_reflect = {}

        def get_reflection_dest(r, c, dir_attempt):
            # dir_attempt: 0 for attempting to move right, 1 for attempting to move down
            # Returns (final_r, final_c) where path lands after reflections,
            # or out-of-bounds coordinates if it leaves the grid.
            if (r, c, dir_attempt) in memo_reflect:
                return memo_reflect[(r, c, dir_attempt)]

            curr_r, curr_c, curr_dir = r, c, dir_attempt
            while True:
                # Check bounds
                if not (0 <= curr_r < m and 0 <= curr_c < n):
                    # Out of bounds. Path is invalid from this point.
                    # Return the out-of-bounds coordinates; caller must check them.
                    memo_reflect[(r, c, dir_attempt)] = (curr_r, curr_c)
                    return curr_r, curr_c

                # Check cell type
                if grid[curr_r][curr_c] == 0:
                    # Empty cell, path successfully enters.
                    memo_reflect[(r, c, dir_attempt)] = (curr_r, curr_c)
                    return curr_r, curr_c
                
                # Mirror cell (grid[curr_r][curr_c] == 1), reflect
                if curr_dir == 0: # Attempted right (to curr_r, curr_c), reflect down
                    curr_r += 1
                    curr_dir = 1
                else: # Attempted down (to curr_r, curr_c), reflect right
                    curr_c += 1
                    curr_dir = 0

        # Base case: One way to start at (0,0)
        dp[0][0] = 1

        # Iterate through the grid cells in standard DP order (top-left to bottom-right)
        for i in range(m):
            for j in range(n):
                # If no paths reached this cell, skip propagation from it.
                if dp[i][j] == 0:
                    continue

                # Paths reaching the target (m-1, n-1) terminate there.
                # Do not propagate further from the target cell.
                if i == m - 1 and j == n - 1:
                    continue

                # Propagate paths trying to move right from (i, j)
                # The intended next cell is (i, j+1), and the robot attempts to move right (dir_attempt=0).
                # get_reflection_dest determines the final landing cell after any reflections.
                final_r_right, final_c_right = get_reflection_dest(i, j + 1, 0)
                
                # If the final destination is within grid boundaries, add the paths.
                if 0 <= final_r_right < m and 0 <= final_c_right < n:
                    dp[final_r_right][final_c_right] = (dp[final_r_right][final_c_right] + dp[i][j]) % MOD

                # Propagate paths trying to move down from (i, j)
                # The intended next cell is (i+1, j), and the robot attempts to move down (dir_attempt=1).
                final_r_down, final_c_down = get_reflection_dest(i + 1, j, 1)
                
                # If the final destination is within grid boundaries, add the paths.
                if 0 <= final_r_down < m and 0 <= final_c_down < n:
                    dp[final_r_down][final_c_down] = (dp[final_r_down][final_c_down] + dp[i][j]) % MOD

        # The result is the total number of paths that successfully reach the bottom-right corner.
        return dp[m-1][n-1]