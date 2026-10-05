class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 0
        for i, char in enumerate(s):
            if char == '(':
                depth += 1
            else:  # char == ')'
                depth -= 1
                # If the current ')' immediately follows an '(', it means we've found a "()" unit.
                # The score contributed by this "()" unit depends on its depth.
                # The 'depth' variable, after decrementing, represents how many layers of outer
                # parentheses enclose the current "()" unit.
                # For a "()" at the outermost layer, depth will be 0 (after decrementing), contributing 2^0 = 1.
                # For "()" nested inside one layer (e.g., in "(())"), depth will be 1 (after decrementing),
                # contributing 2^1 = 2.
                if s[i-1] == '(':
                    score += (1 << depth) # This is equivalent to 2 ** depth
        return score