class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_num = float('inf')
        min_odd_val = float('inf')
        has_odd = False

        for x in nums1:
            min_num = min(min_num, x)
            if x % 2 == 1:
                has_odd = True
                min_odd_val = min(min_odd_val, x)
        
        # The minimum value in nums1, min_num, cannot be formed by subtracting
        # nums1[j] from itself because nums1[i] - nums1[j] >= 1 implies nums1[j] < nums1[i].
        # Thus, nums2[index_of_min_num] must be nums1[index_of_min_num], preserving its parity.
        # This means the target parity for all elements in nums2 is fixed by min_num's parity.
        target_parity = min_num % 2

        if target_parity == 1: # Target all elements in nums2 to be odd
            # This implies min_num is odd.
            # If an element nums1[i] is already odd, we set nums2[i] = nums1[i].
            # If an element nums1[i] is even, we need to flip its parity to odd.
            # We can do this by nums2[i] = nums1[i] - nums1[j] where nums1[j] is odd.
            # Since min_num is odd, it can serve as nums1[j] for any even nums1[i].
            # For any nums1[i] != min_num, nums1[i] > min_num, so nums1[i] - min_num >= 1.
            # If nums1[i] is even and min_num is odd, then (even - odd) is odd, achieving the target parity.
            # This construction is always possible when the target is odd.
            return True
        else: # target_parity == 0 (Target all elements in nums2 to be even)
            # This implies min_num is even.
            # If there are no odd numbers in nums1 (has_odd is False):
            #   All elements in nums1 are even. Since min_num is even, the target parity is even.
            #   We can simply set nums2[i] = nums1[i] for all i. All elements in nums2 will be even.
            #   This construction is possible.
            if not has_odd:
                return True
            # If there are odd numbers in nums1 (has_odd is True):
            #   All even elements in nums1 are fine; we set nums2[i] = nums1[i].
            #   All odd elements in nums1 need to have their parity flipped to even.
            #   To flip an odd number x to even using subtraction (x - y), y must be an odd number.
            #   Consider the smallest odd number in nums1, which is min_odd_val.
            #   min_odd_val itself is odd and needs to be flipped to even.
            #   To flip min_odd_val, we would need an odd nums1[j] such that nums1[j] < min_odd_val.
            #   However, min_odd_val is by definition the smallest odd number in nums1,
            #   so no such nums1[j] exists.
            #   Therefore, min_odd_val cannot be flipped to even, making it impossible to achieve
            #   an array where all elements are even.
            return False