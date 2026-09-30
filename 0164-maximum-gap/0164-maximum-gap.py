class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n = len(nums)

        if n < 2:
            return 0

        # Step 1: Find the minimum and maximum elements in the array.
        min_val = float('inf')
        max_val = float('-inf')
        for num in nums:
            min_val = min(min_val, num)
            max_val = max(max_val, num)
        
        # If all elements are the same, the maximum gap is 0.
        if min_val == max_val:
            return 0

        # Step 2: Calculate the bucket size (gap).
        # The minimum possible value for the maximum gap is ceil((max_val - min_val) / (N - 1)).
        # We use integer arithmetic for ceiling: ceil(A/B) = (A + B - 1) // B for A, B > 0.
        # Here A = (max_val - min_val), B = (n - 1).
        # Both A and B are positive because we handled min_val == max_val and n < 2.
        bucket_size = (max_val - min_val + n - 2) // (n - 1)
        
        # Determine the number of buckets required.
        # This covers the range [min_val, max_val] with buckets of size `bucket_size`.
        # min_val falls into bucket 0. max_val falls into bucket (max_val - min_val) // bucket_size.
        # The total number of buckets will be at most N, ensuring linear space.
        num_buckets = (max_val - min_val) // bucket_size + 1

        # Step 3: Initialize buckets.
        # Each bucket stores the minimum and maximum element that falls into it.
        # Initialize with sentinel values (infinity and negative infinity).
        bucket_min = [float('inf')] * num_buckets
        bucket_max = [float('-inf')] * num_buckets

        # Step 4: Distribute numbers into buckets.
        for num in nums:
            # Calculate the bucket index for the current number.
            # Numbers are offset by min_val to start indexing from 0.
            idx = (num - min_val) // bucket_size
            bucket_min[idx] = min(bucket_min[idx], num)
            bucket_max[idx] = max(bucket_max[idx], num)
        
        # Step 5: Calculate the maximum gap.
        # The maximum gap cannot be within a single bucket because any two numbers
        # x, y in the same bucket satisfy |x - y| < bucket_size.
        # Therefore, the maximum gap must occur between the maximum of one non-empty bucket
        # and the minimum of the next non-empty bucket.
        max_gap = 0
        prev_max = min_val  # Start with the overall minimum value.

        for i in range(num_buckets):
            # If the current bucket is empty (i.e., its min_val is still float('inf')), skip it.
            if bucket_min[i] == float('inf'):
                continue
            
            # The gap is calculated between the current bucket's minimum element
            # and the maximum element of the previous non-empty bucket.
            max_gap = max(max_gap, bucket_min[i] - prev_max)
            
            # Update prev_max to the maximum element found in the current non-empty bucket.
            prev_max = bucket_max[i]
            
        return max_gap