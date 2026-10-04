class Solution:
    def numberWays(self, hats: list[list[int]]) -> int:
        MOD = 10**9 + 7
        n = len(hats)
        # DP state: dp[mask] = number of ways to assign hats to the subset of people represented by mask
        # mask bits set => those people have already received a hat
        # We iterate hats 1..40 and update dp using previous values (no reuse of same hat)
        # Time complexity: O(40 * 2^n * n) where n <= 10
        # Space complexity: O(2^n)
        hat_to_people = [[] for _ in range(41)]
        for i, pref in enumerate(hats):
            for h in pref:
                hat_to_people[h].append(i)
        full_mask = (1 << n) - 1
        dp = [0] * (1 << n)
        dp[0] = 1
        for h in range(1, 41):
            newdp = dp[:]  # start with ways that do not use current hat
            for mask in range(1 << n):
                if dp[mask] == 0:
                    continue
                for p in hat_to_people[h]:
                    if not (mask >> p) & 1:
                        new_mask = mask | (1 << p)
                        newdp[new_mask] = (newdp[new_mask] + dp[mask]) % MOD
            dp = newdp
        return dp[full_mask]