class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        total_palindromes = 0

        # Helper function to expand around a center (l, r)
        # and return the number of palindromes found
        def expand_and_count(l: int, r: int) -> int:
            count_from_center = 0
            while l >= 0 and r < n and s[l] == s[r]:
                count_from_center += 1
                l -= 1
                r += 1
            return count_from_center

        for i in range(n):
            # Case 1: Odd length palindromes. The center is a single character s[i].
            # e.g., "aba", where 'b' is the center.
            total_palindromes += expand_and_count(i, i)

            # Case 2: Even length palindromes. The center is two characters s[i] and s[i+1].
            # e.g., "abba", where "bb" is the center.
            total_palindromes += expand_and_count(i, i + 1)
        
        return total_palindromes