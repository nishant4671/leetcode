class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        # Build tree adjacency
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [0] * n
        heavy = [-1] * n

        # First DFS: compute sizes and heavy child
        stack = [(0, 0, -1)]  # node, state, parent; state 0 = pre, 1 = post
        order = []
        while stack:
            node, state, p = stack.pop()
            if state == 0:
                parent[node] = p
                size[node] = 1
                stack.append((node, 1, p))
                for nb in g[node]:
                    if nb == p: continue
                    depth[nb] = depth[node] + 1
                    stack.append((nb, 0, node))
            else:
                max_sz = 0
                for nb in g[node]:
                    if nb == p: continue
                    size[node] += size[nb]
                    if size[nb] > max_sz:
                        max_sz = size[nb]
                        heavy[node] = nb

        head = [0] * n
        pos = [0] * n
        cur = 0
        # Second DFS: decompose
        for i in range(n):
            if parent[i] == -1 or heavy[parent[i]] != i:
                # i is head of a new chain
                h = i
                while h != -1:
                    head[h] = i
                    pos[h] = cur
                    cur += 1
                    h = heavy[h]

        # Fenwick tree for xor
        bit = [0] * (n + 1)
        curMask = [0] * n
        for i in range(n):
            m = 1 << (ord(s[i]) - 97)
            curMask[i] = m
            idx = pos[i] + 1
            while idx <= n:
                bit[idx] ^= m
                idx += idx & -idx

        def bit_update(idx, val):
            while idx <= n:
                bit[idx] ^= val
                idx += idx & -idx

        def bit_query(idx):
            res = 0
            while idx:
                res ^= bit[idx]
                idx -= idx & -idx
            return res

        def range_xor(l, r):
            return bit_query(r + 1) ^ bit_query(l)

        def path_xor(u, v):
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                res ^= range_xor(pos[head[u]], pos[u])
                u = parent[head[u]]
            if depth[u] > depth[v]:
                u, v = v, u
            res ^= range_xor(pos[u], pos[v])
            return res

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                new_mask = 1 << (ord(c) - 97)
                delta = curMask[u] ^ new_mask
                if delta:
                    bit_update(pos[u] + 1, delta)
                    curMask[u] = new_mask
            else:  # query
                u = int(parts[1])
                v = int(parts[2])
                mask = path_xor(u, v)
                ans.append((mask & (mask - 1)) == 0)
        return ans