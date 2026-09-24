class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Initialize pointers for nums1, nums2, and the write position in nums1.
        # p1 points to the last actual element in nums1 (index m-1).
        p1 = m - 1
        # p2 points to the last element in nums2 (index n-1).
        p2 = n - 1
        # p_write points to the last available position in nums1 (index m+n-1).
        p_write = m + n - 1
        
        # Iterate while there are still elements to consider in nums2.
        # If p1 becomes negative, it means all elements from the original nums1
        # have already been placed in their final sorted positions.
        # Any remaining elements in nums2 are smaller and should be copied directly
        # to the beginning of nums1.
        while p2 >= 0:
            # Check if there are still elements in the original nums1 portion (p1 >= 0)
            # AND if the current element in nums1 is greater than the current element in nums2.
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                # If nums1[p1] is the larger element, place it at the current write position.
                nums1[p_write] = nums1[p1]
                # Move p1 to the left to consider the next smaller element from nums1.
                p1 -= 1
            else:
                # If nums2[p2] is the larger element (or equal),
                # OR if p1 has already exhausted all its elements (p1 < 0),
                # then place nums2[p2] at the current write position.
                nums1[p_write] = nums2[p2]
                # Move p2 to the left to consider the next smaller element from nums2.
                p2 -= 1
            
            # Move p_write to the left to fill the next position.
            p_write -= 1