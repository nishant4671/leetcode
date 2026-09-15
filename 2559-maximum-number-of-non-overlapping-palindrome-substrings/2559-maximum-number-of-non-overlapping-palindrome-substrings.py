class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        # palindrome[i][j] indicates s[i..j] is palindrome
        palindrome = [[False]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            pi = palindrome[i]
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or palindrome[i+1][j-1]):
                    pi[j] = True
        dp = [0]*(n+1)
        for i in range(n):
            # carry forward
            if dp[i+1] < dp[i]:
                dp[i+1] = dp[i]
            # try palindromes starting at i
            min_end = i + k - 1
            if min_end >= n:
                continue
            row = palindrome[i]
            for end in range(min_end, n):
                if row[end]:
                    if dp[end+1] < dp[i] + 1:
                        dp[end+1] = dp[i] + 1
        return dp[n]