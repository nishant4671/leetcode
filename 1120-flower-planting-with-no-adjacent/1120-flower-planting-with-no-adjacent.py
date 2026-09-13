class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in paths:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)

        result = [0] * n

        for i in range(n):
            forbidden_colors = set()
            
            for neighbor in adj[i]:
                if result[neighbor] != 0:
                    forbidden_colors.add(result[neighbor])
            
            for flower_type in range(1, 5):
                if flower_type not in forbidden_colors:
                    result[i] = flower_type
                    break

        return result