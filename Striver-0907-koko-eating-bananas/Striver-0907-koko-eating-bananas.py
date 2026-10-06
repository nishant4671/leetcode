class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # The eating speed 'k' can range from 1 to the maximum number of bananas in any pile.
        # Minimum possible speed is 1 banana per hour.
        low = 1
        # Maximum possible speed to consider is the largest pile. If Koko eats at this speed,
        # she finishes each pile in 1 hour. Any speed greater than this would still
        # result in 1 hour per pile, so it doesn't reduce total time further.
        high = max(piles)
        
        # 'ans' will store the minimum 'k' that satisfies the condition.
        # Initialize it with a value that is guaranteed to be an upper bound (e.g., high).
        ans = high

        # Binary search for the optimal 'k'.
        while low <= high:
            mid = low + (high - low) // 2  # Calculate the middle speed.

            # Calculate the total hours required to eat all piles at speed 'mid'.
            total_hours_needed = 0
            for pile in piles:
                # The number of hours to eat a 'pile' of bananas at speed 'mid' is ceil(pile / mid).
                # In integer arithmetic, ceil(a / b) can be calculated as (a + b - 1) // b.
                total_hours_needed += (pile + mid - 1) // mid
            
            # Check if Koko can finish all bananas within 'h' hours at the current speed 'mid'.
            if total_hours_needed <= h:
                # If she can finish, 'mid' is a possible eating speed.
                # We record 'mid' as a potential answer and try to find an even smaller 'k'
                # in the lower half of the search space.
                ans = mid
                high = mid - 1
            else:
                # If she cannot finish within 'h' hours, 'mid' is too slow.
                # We need to increase the eating speed, so we search in the upper half.
                low = mid + 1
                
        return ans