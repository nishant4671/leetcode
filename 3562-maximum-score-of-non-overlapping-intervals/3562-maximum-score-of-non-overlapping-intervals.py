import bisect
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # attach original indices
        arr = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        # sort by end coordinate
        arr.sort(key=lambda x: x[1])
        ends = [r for (_, r, _, _) in arr]
        # dp[i][c] = (weight, sorted list of indices) using first i intervals (i from 0..n)
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            l, r, w, idx = arr[i - 1]
            # inherit not taking i
            for c in range(5):
                dp[i][c] = dp[i - 1][c]
            # find previous compatible interval count
            p = bisect.bisect_left(ends, l)  # number of intervals with end < l
            for c in range(1, 5):
                prev_weight, prev_list = dp[p][c - 1]
                cand_weight = prev_weight + w
                cand_list = prev_list + [idx]
                cand_list.sort()
                cur_weight, cur_list = dp[i][c]
                if cand_weight > cur_weight or (cand_weight == cur_weight and cand_list < cur_list):
                    dp[i][c] = (cand_weight, cand_list)
        # choose best among using up to 4 intervals
        best_weight, best_list = 0, []
        for c in range(5):
            w, lst = dp[n][c]
            if w > best_weight or (w == best_weight and lst < best_list):
                best_weight, best_list = w, lst
        return best_list