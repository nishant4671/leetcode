import collections
from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        
        island_count = 0
        
        # Directions for 4-directional connectivity: (dr, dc)
        # (0, 1) -> right
        # (0, -1) -> left
        # (1, 0) -> down
        # (-1, 0) -> up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Iterate through each cell in the grid
        for r in range(m):
            for c in range(n):
                # If the current cell is land (positive value) and hasn't been visited
                # (visited land cells are marked as 0)
                if grid[r][c] > 0:
                    # Start a new Breadth-First Search (BFS) for this island
                    current_island_sum = 0
                    q = collections.deque()
                    
                    # Add the starting land cell to the queue
                    q.append((r, c))
                    
                    # Add its value to the island sum and mark it as visited by setting to 0.
                    # This ensures its value is counted and it's not revisited.
                    current_island_sum += grid[r][c]
                    grid[r][c] = 0 
                    
                    # Process the queue
                    while q:
                        curr_r, curr_c = q.popleft()
                        
                        # Explore 4-directional neighbors
                        for dr, dc in directions:
                            nr, nc = curr_r + dr, curr_c + dc
                            
                            # Check if the neighbor is within grid boundaries
                            # and if it is unvisited land (positive value)
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                # Add the neighbor's value to the island sum
                                current_island_sum += grid[nr][nc]
                                # Mark the neighbor as visited
                                grid[nr][nc] = 0
                                # Add the neighbor to the queue for further exploration
                                q.append((nr, nc))
                    
                    # After the BFS for this island completes, check if its total value
                    # is divisible by k
                    if current_island_sum % k == 0:
                        island_count += 1
                        
        return island_count