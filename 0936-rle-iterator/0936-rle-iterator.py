class RLEIterator:

    def __init__(self, encoding: list[int]):
        self.encoding = encoding
        self.ptr = 0  # Pointer to the current count in the encoding array

    def next(self, n: int) -> int:
        last_val = -1  # Default return value if no elements are exhausted

        # Continue exhausting elements until n becomes 0 or we run out of encoded pairs
        while n > 0:
            # Check if we have exhausted all pairs in the encoding array
            if self.ptr >= len(self.encoding):
                return -1  # No more elements left to exhaust

            current_count = self.encoding[self.ptr]
            current_value = self.encoding[self.ptr + 1]

            if current_count == 0:
                # This pair is already exhausted, move to the next pair
                self.ptr += 2
                continue  # Try again with the next pair and the same remaining 'n'

            if n >= current_count:
                # We need to exhaust 'n' elements, and the current pair has 'current_count' elements.
                # Since n >= current_count, we exhaust all elements from the current pair.
                n -= current_count
                self.ptr += 2  # Move to the next pair as this one is fully exhausted
                last_val = current_value  # This could be the last element exhausted if n becomes 0 after this
            else:  # n < current_count
                # We need to exhaust 'n' elements, and the current pair has more than 'n' elements.
                # Exhaust 'n' elements from the current pair.
                self.encoding[self.ptr] -= n  # Update the count for the current pair
                last_val = current_value  # This is the last element exhausted
                n = 0  # All 'n' elements have been exhausted

        return last_val


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)