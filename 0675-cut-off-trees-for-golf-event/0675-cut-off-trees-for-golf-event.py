class Solution:
    def cutOffTree(self, forest: list[list[int]]) -> int:
        # Gather all trees with height > 1 and sort them by height
        trees = [(h, i, j) for i, row in enumerate(forest) for j, h in enumerate(row) if h > 1]
        trees.sort()
        m, n = len(forest), len(forest[0])
        from collections import deque

        def bfs(sr, sc, tr, tc):
            if sr == tr and sc == tc:
                return 0
            visited = [[False] * n for _ in range(m)]
            q = deque()
            q.append((sr, sc, 0))
            visited[sr][sc] = True
            while q:
                r, c, d = q.popleft()
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and forest[nr][nc] != 0:
                        if nr == tr and nc == tc:
                            return d + 1
                        visited[nr][nc] = True
                        q.append((nr, nc, d + 1))
            return -1

        total_steps = 0
        cur_r, cur_c = 0, 0
        for _, tr, tc in trees:
            dist = bfs(cur_r, cur_c, tr, tc)
            if dist == -1:
                return -1
            total_steps += dist
            cur_r, cur_c = tr, tc
            forest[tr][tc] = 1  # cut the tree
        return total_steps