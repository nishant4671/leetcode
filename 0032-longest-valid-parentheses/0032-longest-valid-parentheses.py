class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # dp[i] = length of longest valid parentheses substring ending at index i
        # Transition:
        # 1) If s[i] == ')' and s[i-1] == '(':
        #    dp[i] = dp[i-2] + 2 (if i >= 2)
        # 2) If s[i] == ')' and s[i-1] == ')' and the character before the previous valid block is '(':
        #    let prev_len = dp[i-1]
        #    let match_pos = i - prev_len - 1
        #    if match_pos >= 0 and s[match_pos] == '(':
        #        dp[i] = dp[i-1] + 2 + dp[match_pos-1] (if match_pos >= 1)
        # Track the maximum dp value as answer.
        n = len(s)
        dp = [0] * n
        max_len = 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                else:
                    prev_len = dp[i-1]
                    match_pos = i - prev_len - 1
                    if match_pos >= 0 and s[match_pos] == '(':
                        dp[i] = dp[i-1] + 2 + (dp[match_pos-1] if match_pos >= 1 else 0)
                if dp[i] > max_len:
                    max_len = dp[i]
        return max_len