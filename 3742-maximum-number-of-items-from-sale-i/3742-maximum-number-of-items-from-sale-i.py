import collections
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        N = len(items)

        # 1. Precompute F_i: number of free items obtained by purchasing item i.
        # F[i] is the count of distinct items j (where j != i) such that factor_i divides factor_j.
        # "factor_i divides factor_j" means factor_j % factor_i == 0.
        F = [0] * N
        for i in range(N):
            factor_i = items[i][0]
            for j in range(N):
                if i == j:
                    continue
                factor_j = items[j][0]
                if factor_j % factor_i == 0:
                    F[i] += 1

        # 2. Precompute dp_additional[b]: maximum additional items that can be bought with budget b.
        # This is an unbounded knapsack problem. We want to maximize the count of purchased items
        # given a budget, where each purchased item adds 1 to the total count (no free bonuses).
        # We can buy unlimited copies of any item.
        dp_additional = [0] * (budget + 1)
        for b in range(1, budget + 1):
            for k in range(N):
                price_k = items[k][1]
                if price_k <= b:
                    dp_additional[b] = max(dp_additional[b], dp_additional[b - price_k] + 1)
        
        # 3. Compute dp_activate[b]: maximum total "value" obtained by activating a subset of item types
        # with a total cost of exactly b.
        # The "value" for activating item i is (1 purchased copy for activation + F[i] free copies).
        # Each item type i can be activated at most once (by buying at least one copy of it).
        # This is a 0/1 knapsack problem.
        # Initialize with -1 to indicate unreachable budget states, except for budget 0.
        dp_activate = [-1] * (budget + 1)
        dp_activate[0] = 0 # 0 cost, 0 items activated
        
        for i in range(N):
            item_cost = items[i][1]
            item_value = 1 + F[i] 
            
            # Iterate budget downwards to ensure each item is considered once (0/1 knapsack logic).
            for b in range(budget, item_cost - 1, -1):
                if dp_activate[b - item_cost] != -1: # If the prior budget state is reachable
                    dp_activate[b] = max(dp_activate[b], dp_activate[b - item_cost] + item_value)

        # 4. Combine results: Iterate through all possible ways to split the total budget.
        # For each possible amount 'b_activated' spent on activating item types,
        # calculate the total items:
        # (items obtained from activation) + (additional items purchased with remaining budget).
        max_total_items = 0
        for b_activated in range(budget + 1):
            if dp_activate[b_activated] != -1: # Only consider reachable activation costs
                current_items_from_activation = dp_activate[b_activated]
                remaining_budget = budget - b_activated
                additional_items = dp_additional[remaining_budget]
                
                max_total_items = max(max_total_items, current_items_from_activation + additional_items)
        
        return max_total_items