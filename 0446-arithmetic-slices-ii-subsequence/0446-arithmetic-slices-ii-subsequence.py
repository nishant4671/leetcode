class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        # DP state: dp[i] is a hashmap mapping difference -> count of arithmetic subsequences
        # that end at index i and have length at least 2.
        # For each pair (j, i) with j < i, we compute diff = nums[i] - nums[j].
        # Let cnt = dp[j].get(diff, 0): number of subsequences ending at j with this diff.
        # Extending each of those by nums[i] creates cnt new subsequences of length >=3,
        # which we add to the answer.
        # Additionally, the pair (nums[j], nums[i]) forms a new subsequence of length 2,
        # so we increment dp[i][diff] by cnt + 1.
        # Time complexity: O(n^2) where n = len(nums).
        # Space complexity: O(n^2) in the worst case due to stored differences.
        from collections import defaultdict
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        total = 0
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                cnt = dp[j][diff]
                total += cnt
                dp[i][diff] += cnt + 1
        return total