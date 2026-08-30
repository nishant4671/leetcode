import collections
from typing import List

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Max value for nums[i] is < 2^10, so XOR sum will be < 2^10.
        MAX_XOR_VAL = 1 << 10 # 1024

        # group_data[j] will store a list [count_j, freq_map_j]
        # count_j is the total number of elements in group G_j
        # freq_map_j is a Counter for elements in group G_j
        group_data = []
        for _ in range(k):
            group_data.append([0, collections.defaultdict(int)])

        for i in range(n):
            group_idx = i % k
            group_data[group_idx][0] += 1
            group_data[group_idx][1][nums[i]] += 1

        # dp_current[x] stores the minimum changes for groups G_0 to G_j
        # such that their XOR sum is x.
        # Initialize dp_current for the first group G_0.
        dp_current = [float('inf')] * MAX_XOR_VAL
        
        count_0, freq_map_0 = group_data[0]
        for v in range(MAX_XOR_VAL):
            dp_current[v] = count_0 - freq_map_0.get(v, 0)
            
        # Iterate for groups G_1 to G_{k-1}
        for j in range(1, k):
            dp_next = [float('inf')] * MAX_XOR_VAL
            count_j, freq_map_j = group_data[j]
            
            # Find the minimum changes possible from previous groups
            # This is used for the "fallback" option where we change all elements in G_j
            # to a value not present in freq_map_j (or to any value costing count_j changes).
            min_prev_val = min(dp_current)

            # Option 1: Set x_j to any value, incurring `count_j` changes for G_j.
            # This means we can achieve `min_prev_val` from previous groups.
            # To get an overall XOR sum `x` (for `dp_next[x]`), we need `prev_xor ^ x_j = x`.
            # If we choose `x_j` such that `dp_current[prev_xor]` is `min_prev_val`,
            # then `dp_next[x]` can be `min_prev_val + count_j`. This serves as a general upper bound
            # (lower actual cost) for all `x` if `x_j` is chosen from outside `freq_map_j`.
            for x in range(MAX_XOR_VAL):
                dp_next[x] = min_prev_val + count_j

            # Option 2: Set x_j to a value 'val' that is present in G_j.
            # This incurs `count_j - freq` changes for G_j.
            for val, freq in freq_map_j.items():
                cost_v = count_j - freq
                for prev_xor in range(MAX_XOR_VAL):
                    # If `dp_current[prev_xor]` is the minimum changes for first `j-1` groups to XOR to `prev_xor`,
                    # and we set `x_j = val` (cost `cost_v`),
                    # then the total XOR sum for `j` groups is `prev_xor ^ val`.
                    # The total changes is `dp_current[prev_xor] + cost_v`.
                    dp_next[prev_xor ^ val] = min(dp_next[prev_xor ^ val], dp_current[prev_xor] + cost_v)
            
            dp_current = dp_next

        # The final answer is the minimum changes to make the XOR sum of all groups zero.
        return dp_current[0]