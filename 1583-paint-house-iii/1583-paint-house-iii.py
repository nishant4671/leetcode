class Solution:
    def minCost(self, houses, cost, m, n, target):
        INF = 10**15
        dp_prev = [[INF] * (n + 1) for _ in range(target + 1)]
        if houses[0]:
            c = houses[0]
            dp_prev[1][c] = 0
        else:
            for c in range(1, n + 1):
                dp_prev[1][c] = cost[0][c - 1]
        for i in range(1, m):
            dp_cur = [[INF] * (n + 1) for _ in range(target + 1)]
            for t in range(1, min(target, i + 1) + 1):
                for c in range(1, n + 1):
                    if houses[i] and houses[i] != c:
                        continue
                    cur_cost = 0 if houses[i] else cost[i][c - 1]
                    same = dp_prev[t][c]
                    diff = INF
                    if t > 1:
                        for pc in range(1, n + 1):
                            if pc != c:
                                val = dp_prev[t - 1][pc]
                                if val < diff:
                                    diff = val
                    best = same if same < diff else diff
                    if best < INF:
                        dp_cur[t][c] = best + cur_cost
            dp_prev = dp_cur
        ans = min(dp_prev[target][1:]) 
        return -1 if ans >= INF else ans