from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] will store the minimum number of coins needed to make amount i.
        # Initialize dp array with amount + 1. This value acts as "infinity"
        # because the maximum number of coins needed for any amount 'A' is 'A' itself
        # (e.g., using only 1-unit coins). So, A + 1 is an impossible count,
        # indicating that the amount 'i' cannot be formed.
        dp = [amount + 1] * (amount + 1)

        # Base case: 0 coins are needed to make an amount of 0.
        dp[0] = 0

        # Iterate through each amount from 1 up to the target amount.
        for i in range(1, amount + 1):
            # For each amount 'i', iterate through all available coin denominations.
            for coin in coins:
                # If the current coin's value is less than or equal to the current amount 'i',
                # it means we can potentially use this coin to form 'i'.
                if i - coin >= 0:
                    # We want to find the minimum number of coins for amount 'i'.
                    # This can be either the current best way to make 'i' (dp[i])
                    # or using one 'coin' plus the minimum number of coins needed
                    # for the remaining amount (i - coin).
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # After filling the dp table, dp[amount] will hold the minimum number of coins
        # required for the target 'amount'.
        # If dp[amount] is still 'amount + 1', it means the target amount cannot be formed
        # by any combination of the given coins. In this case, return -1.
        # Otherwise, return dp[amount].
        return dp[amount] if dp[amount] != amount + 1 else -1