class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        # Sort a copy to know the target order
        sorted_arr = sorted(arr)
        # Dictionary to store frequency differences between original prefix and sorted prefix
        diff = {}
        # Counter of keys with non‑zero difference
        nonzero = 0
        chunks = 0
        for a, b in zip(arr, sorted_arr):
            # Increment count for element from original array
            cnt_a = diff.get(a, 0) + 1
            if cnt_a == 0:
                nonzero -= 1
            elif cnt_a == 1:
                nonzero += 1
            diff[a] = cnt_a
            # Decrement count for element from sorted array
            cnt_b = diff.get(b, 0) - 1
            if cnt_b == 0:
                nonzero -= 1
            elif cnt_b == -1:
                nonzero += 1
            diff[b] = cnt_b
            # If all differences are zero, we can cut here
            if nonzero == 0:
                chunks += 1
        return chunks