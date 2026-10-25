import math

class Solution:
    def minSkips(self, dist, speed, hoursBefore):
        n = len(dist)
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0.0
        for i in range(n):
            ndp = [INF] * (n + 1)
            for j in range(i + 1):
                cur = dp[j]
                if cur == INF:
                    continue
                t = cur + dist[i] / speed
                if i == n - 1:
                    if t < ndp[j]:
                        ndp[j] = t
                else:
                    wait = math.ceil(t - 1e-12)
                    if wait < ndp[j]:
                        ndp[j] = wait
                    if t < ndp[j + 1]:
                        ndp[j + 1] = t
            dp = ndp
        for j in range(n + 1):
            if dp[j] <= hoursBefore + 1e-12:
                return j
        return -1