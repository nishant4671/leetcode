class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        # DP state: dp[i] = max profit considering first i jobs in order of increasing end time
        # Transition: either skip i-th job (dp[i-1]) or take it (profit[i-1] + dp[p])
        # where p is the number of jobs that end <= start of i-th job (found via binary search)
        # Time complexity: O(n log n) for sorting + binary searches, n <= 5e4
        # Space complexity: O(n) for dp and sorted arrays
        jobs = sorted(zip(endTime, startTime, profit))
        ends = [e for e, _, _ in jobs]
        starts = [s for _, s, _ in jobs]
        profits = [p for _, _, p in jobs]
        import bisect
        n = len(jobs)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            s = starts[i - 1]
            p = profits[i - 1]
            idx = bisect.bisect_right(ends, s)
            dp[i] = max(dp[i - 1], p + dp[idx])
        return dp[n]