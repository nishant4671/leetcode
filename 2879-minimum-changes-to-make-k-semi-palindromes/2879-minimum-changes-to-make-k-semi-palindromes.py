class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = 10**9
        # precompute divisors for each length
        divisors = [[] for _ in range(n+1)]
        for m in range(2, n+1):
            for d in range(1, int(m**0.5)+1):
                if m % d == 0:
                    if d < m:
                        divisors[m].append(d)
                    nd = m // d
                    if nd != d and nd < m:
                        divisors[m].append(nd)
        # cost[l][r]: minimal changes to make s[l:r] semi-palindrome, r exclusive
        cost = [[INF]*(n+1) for _ in range(n+1)]
        for l in range(n):
            for r in range(l+2, n+1):  # length at least 2
                m = r - l
                best = INF
                for d in divisors[m]:
                    cur = 0
                    for offset in range(d):
                        # collect positions in this group
                        positions = []
                        pos = l + offset
                        while pos < r:
                            positions.append(pos)
                            pos += d
                        sz = len(positions)
                        for i in range(sz // 2):
                            if s[positions[i]] != s[positions[sz-1-i]]:
                                cur += 1
                    if cur < best:
                        best = cur
                cost[l][r] = best
        # dp[i][j]: min cost for prefix length i using j substrings
        dp = [[INF]*(k+1) for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(n+1):
            for j in range(k):
                if dp[i][j] == INF:
                    continue
                # remaining substrings = k - j - 1, each at least length 2
                min_len = 2
                max_end = n - 2*(k - j - 1)
                for p in range(i + min_len, max_end + 1):
                    c = cost[i][p]
                    if c == INF:
                        continue
                    nd = dp[i][j] + c
                    if nd < dp[p][j+1]:
                        dp[p][j+1] = nd
        return dp[n][k] if dp[n][k] != INF else -1