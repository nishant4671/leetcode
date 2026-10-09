class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        count = n
        direction = True  # True for left-to-right, False for right-to-left

        while count > 1:
            if direction:  # Left-to-right pass
                # In a left-to-right pass, the first element is always removed.
                # So the effective 'head' of the remaining sequence shifts.
                head += step
            else:  # Right-to-left pass
                # In a right-to-left pass, the head element (smallest current value)
                # is removed only if the total count of elements is odd.
                # If count is even, the head element is not among those removed.
                if count % 2 == 1:
                    head += step
            
            # After each pass, the number of elements remaining is halved.
            count //= 2
            # The difference between consecutive remaining elements doubles.
            step *= 2
            # Alternate the direction for the next pass.
            direction = not direction
            
        return head