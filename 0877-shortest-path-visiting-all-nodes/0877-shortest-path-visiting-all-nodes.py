class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        
        if n == 1:
            return 0
        
        target_mask = (1 << n) - 1
        
        # Queue for BFS: (current_node, mask_of_visited_nodes, current_path_length)
        queue = collections.deque()
        
        # Set to store visited states: (node, mask)
        visited = set()
        
        # Initialize BFS: start from every possible node
        for i in range(n):
            initial_mask = (1 << i)
            queue.append((i, initial_mask, 0))
            visited.add((i, initial_mask))
            
        while queue:
            u, mask, dist = queue.popleft()
            
            # If current mask equals target_mask, we've visited all nodes.
            # Since it's BFS, this is the shortest path.
            if mask == target_mask:
                return dist
            
            # Explore neighbors of current node u
            for v in graph[u]:
                # Calculate new mask by including node v
                new_mask = mask | (1 << v)
                
                # If this (node, new_mask) state has not been visited yet
                if (v, new_mask) not in visited:
                    visited.add((v, new_mask))
                    queue.append((v, new_mask, dist + 1))