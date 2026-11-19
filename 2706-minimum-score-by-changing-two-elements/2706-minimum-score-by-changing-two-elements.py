from typing import List

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Sort the array to easily access smallest and largest elements.
        # This takes O(N log N) time.
        nums.sort()
        
        # The problem asks to minimize (high_score + low_score) after changing at most two elements.
        #
        # Insight 1: We can always make the low_score 0.
        # To do this, we simply pick any existing element, say `nums[k]`, and change two other elements
        # (e.g., `nums[i]` and `nums[j]`) to `nums[k]`. After this change, the array will contain
        # `nums[k]` at least twice, making the minimum absolute difference (low_score) equal to 0.
        #
        # Insight 2: If low_score is 0, the total score simplifies to just high_score.
        # The high_score is the maximum absolute difference between any two elements. In a sorted array,
        # this is `max(new_nums) - min(new_nums)`.
        #
        # So, the problem reduces to minimizing `max(new_nums) - min(new_nums)` by changing two elements.
        # To minimize the range `(max - min)`, we should try to reduce either the max, the min, or both.
        # The most effective ways to reduce the range by changing two elements are:
        #
        # Case 1: Change the two smallest elements.
        # We effectively "remove" `nums[0]` and `nums[1]`. The new minimum becomes `nums[2]`,
        # and the maximum remains `nums[n-1]`.
        # The range is `nums[n-1] - nums[2]`.
        # (For example, change `nums[0]` and `nums[1]` to `nums[2]` to ensure `low_score=0` and this range).
        score_by_removing_two_smallest = nums[n-1] - nums[2]
        
        # Case 2: Change the two largest elements.
        # We effectively "remove" `nums[n-1]` and `nums[n-2]`. The new maximum becomes `nums[n-3]`,
        # and the minimum remains `nums[0]`.
        # The range is `nums[n-3] - nums[0]`.
        # (For example, change `nums[n-1]` and `nums[n-2]` to `nums[n-3]` to ensure `low_score=0` and this range).
        score_by_removing_two_largest = nums[n-3] - nums[0]
        
        # Case 3: Change the smallest and the largest element.
        # We effectively "remove" `nums[0]` and `nums[n-1]`. The new minimum becomes `nums[1]`,
        # and the new maximum becomes `nums[n-2]`.
        # The range is `nums[n-2] - nums[1]`.
        # (For example, change `nums[0]` to `nums[1]` and `nums[n-1]` to `nums[1]` to ensure `low_score=0` and this range).
        score_by_removing_one_smallest_one_largest = nums[n-2] - nums[1]
        
        # Since n >= 3, all indices (0, 1, 2, n-3, n-2, n-1) are valid.
        # The minimum of these three possibilities is the overall minimum score.
        return min(score_by_removing_two_smallest, 
                   score_by_removing_two_largest, 
                   score_by_removing_one_smallest_one_largest)