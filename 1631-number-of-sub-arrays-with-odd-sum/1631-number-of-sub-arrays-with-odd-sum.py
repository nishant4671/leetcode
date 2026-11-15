class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        
        # `even_count` stores the number of prefix sums encountered so far that are even.
        # `odd_count` stores the number of prefix sums encountered so far that are odd.
        # We initialize `even_count` to 1 because the prefix sum of an empty array (0) is even.
        even_count = 1
        odd_count = 0
        
        # `current_prefix_sum_parity` stores the parity of the current running prefix sum.
        # 0 for even, 1 for odd. It starts at 0 for the empty prefix sum.
        current_prefix_sum_parity = 0
        
        # `total_odd_subarrays` will store the final count of subarrays with an odd sum.
        total_odd_subarrays = 0
        
        for num in arr:
            # Update the parity of the running prefix sum.
            # (A + B) % 2 is equivalent to (A % 2 + B % 2) % 2.
            # Since `current_prefix_sum_parity` is already `sum % 2`,
            # adding `num` (which is implicitly `num % 2` here) gives the new parity.
            current_prefix_sum_parity = (current_prefix_sum_parity + num) % 2
            
            if current_prefix_sum_parity == 1:  # Current prefix sum is odd
                # If the current prefix sum (P_j+1) is odd,
                # for a subarray sum (P_j+1 - P_i) to be odd,
                # P_i must be even.
                # `even_count` holds the number of previous prefix sums P_i that were even.
                total_odd_subarrays = (total_odd_subarrays + even_count) % MOD
                odd_count += 1  # Increment count for odd prefix sums, as the current one is odd.
            else:  # Current prefix sum is even
                # If the current prefix sum (P_j+1) is even,
                # for a subarray sum (P_j+1 - P_i) to be odd,
                # P_i must be odd.
                # `odd_count` holds the number of previous prefix sums P_i that were odd.
                total_odd_subarrays = (total_odd_subarrays + odd_count) % MOD
                even_count += 1 # Increment count for even prefix sums, as the current one is even.
                
        return total_odd_subarrays