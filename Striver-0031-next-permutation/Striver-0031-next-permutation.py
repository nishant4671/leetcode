from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # Step 1: Find the first decreasing element from the right.
        # This element is at index `i`.
        # We start from the second-to-last element (n-2) and go left.
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # If `i` is -1, it means the entire array is in descending order
        # (e.g., [3,2,1]). In this case, no lexicographically greater
        # permutation is possible. We must rearrange it as the lowest
        # possible order (ascending order). This is achieved by reversing
        # the entire array.
        if i == -1:
            self._reverse(nums, 0, n - 1)
            return

        # Step 2: If a pivot `i` was found, we need to find an element
        # in the suffix nums[i+1:] to swap with nums[i].
        # This element, nums[j], should be the smallest element in the
        # suffix that is greater than nums[i].
        # Since the suffix nums[i+1:] is in descending order, we can find
        # nums[j] by iterating from the right (n-1) towards i+1 and
        # finding the first element nums[j] that is greater than nums[i].
        j = n - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        
        # Step 3: Swap nums[i] and nums[j].
        # This forms a larger permutation.
        nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the suffix starting from i+1 to the end.
        # After swapping nums[i] and nums[j], the suffix nums[i+1:]
        # needs to be sorted in ascending order to create the lexicographically
        # smallest possible suffix. Since this suffix was previously in
        # descending order (due to how `i` was found), reversing it
        # will sort it in ascending order.
        self._reverse(nums, i + 1, n - 1)

    def _reverse(self, nums: List[int], start: int, end: int) -> None:
        """
        Reverses the subarray nums[start:end+1] in-place using two pointers.
        Achieves O(1) extra space complexity.
        """
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1