import collections

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        # 1. Check for already sorted
        if all(nums[i] == i for i in range(n)):
            return 0

        # 2. Precompute current_pos (mapping value to its current index)
        # current_pos[val] stores the index where 'val' is currently located.
        current_pos = [0] * n
        for i in range(n):
            current_pos[nums[i]] = i

        # 3. Compute potential_k_upper_bound
        # For the array to be sortable with a given k, any value 'val' that is
        # currently misplaced (val != current_pos[val]) must be able to move.
        # This implies 'val' must be part of a k-compatible swap chain.
        # A value 'x' can participate in a swap if it's 'k'-compatible, i.e., (x AND k) == k.
        # This means 'k' must be a submask of 'x'.
        # Similarly, the index 'i' (which is the target value) must also be k-compatible if it's involved in a swap.
        # So, for every 'idx' such that nums[idx] != idx, both nums[idx] and idx must have 'k' as a submask.
        # Thus, 'k' must be a submask of (nums[idx] AND idx) for all such 'idx'.
        # Consequently, 'k' must be a submask of the bitwise AND of all such (nums[idx] AND idx) values.

        # Determine the maximum bit length needed to represent numbers up to n-1.
        # For n=1, n-1=0, (n-1).bit_length() is 0.
        # For n > 1, max_val_bit_len is at least 1.
        max_val_bit_len = (n - 1).bit_length() if n > 0 else 0
        
        # Initialize ans_k_bound with all bits set up to max_val_bit_len.
        # This means `ans_k_bound` will be like 0b111...1.
        ans_k_bound = (1 << max_val_bit_len) - 1 if max_val_bit_len > 0 else 0

        for i in range(n):
            # If the value at index 'i' is not 'i', then 'i' is misplaced.
            # Both the value nums[i] and the target value 'i' must be k-compatible.
            # This implies 'k' must be a submask of nums[i] AND k must be a submask of i.
            if nums[i] != i:
                ans_k_bound &= nums[i]
                ans_k_bound &= i
        
        # 4. Bit-by-bit construction of the maximum 'k'
        ans = 0
        
        # Iterate from the most significant bit down to 0.
        # `max_val_bit_len - 1` gives the index of the highest bit.
        # E.g., if max_val = 3 (0b011), bit_length is 2. Bits are 1 and 0. Loop range is 1 down to 0.
        # If n=1, max_val_bit_len is 0. Loop range is -1 down to 0, which means the loop doesn't run.
        # `ans` remains 0, which is correct for `n=1` (already handled by initial check, but robust).
        for b in range(max_val_bit_len - 1, -1, -1):
            candidate_k = ans | (1 << b)
            
            # Optimization: If candidate_k has any bit set that is not set in ans_k_bound,
            # then it cannot satisfy the k-compatibility condition for all misplaced elements.
            # So, it's impossible for this candidate_k to work.
            if (candidate_k & ans_k_bound) != candidate_k:
                continue
            
            # Check if this candidate_k allows sorting
            if self._check(candidate_k, nums, current_pos, n):
                ans = candidate_k
        
        return ans

    def _check(self, k: int, nums: List[int], current_pos: List[int], n: int) -> bool:
        """
        Checks if the array 'nums' can be sorted using swaps based on the given 'k'.
        A swap between indices 'i' and 'j' is allowed if nums[i] AND nums[j] == k.
        """
        dsu = DSU(n)
        
        # All values 'v' that satisfy (v AND k) == k are "k-compatible".
        # If 'k' itself is present in 'nums' (which it always is, as nums is a permutation of 0..n-1),
        # then 'k' is a k-compatible value (k AND k == k).
        # Any other k-compatible value 'v_other' can swap with 'k' if 'v_other' AND k == k.
        # This condition is already satisfied for 'v_other'.
        # Therefore, all indices whose values are k-compatible can be connected to the index where 'k' is located.
        # This efficiently groups all k-compatible indices into a single DSU component.
        
        # Get the index where the value 'k' is currently located.
        # 'k' must be a value within [0, n-1] because of the bit-by-bit construction from ans_k_bound.
        # (If k was outside this range and non-zero, it would have been filtered out by ans_k_bound logic.)
        root_of_k_compatible_group = current_pos[k] 
        
        for i in range(n):
            # If the value at index 'i' is k-compatible, union 'i' with the group's root.
            if (nums[i] & k) == k:
                dsu.union(i, root_of_k_compatible_group)
        
        # After establishing components based on k-compatibility,
        # verify if the array can be sorted.
        # This means for every value 'val' from 0 to n-1, its current position (current_pos[val])
        # must be in the same DSU component as its target position (which is 'val' itself).
        for val in range(n):
            if dsu.find(val) != dsu.find(current_pos[val]):
                return False
                
        return True