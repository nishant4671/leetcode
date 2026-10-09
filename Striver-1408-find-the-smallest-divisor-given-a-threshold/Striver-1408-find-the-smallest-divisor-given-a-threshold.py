class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        # Helper function to calculate the sum of divisions for a given divisor.
        # Each division result is rounded up (ceiling division).
        def calculate_sum(divisor: int) -> int:
            current_sum = 0
            for num in nums:
                # Ceiling division for positive integers: (a + b - 1) // b
                current_sum += (num + divisor - 1) // divisor
            return current_sum

        # The search space for the divisor 'd' ranges from 1 to max(nums).
        # A divisor of 1 gives the largest possible sum (sum of all nums).
        # A divisor of max(nums) (or anything larger) will result in each num/divisor
        # being rounded up to 1, yielding a sum of len(nums).
        # Since nums[i] >= 1 and len(nums) <= threshold, max(nums) is a valid
        # upper bound that guarantees an answer.
        left = 1
        right = max(nums)
        
        # 'ans' will store the smallest divisor found that satisfies the condition.
        # Initialize it to 'right' as 'right' is a guaranteed valid divisor.
        ans = right 

        while left <= right:
            mid = left + (right - left) // 2
            
            # Check if 'mid' as a divisor satisfies the threshold condition
            if calculate_sum(mid) <= threshold:
                # If the sum is less than or equal to threshold, 'mid' is a potential answer.
                # We want the *smallest* such divisor, so we record 'mid' and
                # try to find an even smaller one in the left half.
                ans = mid
                right = mid - 1
            else:
                # If the sum is greater than threshold, 'mid' is too small.
                # We need a larger divisor, so search in the right half.
                left = mid + 1
                
        return ans