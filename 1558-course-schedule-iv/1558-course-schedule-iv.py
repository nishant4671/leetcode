class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        import collections

        adj = collections.defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)

        isReachable = [[False for _ in range(numCourses)] for _ in range(numCourses)]

        for start_node in range(numCourses):
            q = collections.deque([start_node])
            visited_in_bfs = {start_node} 

            while q:
                curr = q.popleft()
                
                if curr != start_node:
                    isReachable[start_node][curr] = True
                
                for neighbor in adj[curr]:
                    if neighbor not in visited_in_bfs:
                        visited_in_bfs.add(neighbor)
                        q.append(neighbor)
        
        results = []
        for u, v in queries:
            results.append(isReachable[u][v])
        
        return results