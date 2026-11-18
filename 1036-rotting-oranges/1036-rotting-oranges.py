import collections

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        q = collections.deque()
        fresh_oranges = 0

        # Initialize queue with all initially rotten oranges and count fresh oranges
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # If there are no fresh oranges initially, no time is needed.
        # This handles cases like [[0,2]] correctly, where the output should be 0.
        if fresh_oranges == 0:
            return 0

        minutes = 0
        
        # Directions for 4-directional adjacency (right, left, down, up)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Perform BFS layer by layer
        # The loop continues as long as there are rotten oranges in the queue
        # that can potentially spread rot.
        while q: 
            # Get the number of oranges that are currently rotten and will attempt to spread rot in this minute.
            # This defines the "layer" for the current minute.
            current_level_size = len(q)
            
            # This flag tracks if any fresh orange actually became rotten during the current minute's pass.
            # `minutes` should only increment if actual rotting propagation occurred.
            rotted_in_this_minute = False 

            # Process all oranges in the current layer
            for _ in range(current_level_size):
                r, c = q.popleft()

                # Check all 4-directional neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Check if the neighbor is within grid bounds and is a fresh orange
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Mark as rotten
                        fresh_oranges -= 1
                        q.append((nr, nc)) # Add to queue for next minute's processing
                        rotted_in_this_minute = True
            
            # If any fresh oranges became rotten in this pass, it means a minute has elapsed.
            # This increment prepares `minutes` for the next round of spreading.
            # Crucially, `minutes` is NOT incremented if the current layer had no fresh neighbors to rot.
            # This prevents counting extra minutes when rot cannot spread further.
            if rotted_in_this_minute:
                minutes += 1

        # After the BFS loop finishes:
        # If `fresh_oranges` is 0, it means all fresh oranges successfully rotted.
        # Return the accumulated `minutes`.
        # Otherwise, some fresh oranges are unreachable and remain fresh.
        # In this case, return -1.
        if fresh_oranges == 0:
            return minutes
        else:
            return -1