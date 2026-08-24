class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        
        start = 0
        max_len = 0
        
        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            # Odd-length palindromes (single character center)
            len1 = expand_around_center(i, i)
            # Even-length palindromes (two character center)
            len2 = expand_around_center(i, i + 1)
            
            cur_len = max(len1, len2)
            if cur_len > max_len:
                max_len = cur_len
                start = i - (cur_len - 1) // 2

        return s[start:start + max_len]