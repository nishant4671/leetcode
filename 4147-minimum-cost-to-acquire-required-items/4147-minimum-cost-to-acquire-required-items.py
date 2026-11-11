class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        
        # Helper function to calculate the total cost for a given number of type 3 items (z_items).
        # Type 3 items contribute to both type 1 and type 2 requirements.
        def calculate_total_cost(z_items: int) -> int:
            current_cost = z_items * costBoth
            
            # Calculate remaining requirements for type 1 after using z_items.
            # If need1 - z_items is negative, it means type 1 requirement is already met or exceeded.
            remaining_need1 = max(0, need1 - z_items)
            
            # Calculate remaining requirements for type 2 after using z_items.
            # Similarly, if need2 - z_items is negative, requirement is met or exceeded.
            remaining_need2 = max(0, need2 - z_items)
            
            # Add cost for type 1 items to fulfill the remaining type 1 requirement.
            current_cost += remaining_need1 * cost1
            
            # Add cost for type 2 items to fulfill the remaining type 2 requirement.
            current_cost += remaining_need2 * cost2
            
            return current_cost

        # The cost function `calculate_total_cost(z_items)` is a sum of convex functions,
        # and therefore, it is convex itself. For a convex function, we can use ternary search
        # to find its global minimum.
        
        low = 0
        # The maximum relevant number of type 3 items to consider is `max(need1, need2)`.
        # If we buy more than `max(need1, need2)` type 3 items, both `need1` and `need2`
        # would already be satisfied (i.e., `max(0, need1 - z_items)` and `max(0, need2 - z_items)`
        # would both be 0). Any additional type 3 items would only increase the cost without
        # providing further utility, making it suboptimal.
        high = max(need1, need2)

        # Handle the edge case where no items are needed (need1 = 0, need2 = 0).
        # In this scenario, `high` will be 0. The ternary search loop condition
        # `high - low >= 3` will be false, and the final range loop will correctly
        # evaluate `calculate_total_cost(0)`, returning 0.
        if high == 0:
            return 0 

        # Ternary search loop to narrow down the range [low, high] where the minimum might exist.
        # We continue as long as the range has at least 3 elements.
        while high - low >= 3:
            # `mid1` and `mid2` divide the current search space into three parts.
            mid1 = low + (high - low) // 3
            mid2 = high - (high - low) // 3
            
            # Calculate the costs for `mid1` and `mid2`.
            cost_mid1 = calculate_total_cost(mid1)
            cost_mid2 = calculate_total_cost(mid2)
            
            # If the cost at `mid1` is less than `mid2`, the minimum is likely in the left two-thirds,
            # so we can discard the rightmost third by updating `high`.
            if cost_mid1 < cost_mid2:
                high = mid2 - 1 
            # Otherwise, the minimum is likely in the right two-thirds (or `mid2` itself if flat),
            # so we discard the leftmost third by updating `low`.
            else:
                low = mid1 + 1

        # After the loop, the search space `[low, high]` will contain at most 3 integer values.
        # We perform a brute-force check on these remaining values to find the true minimum.
        min_total_cost = float('inf')
        for z_val in range(low, high + 1):
            min_total_cost = min(min_total_cost, calculate_total_cost(z_val))
            
        return int(min_total_cost) # Return as integer, Python's int handles arbitrary size.