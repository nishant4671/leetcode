class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        # right[r][c] stores the number of consecutive 1s to the right of (r, c) including (r,c)
        # down[r][c] stores the number of consecutive 1s downwards from (r, c) including (r,c)
        right = [[0] * C for _ in range(R)]
        down = [[0] * C for _ in range(R)]

        # Precompute right and down DP tables
        # Iterate from bottom-right to top-left to ensure dependencies (c+1, r+1) are met
        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                if grid[r][c] == 1:
                    right[r][c] = 1
                    if c + 1 < C:
                        right[r][c] += right[r][c+1]
                    
                    down[r][c] = 1
                    if r + 1 < R:
                        down[r][c] += down[r+1][c]

        max_side = 0

        # Iterate over all possible top-left corners (r, c)
        for r in range(R):
            for c in range(C):
                # Iterate 'k' (side length) downwards because we want the largest possible square.
                # The maximum possible 'k' for a square starting at (r,c) is limited by the remaining grid dimensions.
                # It's min(number of remaining rows, number of remaining columns).
                for k in range(min(R - r, C - c), 0, -1):
                    # Optimization: if the current 'k' is already smaller than or equal to 'max_side',
                    # any square of this size or smaller for the current (r,c) cannot be the largest.
                    # So, we can stop checking smaller 'k's for this (r,c).
                    if k <= max_side:
                        break
                    
                    # Check the four border conditions using the precomputed DP tables:
                    # A square of side 'k' with top-left corner (r,c) requires:
                    # 1. Top edge (from (r,c) to (r, c+k-1)) to have 'k' consecutive 1s: right[r][c] >= k
                    # 2. Left edge (from (r,c) to (r+k-1, c)) to have 'k' consecutive 1s: down[r][c] >= k
                    # 3. Bottom edge (from (r+k-1, c) to (r+k-1, c+k-1)) to have 'k' consecutive 1s: right[r+k-1][c] >= k
                    # 4. Right edge (from (r, c+k-1) to (r+k-1, c+k-1)) to have 'k' consecutive 1s: down[r][c+k-1] >= k
                    if (right[r][c] >= k and 
                        down[r][c] >= k and 
                        right[r+k-1][c] >= k and 
                        down[r][c+k-1] >= k):
                        
                        max_side = k
                        # Found the largest 'k' for this (r,c), no need to check smaller 'k's.
                        # Move to the next potential top-left corner (r,c).
                        break
        
        return max_side * max_side