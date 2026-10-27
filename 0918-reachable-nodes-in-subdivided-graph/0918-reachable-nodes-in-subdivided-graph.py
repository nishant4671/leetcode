class Solution:
    def reachableNodes(self, edges: list[list[int]], maxMoves: int, n: int) -> int:
        # Build adjacency list where each edge weight is cnt+1 (cost to traverse whole edge)
        import heapq
        adj = [[] for _ in range(n)]
        for u, v, cnt in edges:
            w = cnt + 1
            adj[u].append((v, w, cnt))
            adj[v].append((u, w, cnt))
        # Dijkstra from node 0
        INF = 10**18
        dist = [INF] * n
        dist[0] = 0
        heap = [(0, 0)]
        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            for v, w, _ in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))
        # Count reachable original nodes
        reachable = sum(1 for d in dist if d <= maxMoves)
        # Count reachable subdivided nodes on each edge
        for u, v, cnt in edges:
            # moves left after reaching u and v
            left_u = max(0, maxMoves - dist[u]) if dist[u] != INF else 0
            left_v = max(0, maxMoves - dist[v]) if dist[v] != INF else 0
            # total reachable on this edge is limited by cnt
            reachable += min(cnt, left_u + left_v)
        return reachable