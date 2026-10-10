class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        
        def check(capacity: int) -> bool:
            """
            Helper function to determine if all packages can be shipped within 'days'
            using a ship with the given 'capacity'.
            """
            days_needed = 1  # Start counting from the first day
            current_weight_on_ship = 0  # Weight loaded on the ship for the current day

            for weight in weights:
                # If adding the current package exceeds the ship's capacity,
                # we must start a new day.
                # Since 'capacity' is guaranteed to be >= max(weights) by our binary search bounds,
                # any single package 'weight' will always fit on an empty ship.
                if current_weight_on_ship + weight > capacity:
                    days_needed += 1
                    current_weight_on_ship = weight  # This package starts the new day
                else:
                    # Otherwise, add the package to the current day's load
                    current_weight_on_ship += weight
            
            # Return True if the total days required are within the allowed 'days',
            # False otherwise.
            return days_needed <= days

        # Define the search space for the ship capacity.
        # The minimum possible capacity must be at least the weight of the heaviest single package.
        low = max(weights)
        # The maximum possible capacity is the sum of all package weights.
        # With this capacity, all packages can be shipped in a single day.
        high = sum(weights)

        # 'ans' will store the minimum valid capacity found.
        # Initialize it with 'high' because we know 'high' is a feasible capacity,
        # and we are looking for the minimum.
        ans = high 

        # Perform binary search to find the minimum feasible capacity.
        while low <= high:
            # Calculate the middle capacity to test.
            # Using low + (high - low) // 2 prevents potential integer overflow
            # compared to (low + high) // 2, though not strictly necessary for these constraints.
            mid = low + (high - low) // 2

            if check(mid):
                # If 'mid' capacity is feasible, it could be our answer.
                # We store it and try to find an even smaller capacity in the lower half.
                ans = mid
                high = mid - 1
            else:
                # If 'mid' capacity is not feasible, it means 'mid' is too small.
                # We need a larger capacity, so we adjust the search space to the upper half.
                low = mid + 1
        
        # After the loop, 'ans' will hold the smallest capacity that satisfies the condition.
        return ans