class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n = len(bloomDay)

        # Edge case: If the total number of flowers required (m * k)
        # exceeds the total number of available flowers (n),
        # it's impossible to make m bouquets.
        # This check is crucial to handle cases where m or k are large.
        if m * k > n:
            return -1

        # Helper function to check if `m` bouquets can be made by a given `day`.
        # This function iterates through the `bloomDay` array and counts
        # how many bouquets can be formed with flowers bloomed by `day`.
        def can_make_bouquets(day: int) -> bool:
            bouquets_made = 0
            consecutive_bloomed_flowers = 0

            for bloom_time in bloomDay:
                if bloom_time <= day:
                    # Flower has bloomed by the given day.
                    consecutive_bloomed_flowers += 1
                    if consecutive_bloomed_flowers == k:
                        # We have found `k` adjacent bloomed flowers,
                        # so we can form one bouquet.
                        bouquets_made += 1
                        consecutive_bloomed_flowers = 0  # Reset count as these `k` flowers are used for a bouquet
                else:
                    # Flower has not bloomed by the given day,
                    # breaking the sequence of consecutive bloomed flowers.
                    consecutive_bloomed_flowers = 0
                
                # Optimization: If we have already made enough bouquets,
                # we don't need to check the rest of the flowers.
                if bouquets_made >= m:
                    return True
            
            # Return true if we managed to make at least `m` bouquets.
            return bouquets_made >= m

        # Binary search for the minimum day.
        # The search space for the number of days is from `min(bloomDay)`
        # (the earliest any flower can bloom) to `max(bloomDay)`
        # (the latest any flower can bloom, by which point all flowers have bloomed).
        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1 # Initialize answer to -1, indicating no solution found yet.

        while low <= high:
            mid = low + (high - low) // 2 # Calculate mid-point to avoid potential integer overflow for large low/high

            if can_make_bouquets(mid):
                # If we can make `m` bouquets by `mid` day, then `mid` is a possible answer.
                # We want the *minimum* such day, so we store `mid` in `ans`
                # and try to find an even smaller day by searching in the left half.
                ans = mid
                high = mid - 1
            else:
                # If we cannot make `m` bouquets by `mid` day, then `mid` is too early.
                # We need more days, so we must search in the right half.
                low = mid + 1
        
        return ans