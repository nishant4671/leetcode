class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # The problem states that in one move, we can increment n - 1 elements by 1.
        # Let 'n' be the number of elements in the array.
        #
        # Consider the effect of one move:
        # If we increment n-1 elements by 1, it's equivalent to:
        # 1. Incrementing ALL n elements by 1.
        # 2. Then, decrementing ONE element (the one that was not originally incremented) by 1.
        #
        # Let 'm' be the total number of moves.
        # After 'm' moves:
        # 1. Every element `nums[i]` will have been virtually incremented by `m` due to the "increment all n elements" part of each move.
        #    So, `nums[i]` becomes `nums[i] + m`.
        # 2. A total of `m` "decrements" would have been distributed among the elements. Let `d_i` be the number of times `nums[i]` was chosen to be "decremented".
        #    The sum of these decrements must be `m`: `sum(d_i for all i) = m`.
        #
        # So, the final value of `nums[i]` after `m` moves will be `nums[i] + m - d_i`.
        # Since all elements must become equal to some value `k`, we have:
        # `k = nums[i] + m - d_i` for every `i`.
        # This implies `d_i = nums[i] + m - k`.
        #
        # Substitute `d_i` back into the sum:
        # `sum(nums[i] + m - k for all i) = m`
        # `sum(nums[i]) + n*m - n*k = m`
        # Let `S = sum(nums)`.
        # `S + n*m - n*k = m`
        # `S + (n-1)m = n*k`  (Equation 1)
        #
        # Now, we need to determine the value of `k`.
        # To minimize the number of moves `m`, we should aim for the smallest possible final value `k`.
        # Let `min_val = min(nums)` be the initial minimum element in the array.
        # The element `min_val` must also eventually become `k`.
        # From `k = nums[i] + m - d_i`, for `min_val`, we have `k = min_val + m - d_{min_idx}` (where `min_idx` is the index of `min_val`).
        # To minimize `k` (and thus `m`), we want `d_{min_idx}` to be as large as possible.
        # However, the goal is to make all elements equal, and we are only allowed to increment.
        # The "decrement one element" interpretation is a mathematical equivalence to simplify the problem, not an actual operation.
        #
        # In the context of actual increments, the minimum element `min_val` must be incremented until it reaches `k`.
        # To minimize moves, we want `min_val` to never be the single element that is NOT incremented in a move.
        # If `min_val` is always incremented (i.e., it's part of the `n-1` elements chosen in every move), then its value will increase by 1 in each move.
        # After `m` moves, its value will be `min_val + m`.
        # Since all elements must become equal to `k`, the final value `k` must be at least `min_val + m`.
        # The smallest possible `k` is achieved when `min_val` is always incremented, meaning `k = min_val + m`.
        # This is achievable by always choosing to increment `n-1` elements such that the current minimum is among them, and the current maximum is the one not incremented (unless min=max). This effectively reduces the spread `max-min` while increasing the minimum.
        #
        # Substitute `k = min_val + m` into Equation 1:
        # `S + (n-1)m = n * (min_val + m)`
        # `S + nm - m = n*min_val + nm`
        # `S - m = n*min_val`
        # `m = S - n*min_val`
        #
        # This formula calculates the minimum number of moves.

        n = len(nums)
        
        # Calculate the sum of all elements
        total_sum = sum(nums)
        
        # Find the minimum element
        min_val = min(nums)
        
        # Apply the derived formula
        return total_sum - n * min_val