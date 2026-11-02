class Solution:
    def maxSum(self, nums1: list[int], nums2: list[int]) -> int:
        MOD = 10**9 + 7
        i = j = 0
        sum1 = sum2 = 0
        n1, n2 = len(nums1), len(nums2)
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                common = nums1[i]
                max_sum = max(sum1, sum2) + common
                sum1 = sum2 = max_sum
                i += 1
                j += 1
        while i < n1:
            sum1 += nums1[i]
            i += 1
        while j < n2:
            sum2 += nums2[j]
            j += 1
        return max(sum1, sum2) % MOD