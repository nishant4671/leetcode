class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def get_min_ops_from_current_array(arr: List[int]) -> int:
            """
            Calculates minimum additional operations to sort 'arr' if it's currently
            either a cyclic shift of [0, ..., n-1] (C1 form)
            or a cyclic shift of [0, n-1, ..., 1] (C2 form).
            Returns float('inf') if 'arr' is neither of these forms.
            
            Operations considered here: only rotations to bring '0' to the front,
            and then potentially a reverse + rotate if it's in C2 form.
            """
            current_min_ops = float('inf')

            # Find the index of 0 in the current array
            idx0 = -1
            for i in range(n):
                if arr[i] == 0:
                    idx0 = i
                    break

            # Check if 'arr' is a cyclic shift of [0, 1, ..., n-1] (C1 form)
            # This means arr is [k, k+1, ..., n-1, 0, ..., k-1] for some k.
            # To sort it, we need `idx0` left rotations to bring 0 to the first position.
            is_C1 = True
            for i in range(n):
                if arr[(idx0 + i) % n] != i:
                    is_C1 = False
                    break
            if is_C1:
                current_min_ops = min(current_min_ops, idx0)

            # Check if 'arr' is a cyclic shift of [0, n-1, n-2, ..., 1] (C2 form)
            # This means arr is [k, k-1, ..., 0, n-1, ..., k+1] for some k.
            # First, rotate `idx0` times to bring 0 to the first position.
            # Resulting array is [0, n-1, n-2, ..., 1].
            is_C2 = True
            for i in range(n):
                if arr[(idx0 + i) % n] != (n - i) % n:
                    is_C2 = False
                    break
            
            if is_C2:
                ops_from_C2 = idx0 # Rotations to bring 0 to the front
                if n > 2: # For n=1 or n=2, [0, n-1, ..., 1] is already sorted [0] or [0,1]
                    # From [0, n-1, ..., 1], 1 reverse op leads to [1, 2, ..., n-1, 0].
                    # From [1, 2, ..., n-1, 0], 1 left rotation leads to [0, 1, ..., n-1].
                    # So, for n > 2, it requires an additional 2 operations (1 reverse + 1 rotate).
                    ops_from_C2 += 2
                current_min_ops = min(current_min_ops, ops_from_C2)

            return current_min_ops

        ans = float('inf')

        # Strategy 1: Attempt to sort 'nums' without an initial reverse operation.
        # This covers cases where 'nums' is already in C1 or C2 form.
        res1 = get_min_ops_from_current_array(nums)
        if res1 != float('inf'):
            ans = min(ans, res1)

        # Strategy 2: Perform one initial reverse operation on 'nums',
        # then attempt to sort the resulting 'reversed_nums'.
        # This covers cases where 'nums' can be transformed into C1 or C2 form
        # after a single reverse operation.
        reversed_nums = nums[::-1]
        res2 = get_min_ops_from_current_array(reversed_nums)
        if res2 != float('inf'):
            # Add 1 to account for the initial reverse operation.
            ans = min(ans, 1 + res2) 

        # If 'ans' is still infinity, it means sorting is impossible.
        return ans if ans != float('inf') else -1