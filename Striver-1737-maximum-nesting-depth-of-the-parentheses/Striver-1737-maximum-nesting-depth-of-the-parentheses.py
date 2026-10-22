class Solution:
    def maxDepth(self, s: str) -> int:
        """
        Calculates the maximum nesting depth of parentheses in a valid parentheses string.

        Args:
            s: The input string, guaranteed to be a valid parentheses string.

        Returns:
            The maximum nesting depth.
        """
        max_depth = 0
        current_depth = 0

        for char in s:
            if char == '(':
                # Encountered an opening parenthesis, increase current depth
                current_depth += 1
                # Update max_depth if current_depth is greater
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                # Encountered a closing parenthesis, decrease current depth
                current_depth -= 1
            # Other characters (digits, operators) do not affect depth

        return max_depth