class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2   # number of elements in left half
        
        low, high = 0, m
        
        while low <= high:
            # partition index for nums1
            i = (low + high) // 2
            # partition index for nums2
            j = total_left - i
            
            # Handle edge cases where partition is at the boundary
            nums1_left_max = nums1[i-1] if i > 0 else float('-inf')
            nums1_right_min = nums1[i] if i < m else float('inf')
            nums2_left_max = nums2[j-1] if j > 0 else float('-inf')
            nums2_right_min = nums2[j] if j < n else float('inf')
            
            # Check if partition is correct
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # Valid partition
                if (m + n) % 2 == 1:
                    # Odd total length → median is max of left half
                    return max(nums1_left_max, nums2_left_max)
                else:
                    # Even total length → average of max left and min right
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0
            elif nums1_left_max > nums2_right_min:
                # too many elements from nums1 in left → move i left
                high = i - 1
            else:
                # too few elements from nums1 in left → move i right
                low = i + 1
        
        # Should never reach here for valid inputs
        raise ValueError("Input arrays are not sorted.")