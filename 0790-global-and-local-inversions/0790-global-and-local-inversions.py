class Solution:
    def isIdealPermutation(self, nums: list[int]) -> bool:
        n = len(nums)
        
        # In a permutation of 0 to n-1, all local inversions are also global inversions.
        # Therefore, the number of global inversions equals the number of local inversions
        # if and only if there are no global inversions that are NOT local inversions.
        
        # A global inversion (i, j) is not local if j > i + 1.
        # This means the condition for an ideal permutation is that we must not have
        # nums[i] > nums[j] for any pair (i, j) where j > i + 1.
        
        # This condition is equivalent to stating:
        # For every k from 0 to n-3, the maximum value in the prefix nums[0...k]
        # must be less than or equal to nums[k+2].
        # That is, `max(nums[0], ..., nums[k]) <= nums[k+2]` for all `0 <= k <= n-3`.
        
        # We can verify this condition in a single pass with O(1) extra space.
        # `max_val_prefix` will keep track of `max(nums[0], ..., nums[k])` as `k` increases.
        
        # Constraints guarantee n >= 1, so nums[0] is always safe to access.
        max_val_prefix = nums[0] 
        
        # The loop iterates `k` from `0` up to `n-3` (inclusive).
        # The `range(n - 2)` function generates numbers from `0` to `n-3`.
        # For n=1 or n=2, `n-2` is 0 or -1, so `range(n-2)` will be empty, and the loop won't run.
        # In these cases, no `k` exists for which `k+2` is a valid index, so no non-local
        # inversions are possible. The function correctly returns `True`.
        for k in range(n - 2):
            # At this point, `max_val_prefix` stores `max(nums[0], ..., nums[k])`.
            # We compare this maximum with `nums[k+2]`.
            if max_val_prefix > nums[k+2]:
                return False # Found a global inversion (p, k+2) where p <= k and p < (k+2)-1
                             # This means nums[p] > nums[k+2] for p < k+1, which is a non-local inversion.
            
            # For the next iteration (`k+1`), `max_val_prefix` needs to be `max(nums[0], ..., nums[k+1])`.
            # So, we update `max_val_prefix` to include `nums[k+1]`.
            max_val_prefix = max(max_val_prefix, nums[k+1])
            
        return True