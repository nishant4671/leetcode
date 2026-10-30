class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))

        # dist_array[node][last_char_idx][consecutive_count]
        # last_char_idx: 0-25 for 'a'-'z'
        # consecutive_count: 1 to k
        
        # Max path length: n * max_weight = 5*10^4 * 10^4 = 5*10^8
        # Use a value larger than this for infinity.
        INF = float('inf') 
        
        # Initialize dist_array with INF
        # The size is n * 26 * (k+1)
        # Note: k+1 for consecutive_count as it goes from 1 to k. Index 0 is unused.
        dist_array = [[[INF] * (k + 1) for _ in range(26)] for _ in range(n)]

        pq = []

        # Starting node is 0.
        # Initial state: (distance, current_node, current_node_label_idx, consecutive_count_at_current_node)
        start_label_idx = ord(labels[0]) - ord('a')
        
        # Push initial state to priority queue
        # distance, u, u_label_idx, u_consecutive_count
        dist_array[0][start_label_idx][1] = 0
        heapq.heappush(pq, (0, 0, start_label_idx, 1))

        while pq:
            d, u, u_label_idx, u_consecutive_count = heapq.heappop(pq)

            # If we found a shorter path to this state already, skip.
            if d > dist_array[u][u_label_idx][u_consecutive_count]:
                continue

            # Explore neighbors of u
            for v, weight in adj[u]:
                v_label_idx = ord(labels[v]) - ord('a')
                
                new_consecutive_count = 1
                if v_label_idx == u_label_idx:
                    new_consecutive_count = u_consecutive_count + 1
                
                # Check the consecutive character constraint
                if new_consecutive_count > k:
                    continue # This path is invalid

                # Relax edge: if a shorter path to state (v, v_label_idx, new_consecutive_count) is found
                if d + weight < dist_array[v][v_label_idx][new_consecutive_count]:
                    dist_array[v][v_label_idx][new_consecutive_count] = d + weight
                    heapq.heappush(pq, (d + weight, v, v_label_idx, new_consecutive_count))

        # After Dijkstra's algorithm, find the minimum distance to node n-1
        # from any valid (char_idx, consecutive_count) state.
        final_min_dist = INF
        for char_idx in range(26):
            for count in range(1, k + 1): # Iterate from 1 to k
                final_min_dist = min(final_min_dist, dist_array[n - 1][char_idx][count])
        
        if final_min_dist == INF:
            return -1
        return final_min_dist