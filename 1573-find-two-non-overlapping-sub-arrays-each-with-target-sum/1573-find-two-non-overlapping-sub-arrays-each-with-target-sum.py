class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        # dp[j] stores the minimum length of a subarray that sums to target,
        # considering subarrays ending at or before index j.
        dp = [float('inf')] * n 
        
        # prefix_map stores (prefix_sum: index) pairs.
        # {0: -1} indicates that a prefix sum of 0 exists before the array starts.
        prefix_map = {0: -1}
        current_sum = 0
        min_total_length = float('inf')

        for j in range(n):
            # Initially, dp[j] inherits the minimum length from dp[j-1].
            # This accounts for subarrays that end before j but within arr[0...j].
            if j > 0:
                dp[j] = dp[j-1]

            current_sum += arr[j]

            # If (current_sum - target) is in prefix_map, it means there's a subarray
            # from index (prefix_map[current_sum - target] + 1) to j that sums to target.
            if current_sum - target in prefix_map:
                i = prefix_map[current_sum - target]
                current_subarray_len = j - i

                # We found a subarray arr[i+1 ... j] with sum target and length current_subarray_len.
                # This subarray can be the 'right' one in a pair.
                # For a non-overlapping 'left' subarray, it must end at or before index i.
                # dp[i] stores the minimum length of such a subarray.
                # We check if dp[i] is a valid length (not infinity) and if i is a valid index for dp.
                if i >= 0 and dp[i] != float('inf'):
                    min_total_length = min(min_total_length, dp[i] + current_subarray_len)
                
                # Update dp[j] with the length of the current subarray ending at j.
                # This current_subarray_len is a candidate for the minimum length 
                # of any subarray ending at or before j that sums to target.
                dp[j] = min(dp[j], current_subarray_len)
            
            # Store the current prefix sum and its index j in prefix_map.
            # If a sum exists multiple times, we store the rightmost index,
            # which helps in finding the shortest subarray ending at j.
            prefix_map[current_sum] = j

        # If min_total_length is still infinity, no two such subarrays were found.
        return min_total_length if min_total_length != float('inf') else -1