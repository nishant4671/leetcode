class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        m = len(nums1)
        n = len(nums2)

        if m < n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        dp = [0] * (n + 1)

        for i in range(1, m + 1):
            prev_diag_val = 0 
            for j in range(1, n + 1):
                temp = dp[j] 

                if nums1[i-1] == nums2[j-1]:
                    dp[j] = 1 + prev_diag_val
                else:
                    dp[j] = max(dp[j], dp[j-1])
                
                prev_diag_val = temp
            
        return dp[n]