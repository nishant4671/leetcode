class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        len_s = len(s)
        len_t = len(t)

        # dp[j] will store the number of distinct subsequences of s up to the current character (s[i-1])
        # that equal t up to index j (t[j-1]).
        # The size is len_t + 1 to handle an empty prefix of t (t[:0]) at index 0.
        dp = [0] * (len_t + 1)

        # Base case: An empty string t (t[:0]) can always be formed in 1 way
        # from any prefix of s (by deleting all characters).
        # This initializes dp[0] to 1 for all implicit rows.
        dp[0] = 1

        # Iterate through string s (from s[0] to s[len_s-1])
        for i in range(1, len_s + 1):
            # Iterate through string t backwards (from t[len_t-1] down to t[0])
            # This backward iteration is crucial for the space optimization
            # because dp[j-1] refers to the value from the *previous* row (or s prefix),
            # while dp[j] (before update) also refers to the value from the *previous* row.
            # If we iterated forwards, dp[j-1] would already be updated to the *current* row's value,
            # leading to incorrect results for dp[j] when s[i-1] == t[j-1].
            for j in range(len_t, 0, -1): 
                if s[i-1] == t[j-1]:
                    # If the characters s[i-1] and t[j-1] match:
                    # We have two ways to form t[:j] from s[:i]:
                    # 1. Use s[i-1] to match t[j-1]: This adds the number of ways
                    #    to form t[:j-1] from s[:i-1], which is dp[j-1] (before its current row update).
                    # 2. Do not use s[i-1]: This means we need to form t[:j] from s[:i-1],
                    #    which is dp[j] (before its current row update).
                    dp[j] = dp[j] + dp[j-1]
                # else:
                    # If s[i-1] != t[j-1]:
                    # We cannot use s[i-1] to match t[j-1]. So we must skip s[i-1].
                    # The number of ways to form t[:j] from s[:i] is then the same
                    # as forming t[:j] from s[:i-1]. This value is already stored in dp[j]
                    # from the previous iteration of `i`, so no change is needed.

        return dp[len_t]