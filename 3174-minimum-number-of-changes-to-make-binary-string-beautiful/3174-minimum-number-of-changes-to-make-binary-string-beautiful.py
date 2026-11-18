class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        changes = 0
        # Iterate through the string, considering characters in pairs.
        # Since the string length is even, we can process s[0],s[1], then s[2],s[3], and so on.
        # A beautiful string 's_prime' must satisfy s_prime[2k] == s_prime[2k+1] for all k.
        # This is because any substring in a beautiful partition must have an even length
        # and contain only identical characters. If a substring starts at an even index
        # and has even length, it must cover an even number of characters.
        # This implies that any pair (s_prime[2k], s_prime[2k+1]) must fall
        # entirely within one such beautiful substring. If s_prime[2k] were the end
        # of one substring and s_prime[2k+1] the start of another, the first substring
        # would have an odd length (since it ends at an even index relative to s' start, and starts at an even index).
        # Thus, s_prime[2k] and s_prime[2k+1] must belong to the same segment,
        # and therefore must be identical.
        for i in range(0, n, 2):
            # If the characters in the current pair are different,
            # one change is required to make them identical ('00' or '11').
            if s[i] != s[i+1]:
                changes += 1
        return changes