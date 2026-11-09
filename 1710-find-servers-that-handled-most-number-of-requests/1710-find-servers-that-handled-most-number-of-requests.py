class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        n = len(arrival)
        # segment tree for free servers
        size = 1
        while size < k:
            size <<= 1
        tree = [0] * (2 * size)

        # initialize leaves: 1 means free
        for i in range(k):
            tree[size + i] = 1
        for i in range(size - 1, 0, -1):
            tree[i] = tree[i << 1] + tree[(i << 1) | 1]

        def update(pos: int, val: int):
            idx = size + pos
            tree[idx] = val
            idx >>= 1
            while idx:
                tree[idx] = tree[idx << 1] + tree[(idx << 1) | 1]
                idx >>= 1

        def query_first(l: int, r: int) -> int:
            # return first index with value 1 in [l, r], or -1
            def dfs(node, nl, nr):
                if nr < l or nl > r or tree[node] == 0:
                    return -1
                if nl == nr:
                    return nl
                mid = (nl + nr) >> 1
                left = dfs(node << 1, nl, mid)
                if left != -1:
                    return left
                return dfs((node << 1) | 1, mid + 1, nr)
            return dfs(1, 0, size - 1)

        import heapq
        busy = []  # (finish_time, server_id)
        cnt = [0] * k

        for i in range(n):
            t = arrival[i]
            # free servers whose work finished
            while busy and busy[0][0] <= t:
                ft, sid = heapq.heappop(busy)
                update(sid, 1)  # mark free
            start = i % k
            sid = query_first(start, k - 1)
            if sid == -1:
                sid = query_first(0, start - 1)
            if sid == -1:
                continue  # drop request
            # assign to sid
            cnt[sid] += 1
            update(sid, 0)  # mark busy
            heapq.heappush(busy, (t + load[i], sid))

        maxc = max(cnt)
        return [i for i, c in enumerate(cnt) if c == maxc]