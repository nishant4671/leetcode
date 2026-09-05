class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Calculate max_prefix array
        # max_prefix[i] stores the maximum value in nums[0...i]
        max_prefix = [0] * n
        max_prefix[0] = nums[0]
        for i in range(1, n):
            max_prefix[i] = max(max_prefix[i-1], nums[i])

        # Calculate min_suffix array
        # min_suffix[i] stores the minimum value in nums[i...n-1]
        min_suffix = [0] * n
        min_suffix[n-1] = nums[n-1]
        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(min_suffix[i+1], nums[i])

        # Iterate from left to right to find the smallest stable index
        for i in range(n):
            # Calculate the instability score for the current index i
            instability_score = max_prefix[i] - min_suffix[i]

            # Check if the current index is stable
            if instability_score <= k:
                return i  # Return the smallest stable index found

        # If no stable index is found after checking all possibilities
        return -1