class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)

        # dp[i] represents the minimum cost to reach the top of the staircase
        # starting from step i (after paying cost[i]).
        # The 'top' is considered to be index n.
        # We need two base cases:
        # dp[n] = 0 (cost to reach top from top is 0)
        # dp[n+1] = 0 (cost to reach top from beyond top is 0, for calculation of dp[n-1])

        # prev2 stores dp[i+2]
        # prev1 stores dp[i+1]
        prev2 = 0  # Corresponds to dp[n+1]
        prev1 = 0  # Corresponds to dp[n]

        # Iterate backwards from the last actual step (n-1) down to the first step (0).
        for i in range(n - 1, -1, -1):
            # The minimum cost from step i to the top is cost[i] plus the minimum
            # of the costs from step i+1 or step i+2.
            current_cost = cost[i] + min(prev1, prev2)

            # Update prev2 and prev1 for the next iteration (i-1)
            prev2 = prev1
            prev1 = current_cost

        # After the loop, prev1 holds dp[0] and prev2 holds dp[1].
        # We can start from step 0 or step 1.
        # The minimum of these two starting costs is the answer.
        return min(prev1, prev2)