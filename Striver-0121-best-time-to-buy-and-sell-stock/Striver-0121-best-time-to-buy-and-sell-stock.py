import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit achievable by buying and selling a stock once.

        Args:
            prices: A list of integers where prices[i] is the price of the stock
                    on the i-th day.

        Returns:
            The maximum profit that can be achieved. If no profit can be
            achieved (or profit is negative), returns 0.
        """

        # Initialize min_price_so_far to a very large number.
        # This ensures that the first stock price encountered will always become
        # the initial minimum price.
        min_price_so_far = float('inf')
        
        # Initialize max_profit to 0. We cannot achieve less than 0 profit
        # (we can choose not to make a transaction).
        max_profit = 0

        # Iterate through each price in the given list.
        for price in prices:
            # Update min_price_so_far:
            # This keeps track of the lowest price observed up to the current day.
            # This is our potential 'buy' price.
            min_price_so_far = min(min_price_so_far, price)

            # Calculate current_profit:
            # If we sell on the current day (at 'price'), the best profit is
            # achieved by buying at the lowest price seen so far (min_price_so_far).
            current_profit = price - min_price_so_far

            # Update max_profit:
            # Keep track of the highest profit found across all potential selling days.
            max_profit = max(max_profit, current_profit)
        
        # Return the overall maximum profit.
        # If no profitable transaction was possible, max_profit will remain 0.
        return max_profit